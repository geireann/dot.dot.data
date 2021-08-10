import numpy as np
import pandas as pd
import sqlite3
import random
import statsmodels.api as sm
from statsmodels.tools import eval_measures
from sklearn.metrics import r2_score
from util import all_variable_names_in_df, train_test_split, RANDOM_SEED


def regression(train_df, test_df, ind_var_names: list, dep_var_name: str):
    """
    Implement Linear Regression using StatsModel.

    inputs:
        - train_df: a Pandas DataFrame, containing all the training samples
        - test_df: a Pandas DataFrame, containing all the testing samples
        - ind_var_names: a list of strings of independent variable columns
                        that we want to include in the model
        - dep_var_name: the name of the dependent variable of our model
    

    outpus:
        - mse_train: the mean-squared error of the model (trained on the training
                    data), evaluated on the training dataset
        - mse_test: the mean-squared error of the model (trained on the training
                    data), evaluated on the testing dataset
        - rsquared_val: the r-squared value of the model (trained on the training
                    data), evaluated on the testing dataset
    """
    ## Stencil: Error check whether the input that you provided to the function is correct or not
    # Do not modify
    for df in [train_df, test_df]:
        assert all_variable_names_in_df(ind_var_names + [dep_var_name], df)

    # Construct X_train, X_test, y_train, y_test from train_df and test_df, where
    # X_train is a numpy array of all the independent variable instances from train_df,
    # y_train is a numpy array of all the dependent variable instances from train_df,
    # and the same applies to X_test and y_test from test_df.
    # Hint: Look up (1) how to select a Pandas DataFrame B with a subset of columns from a given DataFrame A,
    #           and (2) how to use Pandas .to_numpy() function.
    
    train_ind_var_df = train_df[ind_var_names]
    train_dep_var_df = train_df[dep_var_name]
    test_ind_var_df = test_df[ind_var_names]
    test_dep_var_df = test_df[dep_var_name]
    # construct training data and convert to numpy array
    X_train = train_ind_var_df.to_numpy()
    y_train = train_dep_var_df.to_numpy()
    # construct testing data and convert to numpy array
    X_test = test_ind_var_df.to_numpy()
    y_test = test_dep_var_df.to_numpy()

    # Using statsmodel, fit a linear regression model to the training dataset
    # You may checkout statsmodel's documentation here: https://www.statsmodels.org/stable/regression.html
    # spector_data = sm.datasets.spector.load(as_pandas=False)
    X_train = sm.add_constant(X_train)
    train_mod = sm.OLS(y_train, X_train)
    train_res = train_mod.fit()

    # Add constant for testing independent variable
    X_test = sm.add_constant(X_test)

    # Using statsmodel's eval_measures MSE calculation function,
    # calculate the Mean-squared Error of the model above (on the training dataset)
    train_mse = eval_measures.mse(y_train, train_res.predict(X_train))

    # Similarly, calculate the Mean-squared Error of the model above (on the testing dataset)
    test_mse = eval_measures.mse(y_test, train_res.predict(X_test))

    # Calculate the *test* R-squared value (using sklearn's r2_score function)
    test_r2 = r2_score(y_test, train_res.predict(X_test))

    # Print out the summary to see more information as needed
    print(train_res.summary())

    # Replace these values with whatever you found!
    mse_train, mse_test, rsquared_val = train_mse, test_mse, test_r2
    
    # And return them! :)
    return mse_train, mse_test, rsquared_val
    

def main():
    # Load the data from the bike-sharing.csv file into a Pandas DataFrame. Do not change
    # the variable name /data/
    # Hint: Look at the Pandas' read_csv function
    conn = sqlite3.connect('../data-cleaning/data.db')
    c = conn.cursor()

    dfgames = pd.read_sql_query("select * from games_final_cat;", conn)
    
    print("Columns: ", dfgames.columns)

    IND_VAR_NAMES = ['elo_diff', 'age_diff', 'time_since_gm_diff']

    DEP_VAR_NAME = "result"

    dfnew = dfgames[[DEP_VAR_NAME] + IND_VAR_NAMES]


    for col in [DEP_VAR_NAME] + IND_VAR_NAMES:
        dfnew[col] = dfnew[col].astype(int)


    print(dfnew)
    # Using the imported train_test_split function (from util.py), create the train_df and
    # test_df that will be passed into regression.
    split = train_test_split(dfgames)
    train_df, test_df = split[0], split[1]

    # Call regression and perform other calculations as you deem necessary to answer the
    # questions posed for this section.
    print(regression(train_df, test_df, IND_VAR_NAMES, DEP_VAR_NAME))

############ DON'T MODIFY BELOW THIS LINE ############

if __name__ == "__main__":
    main()