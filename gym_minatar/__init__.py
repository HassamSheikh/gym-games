from gym.envs.registration import register

for game in ['Asterix', 'Breakout', 'Freeway', 'Seaquest', 'Space_invaders']:
  register(
    id='{}-MinAtar-v0'.format(game),
    entry_point="gym_minatar.envs:{}".format(game)
)
