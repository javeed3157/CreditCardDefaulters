from Prediction_Raw_Data_Validation.predictionDataValidation import Prediction_Data_validation
from DB_Prediction.DBPrediction import dBOperation
from DataTransformation_Prediction.DataTransformationPrediction import dataTransformPredict
class pred_validation:
    def __init__(self,path):
        self.raw_data = Prediction_Data_validation(path)
        self.dataTransform = dataTransformPredict()
        self.dBOperation = dBOperation()
    def prediction_validation(self):
        try:
            LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,noofcolumns = self.raw_data.valuesFromSchema()
            regex = self.raw_data.manualRegexCreation()
            self.raw_data.validationFileNameRaw(regex,LengthOfDateStampInFile,LengthOfTimeStampInFile)
            self.raw_data.validateColumnLength(noofcolumns)
            self.raw_data.validateMissingValuesInWholeColumn()
            self.dataTransform.replaceMissingWithNull()
            self.dBOperation.createTableDb('Prediction',column_names)
            self.dBOperation.insertIntoTableGoodData('Prediction')
            self.raw_data.deleteExistingGoodDataTrainingFolder()
            self.raw_data.moveBadFilesToArchiveBad()
            self.dBOperation.selectingDatafromtableintocsv('Prediction')
        except Exception as e:
            raise e
