import Halfadder


def test_case1():
    ret = Halfadder.getHalfadder(0, 0)
    assert ret == (0, 0)


def test_case2():
    ret = Halfadder.getHalfadder(0, 1)
    assert ret == (0, 1)


def test_case3():
    ret = Halfadder.getHalfadder(1, 0)
    assert ret == (0, 1)


def test_case4():
    ret = Halfadder.getHalfadder(1, 1)
    assert ret == (1, 0)
