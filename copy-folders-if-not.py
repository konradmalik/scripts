#!/usr/bin/env python3

"""
Copy folders from dir A to dir B, but only if not already in C

"""

import os
import shutil
import sys
from pathlib import Path


def folders_in(path):
    dirs = os.listdir(path)
    return set(dirs)


if __name__ == '__main__':
    source_folder = Path(sys.argv[1])
    target_folder = Path(sys.argv[2])
    filter_folder = Path(sys.argv[3])

    not_in = folders_in(filter_folder)

    for folder in folders_in(source_folder):
        if folder not in not_in:
            shutil.copytree(src=source_folder / folder,
                            dst=target_folder / folder)
