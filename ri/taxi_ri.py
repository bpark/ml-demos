import gym
from time import sleep
from IPython.display import clear_output

# Creating thr env
env = gym.make("Taxi-v2").env

env.s = 328

print(env.P[328])

# {0: [(1.0, 428, -1, False)],
# 1: [(1.0, 228, -1, False)],
# 2: [(1.0, 348, -1, False)],
# 3: [(1.0, 328, -1, False)],
# 4: [(1.0, 328, -10, False)],
# 5: [(1.0, 328, -10, False)]}

# Setting the number of iterations, penalties and reward to zero,
epochs = 0
penalties, reward = 0, 0

frames = []

done = False

while not done:
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

    if reward == -10:
        penalties += 1

    # Put each rendered frame into the dictionary for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': state,
        'action': action,
        'reward': reward
    }
    )

    epochs += 1

print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))


# Printing all the possible actions, states, rewards.
def render_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)


render_frames(frames)
