from collections.abc import Hashable

lst = set([1, 2, 5, 89, 'pop', "123"])
_set = lambda lst: [item for item in lst if isinstance(item, Hashable)]

print(_set)
