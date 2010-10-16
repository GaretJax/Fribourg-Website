import sys
import os

from twisted.application import internet, service
from twisted.web import server, resource, wsgi, static, proxy
from twisted.python import threadpool
from twisted.internet import reactor

# Environment setup for your Django project files:
sys.path.append("fribourg_www")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from settings import PORT

class Root(resource.Resource):
    def __init__(self, wsgi_resource):
        resource.Resource.__init__(self)
        self.wsgi_resource = wsgi_resource
    
    def getChild(self, _, request):
        path = request.prepath.pop(0)
        request.postpath.insert(0, path)
        return self.wsgi_resource

def wsgi_resource():
    from django.core.handlers.wsgi import WSGIHandler
    
    pool = threadpool.ThreadPool()
    pool.start()
    
    # Allow Ctrl-C to get you out cleanly:
    reactor.addSystemEventTrigger('after', 'shutdown', pool.stop)
    
    # Add change notification restarting
    wsgi_resource = wsgi.WSGIResource(reactor, pool, WSGIHandler())
    
    return wsgi_resource

# WSGI container for Django, combine it with twisted.web.Resource:
root = Root(wsgi_resource())

# Serve media files off of /media:
static_res = static.File(os.path.join(os.path.dirname(__file__), "htdocs"))
#print static_res.contentTypes
#static_res.contentTypes = static.loadMimeTypes(['data/mime.types'])
#print static_res.contentTypes
root.putChild("media", static_res)

# The cool part! Add in pure Twisted Web Resouce in the mix
# This 'pure twisted' code could be using twisted's XMPP functionality, etc:
#root.putChild("google", twresource.GoogleResource())

# Twisted Application Framework setup:
application = service.Application('twisted-django')
site = server.Site(root, logPath='logs/access.log')
internet.TCPServer(PORT, site).setServiceParent(application)
