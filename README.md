# DM-Gym

Data Mining Gym Environment for Reinforcement Learning

### Installation

You can download the git repository directly and keep the dm_gym folder inside your project folder.

You could also use the following steps to install DM-Gym in your system to be accessible anywhere:

```bash
git clone https://github.com/ashwin-M-D/DM-Gym.git
cd DM-Gym
pip install -e
```

### Testing

To test the environment using the test codes provided, you need to have ray installed. Please use the conda environment file provided to setup your environment. Then, install DM-Gym as mentioned above and proceed with running the python notebooks provided. All of this can be done as follows.

```bash
## Installing DM-Gym
git clone https://github.com/ashwin-M-D/DM-Gym.git
cd DM-Gym
pip install -e

## Creating the conda environment
cd testing
cd conda_envs
conda env create -f ray_environment.yml

## Activate conda environment and cd to the folder containing the experiment files.
conda activate myenv_ray
cd ..
cd experiments
```



### Available Environments

1. Clustering:

   All these environments involve records which arrive in a random order and they are classified into one of k clusters. The value of k is predefined similar to k-means clustering.

   Basically the input / state space is a single record from the dataset and the output is a discreet variable which is an integer between 0 and k-1, each specifying a specific cluster.

   * Clustering-v0: Reward function is based on distance from the centroids
   * Clustering-v1: Reward function is negative of db-index
   * Clustering-v2: Reward function is based on distance and also number of points in each cluster
   * Clustering-v3: Reward function is based on db-index but is only received in the end of each episode. i.e one the environment goes through the entire dataset.
   * Clustering-v4: Reward function is based on both the distance and also the db-index.

### Environments planned in the future

1. Classification
2. Linear Regression

#### Notes:

1. **See Testing folder to see examples of each of the environments and their outputs**

2. **Documentation for all available functions will be made available soon.**