from Training_Raw_data_validation.rawValidation import Raw_Data_validation
from DB_Training.DBTraining import dBOperation
from DataTransform_Training.DataTransformation import dataTransform
import os
class train_validation:
    def __init__(self,path):
        self.raw_data = Raw_Data_validation(path)
        self.dataTransform = dataTransform()
        self.dBOperation = dBOperation()
        self.cwd=os.getcwd()
    def train_validation(self):
        try:
            LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, noofcolumns = self.raw_data.valuesFromSchema()
            regex = self.raw_data.manualRegexCreation()
            self.raw_data.validationFileNameRaw(regex, LengthOfDateStampInFile, LengthOfTimeStampInFile)
            self.raw_data.validateColumnLength(noofcolumns)
            self.raw_data.validateMissingValuesInWholeColumn()
            self.dataTransform.replaceMissingWithNull()
            self.dBOperation.createTableDb('Training', column_names)
            self.dBOperation.insertIntoTableGoodData('Training')
            self.raw_data.deleteExistingGoodDataTrainingFolder()
            self.raw_data.moveBadFilesToArchiveBad()
            self.dBOperation.selectingDatafromtableintocsv('Training')
        except Exception as e:
            raise e
