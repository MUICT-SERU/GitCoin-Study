from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import operator
import sys

# Change datetime format
def try_parsing_date(text):
    for fmt in ('%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%S.%f%z'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass


# Set database environment
client = MongoClient("mongodb://localhost:27017")

Data_Collection = client["Data_Collection"]

myCol = Data_Collection["allBounty_3_onlyMainnet"]

data = myCol.find({}, {"title": 1, "activities": 1, "bounty_type": 1, "project_type": 1, "pk": 1, "value_in_eth": 1, "value_in_usdt": 1, "value_in_token": 1,
                       "status": 1, "value_true": 1})

# Create arrays of fields
pj_pk = []
pj_titles = []
increased_bounty_times = []
latest_increased_date = []
old_bounty_value = []
new_bounty_value = []
changed_value_final = []

old_value = 0
new_value = 0
max_title_pk = dict()

# Calculate Changed Bounty Values
for collection in data:
    title = collection["title"]
    get_pk = collection["pk"]
    status = collection["status"]
    value_in_eth = collection["value_in_eth"]
    value_in_usdt = collection["value_in_usdt"]

    current_bounty_date_keep = list() #Use list() for keeping most current created date of 'increased_bounty'
    temp_activity = None

    all_activities = []
    increased_bounty_activities = []

    for activity in collection["activities"]:
        all_activities.append(try_parsing_date(activity["created"]))

        if activity["activity_type"] == "new_bounty":
            new_bounty_date = activity["created"] #Retreive 'created' date of 'new_bounty' field
            new_bounty_date_obj = try_parsing_date(new_bounty_date) #Convert date from 'str' to 'datetime' format

            if (activity.get("metadata").get("new_bounty") != None):
                if("value_in_eth" in activity.get("metadata").get("new_bounty").keys()):
                    old_value = activity.get("metadata").get("new_bounty")["value_in_eth"]

            if (activity.get("metadata") != None):
                if ("value_in_eth" in activity.get("metadata").keys()):
                    old_value = activity.get("metadata")["value_in_eth"]

        if activity["activity_type"] == "increased_bounty":
            increased_bounty_date = activity["created"] #Retreive 'created' date of 'increased_value' field
            increased_bounty_date_obj = try_parsing_date(increased_bounty_date) #Convert date from 'str' to 'datetime' format
            current_bounty_date_keep.append(increased_bounty_date_obj)  # Keep created date

    index = None
    if(len(current_bounty_date_keep) != 0):
        max_bounty_date = max(current_bounty_date_keep) # Find the max date of increased bounty
        index = all_activities.index(max_bounty_date)   # Use index to find the value_in_eth of max date

        activities = collection["activities"]

        if (activities[index].get("metadata").get("new_bounty") != None):
            if ("value_in_eth" in activities[index].get("metadata").get("new_bounty").keys()):
                new_value = activities[index].get("metadata").get("new_bounty")["value_in_eth"]
        if (activities[index].get("metadata") != None):
            if ("value_in_eth" in activities[index].get("metadata").keys()):
                new_value = activities[index].get("metadata")["value_in_eth"]
        print(title)
        print("Old Value: ", old_value)
        print("New Value: ", new_value)

        if new_value == 'None' or old_value == 'None':
            changed_value = 'None'
            if old_value == 'None':
                changed_value = new_value
        else:
            changed_value = float(new_value) - float(old_value)

        print("#Times: ", len(current_bounty_date_keep))
        print("### Changed Value: ", changed_value)

    else:
        continue

    pj_pk.append(get_pk)
    pj_titles.append(title)
    increased_bounty_times.append(len(current_bounty_date_keep))
    latest_increased_date.append(max_bounty_date)
    old_bounty_value.append(old_value)
    new_bounty_value.append(new_value)
    changed_value_final.append(changed_value)

repo = {
    'pk': pj_pk,
    'title': pj_titles,
    'increased_bounty_times': increased_bounty_times,
    'latest_increased_bounty': latest_increased_date,
    'old_bounty_value': old_bounty_value,
    'new_bounty_value': new_bounty_value,
    'changed_bounty_value': changed_value_final
}

df = pd.DataFrame(repo, dtype='object')
# df.to_csv('changedBounty2.csv')

