# Data Mining Gym

This project was developed by Ashwin Devanga under the supervision of Prof. M Dehghani at Northeastern University. It aims to convert Data Mining problems into Reinforcement Learning problems. This includes Regression, Classification and Clustering problems.

## Installation

### Regular Installs

*The following shell scripts are written for bash but they are mostly similar for windows and mac users as well.*

The repository is available on PyPI.org and so you can use pip to install the package. Just run the following:

```bash
pip install dm-gym
```

### Install from GitHub

To install it into your python development environment and to make sure you have the latest version, you can install from GitHub directly. To do this run the following in your terminal:

```bash
git clone https://github.com/ashwin-M-D/DM-Gym.git
cd DM-Gym
pip install -e
cd ..
rm -rf ./DM-Gym
```

If you need to modify the reward function in anyway, you may prefer using the package directly in your project folder instead of installing it. To do this open up your terminal in your project folder and run the following:

```bash
git clone https://github.com/ashwin-M-D/DM-Gym.git
mv ./DM-Gym/dm_gym ./
rm -rf ./DM-Gym
```

### Setting up a conda environment to run the test files.

An environment file has been provided which installs all the required packages into an environment called myenv_dmgym_testing. To install the environment, navigate to the folder containing the *.yml file and run the following command:

```bash
conda env create -f dm_gym_environment.yml
conda activate myenv_dmgym_testing
```

This will create the environment. If there are any issues with your scipy installation in the environment, do make sure you run this:

```bash
conda update --name myenv_dmgym_testing scipy
```

