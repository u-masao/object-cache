
=====================
object_cache
=====================

description
============

This module caches the processing result of the function in the storage, and if the cache hits, skips the processing in the function and returns the result. Create ".object_cache" in the current path and cache it.

install
========

.. code-block:: shell
    pip install object-cache

clear cache
============
.. code-block:: shell
    rm -fr .object_cache

code example
============

.. code-block:: python
    import time

    from object_cache import object_cache


    @object_cache
    def factorial(a):
        result = 1
        for i in range(2, a + 1):
            result *= i

        return result


    for _ in range(5):
        start = time.time()
        factorial(100000)
        print("elapsed time", time.time() - start)

