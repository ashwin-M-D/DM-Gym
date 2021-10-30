# DM-Gym: Available Features - Environments

The package's features for data management have been explained. Now we explain environment creation for running your RL algorithm.

## Environment basics

The following environments are OpenAI gym compliant. They are completely integrated with the structure specified by OpenAI's gym.

The package has also ensured that the environments can be created in such a way that prebuilt RL libraries such as ray.rllib and ray.tune can run seamlessly with it. The process to setup such an environment is explained below.

## Available Environments

The following environments have been built into dm-gym so far. The details on how each environment works are explained in the environments documentation.

1. clustering-v0
2. clustering-v1
3. clustering-v2
4. clustering-v3
5. classification-v0

## Environment Creation

The easiest way to create an environment is by using dm_gym.create_env() function.

```python
import dm_gym
from dm_gym.create_env import create_env

env_name = "<env_name>"
env_config = {...<"contents explained in environments documentation">...}

env = create_env(env_name, env_config=env_config)
## This creates an initiated environment.
## It is important to note that you need to specify env_config=env_config i.e **kwargs and not *args.
```

The returned object is the environment object. This is what interacts with your RL algorithm.

## Environments with Ray-rllib or Ray-Tune

Ray cannot use the above environment object creation method therefore you will need to add in a function into your project as follows:

```python
import ray
from ray.rllib import agents
from ray import tune

from dm_gym.create_env import ray_create_env
```

```python
def register_env(env_name, env_config={}):
    env = ray_create_env(env_name)
    tune.register_env(env_name, 
        lambda env_name: env(env_name,
            env_config=env_config))
```

```python
env_name = "<env_name>"
env_config = {...<"contents explained in environments documentation">...}

register_env(env_name, env_config)
```

This registers the environment with ray. For more details look into ray project's documentation.
