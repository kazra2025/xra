import os
import subprocess as sp
from pathlib import Path

# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
_API_PORT = 174_80
_API_HOST = "127.0.0.1"
_REPO_ROOT_PATH = Path(sp.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()).resolve()


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
class CentralConfig:
    """ Central configuration for the library. """

    def __init__(self):
        self.api_port: int = _API_PORT
        self.api_host: str = _API_HOST

        self.repo_root_path: Path = _REPO_ROOT_PATH
        self.repo_root: str = str(_REPO_ROOT_PATH)

        # implement any env variable overrides here
        self.dbg_mode: bool = True


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# create default cc lazily at import.
dfcc = CentralConfig()
