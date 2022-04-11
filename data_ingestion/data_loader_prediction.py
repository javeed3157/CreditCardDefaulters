import pandas as pd

class Data_Getter_Pred:
    """
    This class shall  be used for obtaining the data from the source for prediction.

    Written By: iNeuron Intelligence
    Version: 1.0
    Revisions: None

    """
    def __init__(self):
        self.prediction_file='Prediction_FileFromDB/InputFile.csv'

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception

         Written By: iNeuron Intelligence
        Version: 1.0
        Revisions: None

        """
        try:
            self.data= pd.read_csv(self.prediction_file) # reading the data file
            return self.data
        except Exception as e:
            raise Exception()


