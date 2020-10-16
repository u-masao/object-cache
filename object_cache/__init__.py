import os
from pickle import PickleError
import hashlib
import inspect

import cloudpickle


disable_cache = False
enable_print = False


def _pickle_bytes(obj):
    """ get cloudpickle bytes value """
    return cloudpickle.dumps(obj)


def _object_hash(*objs):
    """ get hash """
    masher = hashlib.new("sha256")
    for obj in objs:
        masher.update(_pickle_bytes(obj))
    return masher.hexdigest()


def object_cache(func):
    """
    cashe decorator
    """

    def wrapper(*args, **kwargs):

        if disable_cache:
            if enable_print:
                print("Cache disabled. {}()".format(func.__name__))
            return func(*args, **kwargs)

        # definition cache file
        cache_dir = ".object_cache"
        digest = _object_hash(
            str(func.__name__),
            str(inspect.getmodule(func)),
            str(inspect.getsource(func)),
            args,
            kwargs,
        )
        file_name = "cache_{}.cloudpickle".format(digest)
        file_path = os.path.join(cache_dir, file_name)

        try:
            # check cache
            os.makedirs(cache_dir, exist_ok=True)
            return_value = cloudpickle.load(open(file_path, "rb"))
            if enable_print:
                print("Cache hit. {}()".format(func.__name__))
        except (OSError, PickleError, ValueError):
            # exec func
            if enable_print:
                print("Cache miss. {}()".format(func.__name__))
            return_value = func(*args, **kwargs)
            # save result
            with open(file_path, "wb") as fo:
                cloudpickle.dump(return_value, fo)
        return return_value

    return wrapper
