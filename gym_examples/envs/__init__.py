from ..register import register


register(
    id="barkour",
    entry_point="gym_custom_examples.envs.custom_world:CustomTerrainAntEnv",
    max_episode_steps=1000,
    reward_threshold=6000.0,
    xml="custom_terrain_ant.xml",
)
