from os import listdir
import pandas
class dataTransformPredict:
     def __init__(self):
          self.goodDataPath = "Prediction_Raw_Files_Validated/Good_Raw"
     def replaceMissingWithNull(self):
          try:
               onlyfiles = [f for f in listdir(self.goodDataPath)]
               for file in onlyfiles:
                    data = pandas.read_csv(self.goodDataPath + "/" + file)
                    data.to_csv(self.goodDataPath+ "/" + file, index=None, header=True)
          except Exception as e:
               raise e
