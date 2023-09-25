# Studying the association between Gitcoin bounties and issue-addressing outcomes

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8313155.svg)](https://doi.org/10.5281/zenodo.8313155)

This repository provides a replication package of our paper submission titled "Studying the association between Gitcoin bounties and issue-addressing outcomes". 

## Abstract

The development of open-source software (OSS) projects usually have been driven through collaborations among contributors and strongly relies on volunteering. Thus, allocating software practitioners (e.g., contributors) to a particular task is non-trivial and draws attention away from the development. Therefore, a number of bug bounty platforms have emerged to address this problem through bounty rewards. Especially, Gitcoin, a new bounty platform, introduces a bounty reward mechanism that allows individual issue owners (backers) to define a reward value using cryptocurrencies rather than using crowdfunding mechanisms. Although a number of studies have investigated the phenomenon on bounty platforms, those rely on different bounty reward systems. Our study thus investigates the association between the Gitcoin bounties and their outcomes (i.e., success and non-success). We empirically study over 4,000 issues with Gitcoin bounties using statistical analysis and machine learning techniques. We also conducted a comparative study with the Bountysource platform to gain insights into the usage of both platforms. Our study highlights the importance of factors such as the length of the project, issue description, type of bounty issue, and the bounty value, which are found to be highly correlated with the outcome of bounty issues. These findings can provide useful guidance to practitioners.

## Folder structure
```
Dataset/
├─ activities_collection_3.csv
├─ changedBounty2.csv
├─ gitcoin_dataset_5.csv
Script/
├─ gitcoin_point_biserial.ipynb 
├─ gitcoin_random_forests_setting1.ipynb
├─ gitcoin_random_forests_setting2.ipynb 
├─ gitcoin_logistic_setting1.ipynb 
├─ gitcoin_logistic_setting2.ipynb 
├─ gitcoin_rest_api.ipynb 
├─ gitcoin_baseline.ipynb 
├─ coin_real_value.ipynb
README.md
```

## Content
- **Dataset** contains
  - `gitcoin_dataset_5.csv`
    - The dataset only contains the 'Mainnet' network.
    - The dataset includes the extracted attributes as follows:
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
    - coin_value
    ```
  - `activities_collection_3.csv`
    - The duration-related features are as follows:
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
  - `changedBounty2.csv`
    - The bounty value-related features are as follows:
    ```
    - increased_bounty_times
    - changed_bounty_value
    ```


gitcoin_point_biserial.ipynb : Conducting the analysis using the point biserial correlation method.
gitcoin_random_forests_setting1.ipynb : Random Forests Configuration for Gitcoin Dataset (Setting 1)
gitcoin_random_forests_setting2.ipynb : Random Forests Configuration for Gitcoin Dataset (Setting 2)
gitcoin_logistic_setting1.ipynb : Logistic Regression Analysis for Gitcoin Dataset (Setting 1)
gitcoin_logistic_setting2.ipynb : Logistic Regression Analysis for Gitcoin Dataset (Setting 2)
gitcoin_rest_api.ipynb : Data Collection from gitcoin_rest_api
gitcoin_baseline.ipynb : Baseline
coin_real_value.ipynb : Analysis of Real Coin Value

## Authors
- Morakot Choetkiertikul
- Arada Puengmongkolchaikit
- Pandaree Chandra
- [Rungroj Maipradit](https://rungroj-m.github.io)
- [Hideaki Hata](https://hideakihata.github.io/)
- Chaiyong Ragkhitwetsagul
- Thanwadee Sunetnanta
- [Kenichi Matsumoto](https://matsumotokenichi.github.io/)
