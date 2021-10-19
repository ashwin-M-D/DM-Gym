# Classification Environments

## classification-v0

### Environment config

The environment config looks like so:

```python
env_name = "classification-v0"

env_config = {
    'data': data,
    'target': target,
    'num_classes': k,
}
```

The parameters are self explanatory.

### Environment Variables

The major environment variables are the following

```python
## env is the environment object

env.reward_range
# returns a touple which is the range in which the reward can exist for each step
# in this case (-1,1)

env.state_space
env.action_space
# Action space here is a Diecrete spaces object with num_classes.

## To understand more about the spaces object, read the openAI gym documentation
```

### Reward Function

The reward function is quite simply defined as follows:

Reward = 1 if expected_class = predicted_class
Reward = -1 otherwise

Because of such a reward structure, it is recommended to use a low value for gamma such as 0.4 instead of the usual default values such as 0.99 or 0.999