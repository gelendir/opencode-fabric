from fabric.api import *

DEFAULT_PATH = '/home/gregory/opencode/tmp/testrepo'
DEPLOY_BRANCH = 'deploy'


def sync(path=DEFAULT_PATH):
    add(path)
    commit(path)
    push(path)


def add(path=DEFAULT_PATH):
    with lcd(path):
        local('pwd')
        local('git add -i')


def commit(path=DEFAULT_PATH):
    with lcd(path):
        local('git commit -v')


def push(path=DEFAULT_PATH):
    with lcd(path):
        local('git push origin master:%s' % DEPLOY_BRANCH)
