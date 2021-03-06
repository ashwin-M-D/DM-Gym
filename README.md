# DM-Gym

Data Mining Gym Environment for Reinforcement Learning ("RL")

### Installation

You can download the git repository directly and keep the dm_gym folder inside your project folder.

You could also use the following steps to install DM-Gym, which can be accessed anywhere in the system:

```bash
git clone https://github.com/ashwin-M-D/DM-Gym.git
cd DM-Gym
pip install -e
```

The package is also in the pypi repository so it can be installed using pip.

```bash
pip install dm-gym
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
conda env create -f dmgym_environment.yml

## Activate conda environment and cd to the folder containing the experiment files.
conda activate myenv_dmgym_testing
cd ..
cd experiments
```

### Available Environments

1. Clustering:

   All these environments involve records which arrive in a random order and they are classified into one of k clusters. The value of k is predefined similar to k-means clustering.

   Basically the input / state space is a single record from the dataset and the output is a discreet variable which is an integer between 0 and k-1, each specifying a specific cluster.

   - clustering-v0: Reward function is negative of log(db-index)

     ![Reward Function for Clustering-v0](./images/clustering_v0.png)

     This is a poor performing environment.

   - clustering-v1: Reward function is based on both the distance and also the db-index.

     ![Reward Function for Clustering-v1](./images/clustering_v1.png)

     This performs better than clustering-v0. However, it is suggested to use one of the other two clustering environments mentioned below:
   
   - clustering-v2: Uses a different reward system which is either p-1 or p at each step. Based on the paper "A Reinforcement Learning Approach to Online Clustering" [1]. Please use a low gamma value with this environment for optimal results.
   
   - clustering-v3: This has the best performance among all the clustering environments. It converts the problem into a classification problem internally. However, to showcase true capabilities of RL, this should not be used. Use a low gamma value with this environment.
   
2. Classification:

   Classification is done by reading a single record at a time and checking the output of your RL agent against the class it belongs to.

   * classification-v0: This has very good performance and the reward function is defined as 1, if the output of the agent and the class it actually belongs to match. It is -1 if they don't match. It is again recommended to use a low gamma value for this environment.

### Environments planned for the future

1. Linear Regression environments.
2. More Classification environments.

#### Notes:

1. **See Testing folder to see examples of each of the environments and their outputs.**

2. **Documentation for all available functions are provided in the documentation folder. This folder will be updated regularly to make sure there is no ambiguity in the usage of the environments**

### References

1. Likas, A., 1999. A reinforcement learning approach to online clustering. _Neural computation_, _11_(8), pp.1915-1932.
   <a href="http://62.217.125.140/jspui/bitstream/123456789/11133/1/Likas-1999-A%20reinforcement%20learning%20approach%20to%20online%20clustering.pdf">PDF</a>

2. Hubbs, C.D., Perez, H.D., Sarwar, O., Sahinidis, N.V., Grossmann, I.E. and Wassick, J.M., 2020. OR-Gym: A Reinforcement Learning Library for Operations Research Problems. _arXiv preprint arXiv:2008.06319_. <a href="https://arxiv.org/pdf/2008.06319">PDF</a> <a href="https://github.com/hubbs5/or-gym">GitHub</a>
