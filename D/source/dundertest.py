__test__ = {
    'summing': """
>>> sum([])
0
>>> sum([1,2,3,4,5])
15
""",'removal':"""
>>> [1,2,3].remove(55)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
"""
}
