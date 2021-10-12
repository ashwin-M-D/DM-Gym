import numpy as np
import pandas as pd

from copy import deepcopy
from sklearn.metrics import davies_bouldin_score as dbindex


class Reward_Function:

    def __init__(self):
        pass

    def reward_function(self, df, k, done):
        reward = 0

        if done == True:
            try:
                accuracy = dbindex(df[df.columns.drop('action')], df['action'])
                reward = - (accuracy)**2 + (1/(accuracy)**2)
            except:
                accuracy = 1e+10
                reward = -100*len(df.index)
        else:
            reward = 0
            accuracy = 0

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
        return df