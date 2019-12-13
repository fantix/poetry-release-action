#!/usr/bin/env python

import json
import os

from git import Repo

with open(os.environ["GITHUB_EVENT_PATH"]) as f:
    payload = json.load(f)

repo = Repo()
print("Repo: ", repo)
print("Payload: ", payload)
print("Environ: ", os.environ)

# payload = {
#     "pages": [
#         {
#             "action": "created",
#             "html_url": "https://github.com/fantix/release-demo/wiki/Home",
#             "page_name": "Home",
#             "sha": "16edb380041ef742db82b6bf1beae4defeea083a",
#             "summary": None,
#             "title": "Home",
#         }
#     ],
# }
