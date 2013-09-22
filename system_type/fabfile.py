from fabric.api import run

def system_type():
    run('uname -s')
