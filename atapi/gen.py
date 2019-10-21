"""
Generates __init__ files from atapi annotations.
"""

import pkgutil

import atapi


def _generate_init_lines(pkg_name):
    """
    Generates text lines for the __init__.py file of the given package.

    Specifically, identifies the public API of the given package (as specified by ``atapi.api``
    annotations), and generates text lines that import the public functions/classes and list them
    in the package's ``__all__`` attribute.
    """
    # Override the api decorator to store API functions/classes. Use a set to eliminate duplicates,
    # since we may end up loading the same module multiple times while walking the package tree.
    funcs = set()
    def api_inner(func):
        # Only add top-level functions/classes.
        if func.__qualname__ == func.__name__:
            funcs.add((func.__module__, func.__name__))
        return func
    atapi.api = api_inner

    # Recursively load modules under the appropriate package name. This will fill out the `funcs`
    # list.
    for module_info in pkgutil.walk_packages([pkg_name], prefix=pkg_name + "."):
        if module_info.ispkg:
            continue
        module_info.module_finder.find_module(module_info.name).load_module()

    import_lines = []
    for func_module, func_name in funcs:
        import_lines.append("from {0} import {1}".format(func_module, func_name))
    import_lines.sort()

    all_lines = []
    for _, func_name in funcs:
        all_lines.append("    {0},".format(func_name))
    all_lines.sort()

    return import_lines + ["", "__all__ = ["] + all_lines + ["]"]


def main():
    import argparse
    import os
    import sys

    parser = argparse.ArgumentParser(description="Generate __init__ file from atapi annotations..")
    parser.add_argument('pkg_name',
                        type=str,
                        help=("The package name for which to generate the __init__ file. Expected "
                              "be the name of a sub-directory of the current working directory."))
    args = parser.parse_args()

    pkg_name = args.pkg_name
    print("Looking for package {0}".format(pkg_name))
    if not os.path.isdir(pkg_name):
        print("{0} is not a sub-directory of the current working directory".format(pkg_name))
        sys.exit(1)

    init_fn = "./{0}/__init__.py".format(pkg_name)
    print("Looking for {0}".format(init_fn))
    if not os.path.exists(init_fn):
        print("No __init__.py file found, creating one")

        with open(init_fn, "w") as f:
            print("# BEGIN ATAPI", file=f)
            print("# END ATAPI", file=f)

    print("Checking validity of __init__ file")
    with open(init_fn, "r") as f:
        lines = list(f)
    begin_lines = [i for i, line in enumerate(lines) if line.rstrip() == "# BEGIN ATAPI"]
    end_lines = [i for i, line in enumerate(lines) if line.rstrip() == "# END ATAPI"]
    if len(begin_lines) is not 1:
        print("__init__.py must contain exactly one line of the form \"# BEGIN ATAPI\"")
        sys.exit(1)
    if len(end_lines) is not 1:
        print("__init__.py must contain exactly one line of the form \"# END ATAPI\"")
        sys.exit(1)
    if begin_lines[0] >= end_lines[0]:
        print("__init__.py's \"# BEGIN ATAPI\" line must occur before its \"# END ATAPI\" line")
        sys.exit(1)

    print("Generating new __init__ file")
    new_lines = (lines[:begin_lines[0]+1]
                 + ["\n".join(_generate_init_lines(pkg_name)), "\n"]
                 + lines[end_lines[0]:])

    print("Overwriting {0}".format(init_fn))
    with open(init_fn, "w") as f:
        for line in new_lines:
            f.write(line)
