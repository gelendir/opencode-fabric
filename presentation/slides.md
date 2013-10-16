title: Fabric
name: inverse
layout: true
class: center, middle, inverse
---

#Fabric

Lord Junior 6th
Gregory Eric Sanderson Turcot Temlett MacDonnell of Glengary Forbes of Linden

---
layout: false

What is fabric ?
===============

 * http://docs.fabfile.org
 * SSH lib in python
 * Automation of sysadmin tasks

---

What about chef or puppet ?
===========================

 * Similar goals
 * Different approach
 * Chef/Puppet are full-fledged frameworks
 * Fabric feels more like a micro-framework
 * I <3 python

---

Hello world
===========

fabfile.py

    def hello():
        print("Hello world!")

running the code:

    $ fab hello
    Hello world!

    Done.

---

Multiple tasks
==============

fabfile.py

    def hello():
        print("Hello world!")

    def world():
        print("World, Hello!")

running the code:

    $ fab hello
    Hello world!

    Done.


    $ fab world
    World, hello!

    Done.

---

What system am I running ?
=========================

fabfile.py

    from fabric.api import run

    def system_type():
        run('unname -s')

running the code:

    $ fab -H localhost system_type
    [localhost] Executing task 'system_type'
    [localhost] run: uname -s
    [localhost] Login password for 'gregory': 
    [localhost] out: Linux
    [localhost] out: 


    Done.
    Disconnecting from localhost... done.

---

Git workflow
============

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
            local('git push origin %s' % DEPLOY_BRANCH)

---

Git workflow
============

running the code:

    $ fab sync
    [localhost] local: git add -i
    [localhost] local: git commit -v
    [master 001e95a] add hello world
     1 file changed, 5 insertions(+)
     create mode 100644 hello/fabfile.py
    [localhost] local: git push origin master:deploy
    Warning: Permanently added the RSA host key for IP address '192.30.252.130' to the list of known hosts.
    Counting objects: 5, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (4/4), 394 bytes | 0 bytes/s, done.
    Total 4 (delta 0), reused 0 (delta 0)
    To git@github.com:gelendir/opencode-fabric.git
       3cc8181..001e95a  master -> deploy

    Done.

---

Deployment
==========

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

---

Deployment
==========

running the code:

    $ fab -H localhost deploy
    [localhost] Executing task 'deploy'
    [localhost] run: test -d /tmp/opencode-fabric
    [localhost] Login password for 'gregory': 

    Warning: run() received nonzero return code 1 while executing 'test -d /tmp/opencode-fabric'!

    [localhost] run: git clone git://github.com/gelendir/opencode-fabric /tmp/opencode-fabric
    [localhost] out: Cloning into '/tmp/opencode-fabric'...
    [localhost] out: remote: Counting objects: 10, done.
    [localhost] out: remote: Compressing objects: 100% (6/6), done.
    [localhost] out: remote: Total 10 (delta 0), reused 10 (delta 0)
    [localhost] out: Receiving objects: 100% (10/10), done.
    [localhost] out: 

    [localhost] run: git pull
    [localhost] out: Already up-to-date.
    [localhost] out: 


    Done.
    Disconnecting from localhost... done.

---

Roles
=====

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

---


Sudo
====

    from fabric.api import run, sudo, env, settings

    def create_www():
        with settings(sudo_user='http'):
            sudo("mkdir -p /tmp/www")
            sudo("mkdir -p /tmp/www/root")

    def create_cache():
        sudo("mkdir -p /tmp/cache", user="mysql")

---

Sudo
====

running the code:

    $ fab -H localhost create_www
    [localhost] Executing task 'create_www'
    [localhost] sudo: mkdir -p /tmp/www
    [localhost] Login password for 'gregory': 
    [localhost] out: sudo password:
    [localhost] out: 
    [localhost] sudo: mkdir -p /tmp/www/root
    [localhost] out: sudo password:
    [localhost] out: 


Other nice features
===================

 * console.confirm
 * parallel execution
 * hosts

---

Real world examples
===================

 * LFS build scripts : https://github.com/gelendir/lfs-build
 * XiVO prepare-rc-server : https://github.com/xivo-pbx/xivo-tools/blob/master/dev-tools/prepare-rc-server
 * XiVO prepare-rc-client : https://github.com/xivo-pbx/xivo-tools/blob/master/dev-tools/prepare-rc-client


---

Thank you !
===========

 * github : gelendir
 * twitter : @gelendir
 * email : gregory.eric.sanderson@gmail.com
 * repo : http://github.com/gelendir/opencode-fabric
 * presentation : http://remarks.sinaapp.com/repo/gelendir/opencode-fabric/presentation/
