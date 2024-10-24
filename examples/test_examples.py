def test_equal(asserts):
    asserts.assert_equal(1, 1)


def test_not_equal(asserts):
    asserts.assert_not_equal(1, 2)


def test_assert_is(asserts):
    asserts.assert_is(1, 1)
