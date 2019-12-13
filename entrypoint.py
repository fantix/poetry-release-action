#!/usr/bin/env python

import json
import os

from git import Repo

with open(os.environ["GITHUB_EVENT_PATH"]) as f:
    payload = json.load(f)

repo = Repo()
print("Repo: ", repo)
print("Payload: ", payload)
