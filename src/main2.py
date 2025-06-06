import os
import io
import sys
import json
import time
import random
import hashlib
import gc
import traceback
import subprocess as sp
from pathlib import Path
import shutil

from xra.central_config import dfcc
from xra.log_utilz.log_man import current_logger as log


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
def main():
    print("\n\n")
    log.info(f"repo_root: {dfcc.repo_root}")
    time.sleep(3)
    log.info(f"repo_root: {dfcc.repo_root}")
    print("\n\n")


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
if '__main__' == __name__:
    main()
