from gym.envs.registration import register

register(
    id='soldiers-v0',
    entry_point='gym_soldiers.envs:SoldiersEnv',
)
