#!/bin/bash
# Program:
#    This program execute:
#                         1. octopress post generation
#                         2. push files to github
#                         3. new post deploy

rake generate
git add .
git commit -am "Post update" 
git push origin source  # update the remote source branch 
rake deploy             # update the remote master branch
