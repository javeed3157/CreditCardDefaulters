from sklearn.model_selection import train_test_split
from data_ingestion import data_loader
from data_preprocessing import preprocessing
from data_preprocessing import clustering
from best_model_finder import tuner
from file_operations import file_methods
class trainModel:
    def trainingModel(self):
        try:
            data_getter=data_loader.Data_Getter()
            data=data_getter.get_data()
            preprocessor=preprocessing.Preprocessor()
            X,Y=preprocessor.separate_label_feature(data,label_column_name='default payment next month')
            is_null_present,cols_with_missing_values=preprocessor.is_null_present(X)
            if(is_null_present):
                X=preprocessor.impute_missing_values(X,cols_with_missing_values)
            kmeans=clustering.KMeansClustering()
            number_of_clusters=kmeans.elbow_plot(X)
            print("No of clusters are : ",number_of_clusters)
            X=kmeans.create_clusters(X,number_of_clusters)
            X['Labels']=Y
            list_of_clusters=X['Cluster'].unique()
            print("List of clusters are : ",list_of_clusters)
            for i in list_of_clusters:
                cluster_data=X[X['Cluster']==i]
                cluster_features=cluster_data.drop(['Labels','Cluster'],axis=1)
                cluster_label= cluster_data['Labels']
                x_train, x_test, y_train, y_test = train_test_split(cluster_features, cluster_label, test_size=0.2, random_state=355)
                train_x = preprocessor.scale_numerical_columns(x_train)
                test_x = preprocessor.scale_numerical_columns(x_test)
                model_finder=tuner.Model_Finder()
                best_model_name,best_model=model_finder.get_best_model(train_x,y_train,test_x,y_test)
                print("Cluster no : ",i)
                file_op = file_methods.File_Operation()
                save_model=file_op.save_model(best_model,best_model_name+str(i))
        except Exception as e:
            raise Exception