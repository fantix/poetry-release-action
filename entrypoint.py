#!/usr/bin/env python

import json
import os
import re

from git import Repo

GOLLUM_TITLE_REGEXP = re.compile(r"Release v([0-9.]+)")


def handle_gollum(payload):
    payload = payload["pages"][0]
    version = GOLLUM_TITLE_REGEXP.findall(payload["title"])
    if not version:
        return

    version = version[0]
    action = payload["action"]
    summary = payload["summary"]
    print(version, action, summary)
    repo = Repo()
    print("Repo: ", repo)


def main():
    print("Environ: ", os.environ)
    # noinspection PyBroadException
    try:
        with open(os.environ["GITHUB_EVENT_PATH"]) as f:
            payload = json.load(f)
        print("Payload: ", payload)
    except Exception:
        print("No payload.")
        payload = None
    method = "handle_" + os.environ["GITHUB_EVENT_NAME"]
    if method in locals():
        print("Calling", method)
        print("=" * 80)
        locals()[method](payload)


if __name__ == "__main__":
    main()

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

# Payload = {
#     "pages": [
#         {
#             "action": "edited",
#             "html_url": "https://github.com/fantix/release-demo/wiki/Home",
#             "page_name": "Home",
#             "sha": "401b12d450b72c7f80ef485f204b5034c92facbf",
#             "summary": None,
#             "title": "Home",
#         }
#     ],
# }

Payload = {
    "pages": [
        {
            "action": "edited",
            "html_url": "https://github.com/fantix/release-demo/wiki/Home-v1.0",
            "page_name": "Home-v1.0",
            "sha": "22611fdc0591f86edf4e16443f5f8c2d4e21a423",
            "summary": None,
            "title": "Home v1.0",
        }
    ]
}

# environ = {
#     "PATH": "/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
#     "HOSTNAME": "76a8540f02a6",
#     "RUNNER_OS": "Linux",
#     "RUNNER_TOOL_CACHE": "/opt/hostedtoolcache",
#     "HOME": "/github/home",
#     "GITHUB_REF": "refs/heads/master",
#     "GITHUB_SHA": "9ddfe806487e0694ce2254e9d8914b11a2ccdadf",
#     "GITHUB_ACTOR": "fantix",
#     "GITHUB_EVENT_NAME": "gollum",
#     "GITHUB_WORKSPACE": "/github/workspace",
#     "RUNNER_WORKSPACE": "/home/runner/work/release-demo",
#     "GITHUB_BASE_REF": "",
#     "GITHUB_EVENT_PATH": "/github/workflow/event.json",
#     "ACTIONS_RUNTIME_URL": "https://pipelines.actions.githubusercontent.com/auZVI6o4fqDx3D493TF8dwQCeBXTa6kdPd510edr3nBmurxbdd/",
#     "GITHUB_WORKFLOW": "Release CI",
#     "GITHUB_HEAD_REF": "",
#     "GITHUB_ACTION": "fantixpoetry-release-action",
#     "RUNNER_TEMP": "/home/runner/work/_temp",
#     "GITHUB_ACTIONS": "true",
#     "INPUT_WHO-TO-GREET": "World",
#     "GITHUB_REPOSITORY": "fantix/release-demo",
#     "ACTIONS_RUNTIME_TOKEN": "***",
#     "LANG": "C.UTF-8",
#     "GPG_KEY": "0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D",
#     "PYTHON_VERSION": "3.7.5",
#     "PYTHON_PIP_VERSION": "19.3.1",
#     "PYTHON_GET_PIP_URL": "https://github.com/pypa/get-pip/raw/ffe826207a010164265d9cc807978e3604d18ca0/get-pip.py",
#     "PYTHON_GET_PIP_SHA256": "b86f36cc4345ae87bfd4f10ef6b2dbfa7a872fbff70608a1e43944d283fd0eee",
# }
