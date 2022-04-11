import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
class Preprocessor:
    def remove_unwanted_spaces(self,data):
        self.data = data
        try:
            self.df_without_spaces=self.data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
            return self.df_without_spaces
        except Exception as e:
            raise Exception()
    def remove_columns(self,data,columns):
        self.data=data
        self.columns=columns
        try:
            self.useful_data=self.data.drop(labels=self.columns, axis=1)
            return self.useful_data
        except Exception as e:
            raise Exception()
    def separate_label_feature(self, data, label_column_name):
        try:
            self.X=data.drop(labels=label_column_name,axis=1)
            self.Y=data[label_column_name]
            return self.X,self.Y
        except Exception as e:
            raise Exception()
    def is_null_present(self,data):
        self.null_present = False
        self.cols_with_missing_values=[]
        self.cols = data.columns
        try:
            self.null_counts=data.isna().sum()
            for i in range(len(self.null_counts)):
                if self.null_counts[i]>0:
                    self.null_present=True
                    self.cols_with_missing_values.append(self.cols[i])
            # if(self.null_present):
            #     self.dataframe_with_null = pd.DataFrame()
            #     self.dataframe_with_null['columns'] = data.columns
            #     self.dataframe_with_null['missing values count'] = np.asarray(data.isna().sum())
            #     self.dataframe_with_null.to_csv('preprocessing_data/null_values.csv') # storing the null column information to file
            return self.null_present, self.cols_with_missing_values
        except Exception as e:
            raise Exception()
    def impute_missing_values(self, data, cols_with_missing_values):
        self.data= data
        self.cols_with_missing_values=cols_with_missing_values
        try:
            self.imputer = KNNImputer()
            for col in self.cols_with_missing_values:
                self.data[col] = self.imputer.fit_transform(self.data[col])
            return self.data
        except Exception as e:raise Exception()
    def scale_numerical_columns(self,data):
        self.data=data
        try:
            self.num_df = self.data.select_dtypes(include=['int64']).copy()
            self.scaler = StandardScaler()
            self.scaled_data = self.scaler.fit_transform(self.num_df)
            self.scaled_num_df = pd.DataFrame(data=self.scaled_data, columns=self.num_df.columns)
            return self.scaled_num_df
        except Exception as e:
            raise Exception()
    def encode_categorical_columns(self,data):
        try:
            self.cat_df = data.select_dtypes(include=['object']).copy()
            for col in self.cat_df.columns:
                self.cat_df = pd.get_dummies(self.cat_df, columns=[col], prefix=[col], drop_first=True)
            return self.cat_df
        except Exception as e:
            raise Exception()
    def handle_imbalanced_dataset(self,x,y):
        try:
            self.rdsmple = RandomOverSampler()
            self.x_sampled,self.y_sampled  = self.rdsmple.fit_sample(x,y)
            return self.x_sampled,self.y_sampled
        except Exception as e:raise Exception()
