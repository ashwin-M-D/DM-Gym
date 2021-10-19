# DM-Gym: Working with environments

After the creation of the environment as explained before, we can now start to use it.

The environment moves as shown below

```python
## Given environment object env

#first reset the environment to get your first observation
obs = env.reset()

loop('''while done = False'''):
    ## Compute action here
    #action = RL(obs)
    ## RL computation done

    # Step through the environment
    obs, reward, done, info = env.step(action)
```

The returned values are explained below:

1. obs: This is just the next observation which is fed into the RL model
2. reward: This is a measure as to how well the previous action was for that previous state
3. done: The environment has reached a terminal state now.
4. info: is a dictionary but is usually empty. It is mainly used for debugging purposes.

Once done changes from false to true, you can reset the environment as shown above and continue the training process.