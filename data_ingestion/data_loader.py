import pandas as pd

class Data_Getter:
    def __init__(self):
        self.training_file='Training_FileFromDB/InputFile.csv'
    def get_data(self):
        try:
            self.data= pd.read_csv(self.training_file)
            return self.data
        except Exception as e:
            raise Exception()
