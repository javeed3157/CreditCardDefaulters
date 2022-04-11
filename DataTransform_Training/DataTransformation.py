from os import listdir
import pandas

class dataTransform:
     def __init__(self):
          self.goodDataPath = "Training_Raw_files_validated/Good_Raw"
     def replaceMissingWithNull(self):
          try:
               onlyfiles = [f for f in listdir(self.goodDataPath)]
               for file in onlyfiles:
                    data = pandas.read_csv(self.goodDataPath + "/" + file)
                    data.to_csv(self.goodDataPath + "/" + file, index=None, header=True)
          except Exception as e:
               raise e
