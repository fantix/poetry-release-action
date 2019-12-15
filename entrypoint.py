#!/usr/bin/env python

import json
import os
import re
import tempfile

from git import Repo

GOLLUM_TITLE_REGEXP = re.compile(r"Release v([0-9.]+)")


def handle_gollum(payload):
    pages = payload["pages"][0]
    version = GOLLUM_TITLE_REGEXP.findall(pages["title"])
    if not version:
        return

    version = version[0]
    action = pages["action"]
    with tempfile.TemporaryDirectory() as path:
        wiki_msg = (
            Repo.clone_from(payload["repository"]["html_url"] + ".wiki.git", path)
            .commit(pages["sha"])
            .message
        )

    print(version, action, wiki_msg)
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
    if method in globals():
        print("Calling", method)
        print("=" * 80)
        globals()[method](payload)


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
#             "html_url": "https://github.com/fantix/release-demo/wiki/Release-v3.5",
#             "page_name": "Release-v3.5",
#             "sha": "701e110a42b3c0d9ac17d0e46a26035f2fc4b54d",
#             "summary": None,
#             "title": "Release v3.5",
#         }
#     ],
#     "repository": {
#         "archive_url": "https://api.github.com/repos/fantix/release-demo/{archive_format}{/ref}",
#         "archived": False,
#         "assignees_url": "https://api.github.com/repos/fantix/release-demo/assignees{/user}",
#         "blobs_url": "https://api.github.com/repos/fantix/release-demo/git/blobs{/sha}",
#         "branches_url": "https://api.github.com/repos/fantix/release-demo/branches{/branch}",
#         "clone_url": "https://github.com/fantix/release-demo.git",
#         "collaborators_url": "https://api.github.com/repos/fantix/release-demo/collaborators{/collaborator}",
#         "comments_url": "https://api.github.com/repos/fantix/release-demo/comments{/number}",
#         "commits_url": "https://api.github.com/repos/fantix/release-demo/commits{/sha}",
#         "compare_url": "https://api.github.com/repos/fantix/release-demo/compare/{base}...{head}",
#         "contents_url": "https://api.github.com/repos/fantix/release-demo/contents/{+path}",
#         "contributors_url": "https://api.github.com/repos/fantix/release-demo/contributors",
#         "created_at": "2019-12-13T19:26:24Z",
#         "default_branch": "master",
#         "deployments_url": "https://api.github.com/repos/fantix/release-demo/deployments",
#         "description": None,
#         "disabled": False,
#         "downloads_url": "https://api.github.com/repos/fantix/release-demo/downloads",
#         "events_url": "https://api.github.com/repos/fantix/release-demo/events",
#         "fork": False,
#         "forks": 0,
#         "forks_count": 0,
#         "forks_url": "https://api.github.com/repos/fantix/release-demo/forks",
#         "full_name": "fantix/release-demo",
#         "git_commits_url": "https://api.github.com/repos/fantix/release-demo/git/commits{/sha}",
#         "git_refs_url": "https://api.github.com/repos/fantix/release-demo/git/refs{/sha}",
#         "git_tags_url": "https://api.github.com/repos/fantix/release-demo/git/tags{/sha}",
#         "git_url": "git://github.com/fantix/release-demo.git",
#         "has_downloads": True,
#         "has_issues": True,
#         "has_pages": False,
#         "has_projects": True,
#         "has_wiki": True,
#         "homepage": None,
#         "hooks_url": "https://api.github.com/repos/fantix/release-demo/hooks",
#         "html_url": "https://github.com/fantix/release-demo",
#         "id": 227908065,
#         "issue_comment_url": "https://api.github.com/repos/fantix/release-demo/issues/comments{/number}",
#         "issue_events_url": "https://api.github.com/repos/fantix/release-demo/issues/events{/number}",
#         "issues_url": "https://api.github.com/repos/fantix/release-demo/issues{/number}",
#         "keys_url": "https://api.github.com/repos/fantix/release-demo/keys{/key_id}",
#         "labels_url": "https://api.github.com/repos/fantix/release-demo/labels{/name}",
#         "language": None,
#         "languages_url": "https://api.github.com/repos/fantix/release-demo/languages",
#         "license": None,
#         "merges_url": "https://api.github.com/repos/fantix/release-demo/merges",
#         "milestones_url": "https://api.github.com/repos/fantix/release-demo/milestones{/number}",
#         "mirror_url": None,
#         "name": "release-demo",
#         "node_id": "MDEwOlJlcG9zaXRvcnkyMjc5MDgwNjU=",
#         "notifications_url": "https://api.github.com/repos/fantix/release-demo/notifications{?since,all,participating}",
#         "open_issues": 0,
#         "open_issues_count": 0,
#         "owner": {
#             "avatar_url": "https://avatars1.githubusercontent.com/u/1751601?v=4",
#             "events_url": "https://api.github.com/users/fantix/events{/privacy}",
#             "followers_url": "https://api.github.com/users/fantix/followers",
#             "following_url": "https://api.github.com/users/fantix/following{/other_user}",
#             "gists_url": "https://api.github.com/users/fantix/gists{/gist_id}",
#             "gravatar_id": "",
#             "html_url": "https://github.com/fantix",
#             "id": 1751601,
#             "login": "fantix",
#             "node_id": "MDQ6VXNlcjE3NTE2MDE=",
#             "organizations_url": "https://api.github.com/users/fantix/orgs",
#             "received_events_url": "https://api.github.com/users/fantix/received_events",
#             "repos_url": "https://api.github.com/users/fantix/repos",
#             "site_admin": False,
#             "starred_url": "https://api.github.com/users/fantix/starred{/owner}{/repo}",
#             "subscriptions_url": "https://api.github.com/users/fantix/subscriptions",
#             "type": "User",
#             "url": "https://api.github.com/users/fantix",
#         },
#         "private": False,
#         "pulls_url": "https://api.github.com/repos/fantix/release-demo/pulls{/number}",
#         "pushed_at": "2019-12-13T19:27:57Z",
#         "releases_url": "https://api.github.com/repos/fantix/release-demo/releases{/id}",
#         "size": 0,
#         "ssh_url": "git@github.com:fantix/release-demo.git",
#         "stargazers_count": 0,
#         "stargazers_url": "https://api.github.com/repos/fantix/release-demo/stargazers",
#         "statuses_url": "https://api.github.com/repos/fantix/release-demo/statuses/{sha}",
#         "subscribers_url": "https://api.github.com/repos/fantix/release-demo/subscribers",
#         "subscription_url": "https://api.github.com/repos/fantix/release-demo/subscription",
#         "svn_url": "https://github.com/fantix/release-demo",
#         "tags_url": "https://api.github.com/repos/fantix/release-demo/tags",
#         "teams_url": "https://api.github.com/repos/fantix/release-demo/teams",
#         "trees_url": "https://api.github.com/repos/fantix/release-demo/git/trees{/sha}",
#         "updated_at": "2019-12-13T19:27:59Z",
#         "url": "https://api.github.com/repos/fantix/release-demo",
#         "watchers": 0,
#         "watchers_count": 0,
#     },
#     "sender": {
#         "avatar_url": "https://avatars1.githubusercontent.com/u/1751601?v=4",
#         "events_url": "https://api.github.com/users/fantix/events{/privacy}",
#         "followers_url": "https://api.github.com/users/fantix/followers",
#         "following_url": "https://api.github.com/users/fantix/following{/other_user}",
#         "gists_url": "https://api.github.com/users/fantix/gists{/gist_id}",
#         "gravatar_id": "",
#         "html_url": "https://github.com/fantix",
#         "id": 1751601,
#         "login": "fantix",
#         "node_id": "MDQ6VXNlcjE3NTE2MDE=",
#         "organizations_url": "https://api.github.com/users/fantix/orgs",
#         "received_events_url": "https://api.github.com/users/fantix/received_events",
#         "repos_url": "https://api.github.com/users/fantix/repos",
#         "site_admin": False,
#         "starred_url": "https://api.github.com/users/fantix/starred{/owner}{/repo}",
#         "subscriptions_url": "https://api.github.com/users/fantix/subscriptions",
#         "type": "User",
#         "url": "https://api.github.com/users/fantix",
#     },
# }

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
