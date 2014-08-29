#!/usr/bin/python

import subprocess
subprocess.call(["git", "pull", "origin", "source"])
subprocess.STDOUT(["cd", "_deploy"])
subprocess.call(["git", "pull", "origin", "master"])
