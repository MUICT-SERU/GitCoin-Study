# Studying the association between Gitcoin bounties and issue-addressing outcomes

This repository provides a replication package of our paper submission titled "Studying the association between Gitcoin bounties and issue-addressing outcomes". 

## Abstract

The development of open source software (OSS) projects usually have been driven through collaborations among contributors and strongly rely on volunteering. Thus, allocating software practitioners (e.g., contributors) on a particular task is non trivial and draws attention away from the development. Therefore, a number of bug bounty platforms have been emerged to address this problem through bounty rewards. Especially, Gitcoin, a new bounty platform, introduces a bounty reward mechanism that allow individual issue owners (backer) to define a reward value using cryptocurrencies rather than using crowdfunding mechanisms. Although a number studies investigated the phenomenon on bounty platforms, those rely on different bounty reward systems. Our study thus investigates the association between the Gitcoin bounty and their outcomes (i.e. success and non-success). We empirically study over 4,000 Gitcoin bounty issues using statistical analysis and machine learning techniques. We found that the length of bounty description, the bounty value, the bounty proposing time, and the contributor's required experience level are important factors influencing bounty issue resolving outcome.

## Folder structure


## Content
- Dataset: a dataset directory
  - `gitcoin_dataset_5.csv`
    - The dataset only contains the 'Mainnet' network.
    - The dataset ended on 31 December 2020.
    - The dataset is including the new field as the following:
    ```
    - description_length
    - duration_create_to_expire
    - expires_date_ymd
    - web3_created_ymd
    - is_paid
    - is_success
    - number_of_activities
    - number_of_fulfillments
    - number_of_interests
    ```
    - The dataset is excluding some fields as the following:
    ```
    - Array
      - fulfillments array
      - interested array
      - activities array
    - Field with too long description which ruin the format of CSV file
      - issue_description
      - issue_description_text
    ```
  - `activities_collection_3.csv`
    - The dataset is including new fields extracted from the ‘activities array’ as the following:
    ```
    - duration_create_to_new_bounty
    - duration_create_to_firstAct
    - duration_create_to_lastAct
    - duration_create_to_worker_applied
    - duration_worker_applied_to_worker_approved
    - duration_create_to_start
    - duration_create_to_stop
    - duration_create_to_done
    - duration_create_to_submitted
    - duration_create_to_killed
    - number_of_user_in_activities
    - firstAct_activity_type
    - lastAct_activity_type
    ```
  
- Script: Scripts directory
  - `gitcoin_rest_api.ipynb`: the script is for collecting datasets via Gitcoin API.
  - `gitcoin_spearman_correlation.ipynb`: the script for finding Spearman's correlations between each feature.
  - `gitcoin_random_forests_setting1.ipynb`: the script for finding the feature importance of all features.
  - `gitcoin_random_forests_setting2.ipynb`: the script for finding the feature importance of manipulable features.
  - `gitcoin_point_biserial.ipynb`: this script is the calculation of point biserial.

## Authors
- Morakot Choetkiertikul
- Arada Puengmongkolchaikit
- Pandaree Chandra
- [Rungroj Maipradit](https://rungroj-m.github.io)
- [Hideaki Hata](https://hideakihata.github.io/)
- Chaiyong Ragkhitwetsagul
- Thanwadee Sunetnanta
- [Kenichi Matsumoto](https://matsumotokenichi.github.io/)
