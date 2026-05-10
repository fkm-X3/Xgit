import argparse
import configparser
from datetime import datetime

try:
    import grp, pwd
except ModuleNotFoundError:
    print("Yo, `XGit doesn't work on windows yet. You can run it through WSL.")
    pass

from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib
# imports are done, more code tommorow
