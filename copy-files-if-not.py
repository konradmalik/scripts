#!/usr/bin/env python3

"""
Copy files from dir A to dir B, but only if not already in C

"""

import os
import shutil
import sys
from pathlib import Path

LEAF_FOLDER = 'D P&ID'


def listfiles(rootdir):
    dirs = set()

    def f(start):
        for path in Path(start).iterdir():
            if path.is_dir():
                f(path)
            elif path.is_file():
                if path.parent.name == LEAF_FOLDER:
                    dirs.add(str(path.relative_to(rootdir)))
    f(rootdir)
    return dirs


if __name__ == '__main__':
    source_folder = Path(sys.argv[1])
    target_folder = Path(sys.argv[2])
    filter_folder = Path(sys.argv[3])

    not_in = listfiles(filter_folder)

    for file in listfiles(source_folder):
        if file not in not_in:
            target_file = target_folder/file
            # make sure dir exists
            os.makedirs(target_file.parent, exist_ok=True)
            shutil.copy(src=source_folder/file,
                        dst=target_file)
