import git
import datetime
import os
from time import *
from os import path
from git import Repo

# self.rorepo.working_tree_dir equals /Users/mtrier/Development/git-python
repo = Repo(self.rorepo.working_tree_dir)
assert not repo.bare
