#!/bin/bash
# Program:
#    This program execute commands that pull last update from github.

git pull origin source  # update the local source branch
cd ./_deploy
git pull origin master  # update the local master branch
