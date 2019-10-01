"""
utility functions for working with DataFrames
"""

import pandas
import numpy as np

TEST_DF = pandas.DataFrame([1, 2, 3])


class df_functions:
    def list_to_column(self, X, list, name='column'):
        """
        adds list to dataframe
        paramters:
            X = DataFrame
            list = list type
            name = str type
        """
        X[name] = list
        return X

    def round_Data_Frame(self, X, n=2):
        """
        Will round all numbers within the dataframe to defined
        parameters:
            X = DataFrame
            n = int type. will round to this value. 2 if not defined
        """
        for x in X.columns:
            if type(X[x][0]) == np.float64:
                temp = []
                for y in X[x]:
                    temp.append(round(y, n))
                X[x] = temp

        return X
