"""
Test module.
"""

from abc import ABC
from dataclasses import dataclass

from atapi import api

@api
def public():
    """
    Public function.
    """

def private():
    """
    Private function.
    """

@api
class Public():
    """
    Public class.
    """

class Private():
    """
    Private class.
    """

@api
@dataclass
class PublicDataclass():
    """
    Public dataclass.
    """
    value: int

@dataclass
@api
class PublicDataclass2():
    """
    Public dataclass with decorators switched.
    """
    value: int

@api
class PublicABC(ABC):
    """
    Public abstract base class.
    """

@api
class PublicWithFunction():
    """
    Public class with api-annotated method.
    """
    @api
    def method(self):
        """
        Public method.
        """

