from atapi import api

@api
def spkg_mod_public():
    """
    Public function in sub-package.
    """

def spkg_mod_private():
    """
    Private function in sub-package.
    """

@api
class SpkgModPublic():
    """
    Public class in sub-package.
    """

class SpkgModPrivate():
    """
    Private class in sub-package.
    """
