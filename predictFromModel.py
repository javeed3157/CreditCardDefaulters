import pandas as pd
from file_operations import file_methods
from data_preprocessing import preprocessing
from data_ingestion import data_loader_prediction
from Prediction_Raw_Data_Validation.predictionDataValidation import Prediction_Data_validation
class prediction:
    def __init__(self,path):
        self.pred_data_val = Prediction_Data_validation(path)
    def predictionFromModel(self):
        try:
            self.pred_data_val.deletePredictionFile()
            data_getter=data_loader_prediction.Data_Getter_Pred()
            data=data_getter.get_data()
            preprocessor = preprocessing.Preprocessor()
            is_null_present, cols_with_missing_values = preprocessor.is_null_present(data)
            if (is_null_present):
                data = preprocessor.impute_missing_values(data, cols_with_missing_values)
            X = preprocessor.scale_numerical_columns(data)
            file_loader=file_methods.File_Operation()
            kmeans=file_loader.load_model('KMeans')
            clusters=kmeans.predict(X)
            X['clusters']=clusters
            clusters=X['clusters'].unique()
            for i in clusters:
                cluster_data= X[X['clusters']==i]
                cluster_data = cluster_data.drop(['clusters'],axis=1)
                model_name = file_loader.find_correct_model_file(i)
                model = file_loader.load_model(model_name)
                result=(model.predict(cluster_data))
            final= pd.DataFrame(list(zip(result)),columns=['Predictions'])
            path="Prediction_Output_File/Predictions.csv"
            final.to_csv("Prediction_Output_File/Predictions.csv",header=True,mode='a+')
        except Exception as ex:
            raise ex
        return path
