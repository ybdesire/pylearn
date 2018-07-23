import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
    print('action={0}'.format(env.action_space.sample()))
'''
action=1
action=0
action=0
action=0
action=1
action=0
action=1
action=1
action=0
action=0
action=1
action=0
action=1
action=0
action=1
'''