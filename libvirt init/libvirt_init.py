#!/usr/bin/env python2

import libvirt
import time
conn = libvirt.open('qemu:///system')

for id in conn.listDomainsID():
	dom = conn.lookupByID(1)
	print "Dom %s State %s" % (dom.name(), dom.info()[0])
	dom.suspend()
	time.sleep(5)
	print "Dom %s State %s (after suspend)" % (dom.name(), dom.info()[0])
	dom.resume()
	time.sleep(5)
	print "Dom %s State %s (after resume)" % (dom.name(), dom.info()[0])
	
