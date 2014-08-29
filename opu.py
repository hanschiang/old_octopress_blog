#!/usr/bin/python

import subprocess
subprocess.call(["rake", "generate"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-am", "'New post.'"])
subprocess.call(["git", "push", "origin", "source"])
subprocess.call(["rake", "deploy"])
