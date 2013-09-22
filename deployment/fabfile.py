from fabric.api import run, settings, cd

DEPLOY_PATH = '/tmp/opencode-fabric'


def deploy():
    check_deployment()
    update()


def check_deployment():
    with settings(warn_only=True):
        command = run("test -d %s" % DEPLOY_PATH)
        if command.failed:
            run("git clone git://github.com/gelendir/opencode-fabric %s" % DEPLOY_PATH)


def update():
    with cd(DEPLOY_PATH):
        run("git pull")
