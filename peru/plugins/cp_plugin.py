#! /usr/bin/env python3

import distutils.dir_util
import sys


def main():
    sys.argv.pop(0)  # exe name
    assert sys.argv.pop(0) == "--cache"
    sys.argv.pop(0)  # cache_path
    assert sys.argv.pop(0) == "fetch"
    dest = sys.argv.pop(0)

    path = None

    while sys.argv:
        name = sys.argv.pop(0)
        val = sys.argv.pop(0)
        if name == "--path":
            path = val
        else:
            raise RuntimeError("Unknown plugin field name: " + name)

    assert path is not None

    distutils.dir_util.copy_tree(path, dest, preserve_symlinks=True)


if __name__ == "__main__":
    main()