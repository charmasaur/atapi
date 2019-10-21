"""
A test package for the atapi project.
"""

# BEGIN ATAPI
from test_pkg.mod import Public
from test_pkg.mod import PublicABC
from test_pkg.mod import PublicDataclass
from test_pkg.mod import PublicDataclass2
from test_pkg.mod import PublicWithFunction
from test_pkg.mod import public
from test_pkg.spkg.mod import SpkgModPublic
from test_pkg.spkg.mod import SpkgModPublic
from test_pkg.spkg.mod import spkg_mod_public
from test_pkg.spkg.mod import spkg_mod_public
from test_pkg.spkg.mod2 import spkg_mod2_public
from test_pkg.spkg.mod2 import spkg_mod2_public

__all__ = [
    Public,
    PublicABC,
    PublicDataclass,
    PublicDataclass2,
    PublicWithFunction,
    SpkgModPublic,
    SpkgModPublic,
    public,
    spkg_mod2_public,
    spkg_mod2_public,
    spkg_mod_public,
    spkg_mod_public,
]
# END ATAPI
