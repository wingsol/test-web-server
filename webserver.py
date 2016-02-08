#!/usr/bin/python

# Simple httpd

import sys
from twisted.internet import reactor
from twisted.application import internet, service
from twisted.web import static, server, script, http
from twisted.python import log

class Site(server.Site):
    def getResourceFor(self, request):
        request.setHeader('server', 'Server/1.9E377')
        request.setHeader('Allow', 'HEAD, GET, POST')
        request.setHeader('Access-Control-Allow-Origin', '*')
        request.setHeader('Access-Control-Allow-Methods', 'GET')
        request.setHeader('Access-Control-Allow-Headers', 'x-prototype-version,x-requested-with')
	return server.Site.getResourceFor(self, request)


root = static.File("htdocs")
root.indexNames=['index.html']
root.processors = {'.rpy': script.ResourceScript}
application = service.Application('web')
sc = service.IServiceCollection(application)

site = server.Site(root)

log.startLogging(sys.stderr)
reactor.listenTCP(8000, Site(root))
reactor.run()