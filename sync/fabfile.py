from fabric.api import *

DEFAULT_PATH = '/home/gregory/opencode'
DEPLOY_BRANCH = 'deploy'


def sync(path=DEFAULT_PATH):
    add(path)
    commit(path)
    push(path)


def add(path=DEFAULT_PATH):
    with cd(path):
        local('git add -i')


def commit(path=DEFAULT_PATH):
    with cd(path):
        local('git commit -v')


def push(path=DEFAULT_PATH):
    with cd(path):
        local('git push origin master:%s' % DEPLOY_BRANCH)
