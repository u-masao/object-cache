from object_cache import object_cache
import object_cache as oc


@object_cache
def add(a, b):
    return a + b


def test_cache_hit():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(1, 2) == 3


def test_enable_print():
    oc.enable_print = True
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(1, 2) == 3


def test_disable():
    oc.disable_cache = True
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(1, 2) == 3


