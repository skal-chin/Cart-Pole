import gym
import numpy as np

'''
--- Cart and Pole ---

Observations
------------------
Index -> Observations
    0 -> Cart Postion
    1 -> Cart Velocity
    2 -> Pole Angle
    3 -> Pole Angular Velocity

Actions
------------------
Number -> Action
    0 -> Negative Force 1
    1 -> Positive Force 1

Episode Terminates at:
    Pole angle is more then +-12 degrees
    Cart position is +- 2.4
    The episode step reaches 200.


choose_action
----------------
    Parameters
    -----------
        pole_angle -> the current state's pole angle
        cart_vel   -> the current state's cart velocity

    Variables
    -----------
        right_velocity_limit -> the cart velocity limit we are
                restricting in the positive x direction.

        left_velocity_limit -> the cart velocity limit we are
                restricting in the negative x direction

    Returns
    ----------
        1 -> if the pole_angle is greater than 0 or cart_vel less
                than the left_velocity_limit

        0 -> if pole_angle is less than 0 or cart_vel is greater than
                right_velocity_limit
'''
def choose_action(obs):
    cart_pos = obs[0]
    cart_vel = obs[1]
    pole_angle = obs[2]
    pole_angular_vel = obs[3]

    right_velocity_limit = .8
    left_velocity_limit = -right_velocity_limit

    if pole_angle > 0 or cart_vel < left_velocity_limit:
        return 1
    elif pole_angle < 0 or cart_vel > right_velocity_limit:
        return 0


'''
main()
--------------------
    Variables
    ----------
    env -> The Cart and Pole environment
    obs -> The observations of the env, which is reset after
            every episode
    episodes -> the number of times the experiment is repeated
    results  -> holds the number of steps that each episode runs
            through. An average is taken from this. 195 over
            100 episodes considers the problem solved.
    steps -> counts the steps before the episode is terminated
    action -> the chosen action that is returned from choose_action
    done -> Returns true if any of the terminating conditions happen

'''
def main():
    env = gym.make('CartPole-v0')       # creates the environment
    obs = env.reset()
    episodes = 10                       # number of episodes
    results = []                        # collects each episodes step result
                                        # the goal is 195 over 100 episodes
    for e in range(episodes):           # episode loop
        obs = env.reset()
        steps = 0
        for t in range(201):          # step loop
            env.render()
            action = choose_action(obs)      # finds an action based on current state
            obs, reward, done, info = env.step(action)  # creates new state based on action
            steps += 1
            # print(f'Observations: {obs}')
            if done:
                results.append(steps)
                print(f'Finished State: {obs}')
                print(f'Steps: {steps}')
                break

    env.close()

    print(f'Average Success over {episodes} episodes:')
    print(np.average(results))


if __name__ == '__main__':
    main()
