import numpy as np
import pandas as pd

from copy import deepcopy
from sklearn.metrics import davies_bouldin_score as dbindex


class Reward_Function:

    def __init__(self, max_dist):
        self.max_dist = max_dist
        pass

    def reward_function(self, df, k, total_data_size, obs, action, done):
        reward = 0

        centroids = self.gen_mean_coords(df, k)

        num_clusters = len(df['action'].unique().tolist())

        if(done == True):

            try:
                accuracy = dbindex(df[df.columns.drop('action')], df['action'])
            except:
                accuracy = 1e+10

        else:
            dist = np.linalg.norm(np.array(obs) -
                                  np.array(centroids[action-1]))

            accuracy = dist / self.max_dist

        reward = -accuracy + (num_clusters - k) * len(df.index)/total_data_size

        return reward, accuracy

    def gen_mean_coords(self, df, k):
        centroids = []
        for i in range(1, k+1):
            temp_df = df[df['action'] == i]
            temp_df = temp_df.drop(columns=['action'])
            centroid = []
            for col in temp_df.columns:
                centroid.append(temp_df[col].mean())
            centroids.append(centroid)
        return centroids

    def gen_table(self, coordinates, data):
        df = deepcopy(data)
        data = data.drop(columns=['action'])

        dist = pd.DataFrame()
        j = 0
        for coor in coordinates:
            j = j + 1
            dist_temp = []
            c = np.array(coor)
            for i in range(len(data.index)):
                d = np.array(data.iloc[i].tolist())
                dist_temp.append(np.linalg.norm(c-d))
            dist[j] = dist_temp
        df['centroid'] = dist.idxmin(axis=1)
        df['distance'] = dist.min(axis=1)
        return df
