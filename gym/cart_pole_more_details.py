import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print('observation={0}'.format(observation))
        print('action={0}'.format(action))
        print('reward={0}'.format(reward))
        print('done={0}\n'.format(done))
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
'''
observation=[ 0.04262979 -0.18194424 -0.13940168 -0.35241294]
action=1
reward=1.0
done=False

observation=[ 0.0389909  -0.3748371  -0.14644994 -0.10673193]
action=0
reward=1.0
done=False

observation=[ 0.03149416 -0.56758993 -0.14858458  0.13639976]
action=0
reward=1.0
done=False

observation=[ 0.02014236 -0.37068671 -0.14585658 -0.19922403]
action=1
reward=1.0
done=False
'''


'''
https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
check source code for details below
* observation: state, is x, x_dot, theta, theta_dot
* action: force = self.force_mag if action==1 else -self.force_mag, action is 0/1
* reward: if not done: reward = 1.0, else reward=0
the goal is always to increase your total reward
'''
