from fabric.api import run, sudo, env, settings

def create_www():
    with settings(sudo_user='http'):
        sudo("mkdir -p /tmp/www")
        sudo("mkdir -p /tmp/www/root")

def create_cache():
    sudo("mkdir -p /tmp/cache", user="mysql")
