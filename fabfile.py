from fabric.api import env, local, run
from fabric.context_managers import cd
from fabric.contrib.project import rsync_project
import os
from datetime import datetime
    
env.hosts = ['frinat.webfactional.com',]
env.user = 'frinat'
env.path = '/home/frinat/webapps/test'


def deploy():
    """
    Switches from the test environment to the deployment one.
    """
    
    # Shutdown
    # Startup catchall static index server in another virtualenv
    # Update packages
    # Copy files
    # Update links
    # Syncdb
    # Shutdown error page
    # Startup

def test():
    """
    Builds all required resources, uploads and deploys to the test environment
    """
    
    css()
    #req()
    backup()
    sync()
    update()
    link()
    #syncdb()
    restart()

def backup():
    d = ('/home/frinat/backup/%s' % datetime.now()).replace(' ', '_').replace(':', '-')
    
    run("mkdir -p /home/frinat/backup")
    run("cp -R '%s' '%s'" % (env.path, d))
    run("rm -rf %s/apache2" % d)
    run("pg_dump -bc -U frinat_test frinat_test >'%s/dump.sql'" % d)

def restart():
    run("%s/apache2/bin/restart" % env.path)
    #run("touch {0}/server.wsgi".format(env.path))

def syncdb():
    prj = os.path.join(env.path, 'fribourg_www')
    mng = os.path.join(prj, 'manage.py')
    
    # Get the actual DB from the production server
    #run("pg_dump -bc -U frinat_deploy frinat_deploy | sed s/frinat_deploy/frinat_test/g | psql -U frinat_test frinat_test")
    run('workon test ; python {0} syncdb --noinput'.format(mng))
    run('workon test ; python {0} migrate'.format(mng))

def resetdb():
    run("for TABLE in $(psql -d frinat_test -U frinat_test -t -c \"SELECT tablename FROM pg_tables WHERE schemaname='public';\") ; do psql -d frinat_test -U frinat_test -t -c \"DROP TABLE $TABLE CASCADE;\" ; done")

def link():
    """
    Creates all needed symbolic links.
    """
    run("workon test ; ln -fs $VIRTUAL_ENV/src/django/django/contrib/admin/media {0}/htdocs/admin".format(env.path))
    run("workon test ; ln -fs $VIRTUAL_ENV/src/django-cms/cms/media/cms/ {0}/htdocs/cms".format(env.path))

def update():
    """
    Updates all installed packages to match the development platform
    """
    req = os.path.join(env.path, 'requirements.txt')
    run("workon test ; pip install -r {0}".format(req))

def sync():
    """
    Synchronize project with webserver.
    """
    rsync_project(env.path, local_dir='*', delete=True, exclude=[
        '*.pyc','.DS_Store', '.git*', '*.log',
        'htdocs/assets/*',              # Dont' delete deployment assets
        'htdocs/cms_page_media/*',      # Same as above
        'htdocs/admin',                 # Will be linked by the webserver
        'htdocs/cms',                   # Same as above
        'data',                         # We don't need the data directory for deployment
        'fabfile.py',                   # Ignore the tasks file
        'server.py',                    # Twisted servercd 
    ])
    
    prj = os.path.join(env.path, 'fribourg_www')
    sts = os.path.join(prj, 'settings', '__init__.py')
    run('echo "from settings.test import *" >{0}'.format(sts))
    
def req():
    #local("pip freeze -E /Library/Frameworks/Python.framework/Versions/2.6/bin/python >requirements.txt")
    local("workon frinat ; pip freeze >requirements.txt")
    local("sort requirements.txt | uniq -u - requirements.txt")

def css():
    """
    Rebuilds all css files from scratch.
    """
    local("(cd data/sass ; compass)")