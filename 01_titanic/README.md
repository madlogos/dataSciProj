# Titanic 生存预测 Survival Prediction

## 数据 Data

数据来自[kaggle](https://www.kaggle.com/c/titanic)，包括train.csv和test.csv。要求使用train数据集构建模型，用test数据集验证。
The data is from [kaggle](https://www.kaggle.com/c/titanic). It includes train.csv and test.csv. Train dataset is used to build model and test dataset is used for validation.

**数据结构 Data Structure**

Variable | Definition | Key
:--------|:-----------|:------
survival | Survival | 0 = No, 1 = Yes
pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd
sex | Sex |
Age | Age in years |
sibsp | # of siblings / spouses aboard the Titanic |
parch | # of parents / children aboard the Titanic |
ticket | Ticket number |
fare | Passenger fare |
cabin | Cabin number |
embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton
