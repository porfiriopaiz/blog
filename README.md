# Nikola Static Site Generator

These are my notes for setting up a virtual environment for Nikola, the static
site generator that I use to build my blog.

## Reasons for using this guide

This document guides you through the processes of setting up a virtual
environment, this way you can use the lastest version of Nikola, pulling it
fron pypi without worrying about breaking or poluting your system.

- This ensure true portability and reproducible environments.

## Installing `virtualenv` and `pip`

> Fedora

```sh
su -c 'dnf install python2-virtualenv.noarch python3-virtualenv.noarch'
```

```sh
su -c 'dnf install python2-pip.noarch python3-pip.noarch'
```

## Create a directory for virtualenvs

```sh
cd ~/Documents
mkdir virtualenvs
cd virtualenvs
```

## Create a virtualenv for Nikola

Use the `virtualenv-3` or the `virtualenv-3.6` command.

```sh
virtualenv-3 --no-site-packages nikola
```

```sh
cd nikola
```

## Activate the virtualenv

```sh
source bin/activate
```

## Install upgrade the `setuptools` and `pip`

```sh
pip install --upgrade setuptools pip
```

## Install Nikola

```sh
pip install --upgrade "Nikola[extras]"
```

## Clone the github repo

```sh
git clone git@github.com:porfiriopaiz/blog.git
```

## Nikola commands

### Build a site after edit or new post

```sh
nikola build
```

### Create a new post

```sh
nikola new_post -e
```

```sh
nikola serve --browser
```

## Github serving

```sh
git checkout master
git subtree split --prefix output -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages
```
