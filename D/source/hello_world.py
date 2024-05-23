"""
This is the example hello_world.py

This example shows how to use the hello() function.

>>> hello("My name is Daniel!")
'My name is Daniel!'
"""

def hello(a_string):
    """
    This is the docstring of the hello() function!

    >>> hello("My name is Daniel!")
    'My name is Daniel!'
    """
    return f"My name is Daniel!"

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
