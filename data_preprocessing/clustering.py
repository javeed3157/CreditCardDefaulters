import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kneed import KneeLocator
from file_operations import file_methods
class KMeansClustering:
    def elbow_plot(self,data):
        wcss=[]
        try:
            for i in range (1,11):
                kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
                kmeans.fit(data)
                wcss.append(kmeans.inertia_)
            plt.plot(range(1,11),wcss)
            plt.title('The Elbow Method')
            plt.xlabel('Number of clusters')
            plt.ylabel('WCSS')
            plt.savefig('preprocessing_data/K-Means_Elbow.PNG')
            self.kn = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
            return self.kn.knee
        except Exception as e:
            raise Exception()
    def create_clusters(self,data,number_of_clusters):
        self.data=data
        try:
            self.kmeans = KMeans(n_clusters=number_of_clusters, init='k-means++', random_state=42)
            self.y_kmeans=self.kmeans.fit_predict(data)
            self.file_op = file_methods.File_Operation()
            self.save_model = self.file_op.save_model(self.kmeans, 'KMeans')
            self.data['Cluster']=self.y_kmeans
            return self.data
        except Exception as e:
            raise Exception()
