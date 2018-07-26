import gym
env = gym.make('MountainCar-v0')

print(env.action_space, env.action_space.n, ) # 查看这个环境中可用的 action 有多少个
print(env.observation_space)    # 查看这个环境中可用的 state 的 observation 有多少个
print(env.observation_space.high)   # 查看 observation 最高取值
print(env.observation_space.low)    # 查看 observation 最低取值
print(env.reward_range)
import pdb;pdb.set_trace()
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
(Discrete(3), 3)
Box(2L,)
[ 0.60000002  0.07      ]
[-1.20000005 -0.07      ]
(-inf, inf)


observation=[-0.57890163 -0.00436885]
action=0
reward=-1.0
done=False

observation=[-0.58185761 -0.00295598]
action=2
reward=-1.0
done=False

observation=[-0.58537887 -0.00352126]
action=0
reward=-1.0
done=False

observation=[-0.58943943 -0.00406056]
action=0
reward=-1.0
done=False
'''


'''
env source code: https://github.com/openai/gym/blob/master/gym/envs/classic_control/mountain_car.py
* observation = (position, velocity)
* reward = -1.0
* done = bool(position >= self.goal_position)
* action: velocity += (action-1)*0.001 + math.cos(3*position)*(-0.0025)
the goal is always to increase your total reward
'''