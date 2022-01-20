from calc import add


def test_add_3_and_2_gives_5():
    actual = add(3, 2)

    assert actual == 5


def test_add_3_and_3_gives_6():
    actual = add(3, 3)

    assert actual == 6
