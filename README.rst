
At API
======

Explicitly declare the public API of your Python package using ``@api`` decorators, and auto-generate an ``__init__.py`` file that imports the public API into the top-level namespace.

Usage
-----


#. Install ``atapi`` (using Poetry or ``python setup.py install``\ ).
#. Add ``# BEGIN ATAPI`` and ``# END ATAPI`` comments to your ``__init__.py`` file, indicating where you would like ``atapi`` to put generated code. Anything between those lines will be replaced by the tool.
#. Change directory to the parent of your package (i.e. if you just edited ``foo/bar/__init__.py``\ , make sure the current working directory is ``foo/``\ ).
#. Run ``atapi``\ , passing the name of your package (i.e. in the above example, ``atapi bar``.
