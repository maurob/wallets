def iterlen(generator_function):
    class IterableWithLen:
        def __iter__(self):
            return generator_function()

        def __len__(self):
            return sum(1 for _ in self)

    return IterableWithLen()


def listify(generator_function):
    return list(generator_function())
