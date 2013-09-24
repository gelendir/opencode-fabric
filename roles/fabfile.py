from fabric.api import run, env, roles


env.roledefs.update({
    'db':  ['gregory@localhost'],
    'web': ['gregory@localhost'],
})


@roles('db')
def restart_db():
    run('sudo systemctl restart postgresql')


@roles('web')
def restart_www():
    run('sudo systemctl restart httpd')
