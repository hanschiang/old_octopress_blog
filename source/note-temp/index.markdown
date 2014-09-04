---
layout: page
title: "note-temp"
date: 2014-09-04 22:29
comments: true
sharing: true
footer: true
---

### 參考文章：

1. [Setup Ruby On Rails on Ubuntu 14.04 Trusty Tahr](https://gorails.com/setup/ubuntu/14.04)
2. [Blogging Basics (Octopress)](http://octopress.org/docs/blogging/)
3. [Sharing Code Snippets](http://octopress.org/docs/blogging/code/)
4. [Markdown Basics](https://help.github.com/articles/markdown-basics)
5. [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
6. [Add a Page to Top Menu](http://asaf.github.io/blog/2013/07/08/blogging-with-octopress-add-about-page/)

# Ruby on Rails 安裝與設定於 Ubuntu 14.04

- 安裝 ruby 相關套件（install some dependencies for Ruby.）

```
sudo apt-get update
sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties
```

- 以下的套件待弄清楚用途：

```
git-core
curl
zlib1g-dev
build-essential
libssl-dev
libreadline-dev
libyaml-dev
libsqlite3-dev
sqlite3
libxml2-dev
libxslt1-dev
libcurl4-openssl-dev
python-software-properties
```


- 安裝Ruby（Install Ruby by: rbenv or rvm or source）

這次 Ubuntu 14.04 裝 rbenv，兩個步驟：安裝 rbenv 和 ruby-build 。

```
cd
git clone git://github.com/sstephenson/rbenv.git .rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL

git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
exec $SHELL

rbenv install 2.1.2
rbenv global 2.1.2
ruby -v
```


- Configuring Git

```
git config --global color.ui true
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR@EMAIL.com"
ssh-keygen -t rsa -C "YOUR@EMAIL.com"
```



- prax

https://github.com/ysbaddaden/prax


- 監視 development.log

```
tail -f log/development.log
```
