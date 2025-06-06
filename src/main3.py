import os
import io
import sys
import json
import time
import subprocess as sp
from pathlib import Path

from xra.central_config import dfcc
from xra.log_utilz.log_man import current_logger as log


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
def main():
    print("\n\n")
    files = [f for f in Path(dfcc.repo_root).rglob('*.py[ocd]')]
    for f in files:
        print(f)

    # ---
    print("\n\n")


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
if '__main__' == __name__:
    main()
