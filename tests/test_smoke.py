from shardcraft import planner


def test_import():
    assert planner.Config().seed == 0
