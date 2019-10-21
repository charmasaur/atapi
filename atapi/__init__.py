"""
atapi package

Automatically generates __init__ files exposing a public API.
"""

def api(func):
    """
    Indicates that a function or class is part of the public API of the package.

    Should only be used on top-level functions and classes, since a method or nested function/class
    is considered public iff the containing function/class is public.
    """
    return func
