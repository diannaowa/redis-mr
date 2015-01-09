#!/usr/bin/env python
#coding=utf-8
#author:liuzhenwei
#email:570962906@qq.com
#date:2015-01-09
import sys,socket,hiredis

STAR = "*"
DOLLAR = "$"
CRLF = "\r\n"

class runCmd():
	def __init__(self,host,port):
		self.host = host
		self.port = port
		self.msg = None
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.reader = hiredis.Reader()
		self.socket.settimeout(8)
		try:
			self.socket.connect((host,port))
		except socket.error:
			print >>sys.stderr,"connect %s:%s error" %(host,port)
	def sendCmd(self,command):
		for c in command:
			self.socket.send(c)
		self.msg = self.socket.recv(1024)
		self.reader.feed(self.msg)
		msg = self.reader.gets()
		return msg
	def close(self):
		return self.socket.close()


def _parseHostPort(host_port):
	host,port = host_port.split(":")
	return host,int(port)
#ensure
def _ensureSlave():
	"""......"""
	pass

#create command
def createCmd(*args):
	cmd = []
	for arg in args:
		c = arg.split(" ")
		start = ["".join([STAR,str(len(c)),CRLF])]
		c = ["".join([DOLLAR,str(len(x)),CRLF,x,CRLF]) for x in c]
		cmd.append("".join(start+c))
	return cmd
#create a new slave
def replcate(masterHostPort,slaveHostPort,masterAuth=None):
	host,port = _parseHostPort(masterHostPort)
	s = runCmd(*_parseHostPort(slaveHostPort))
	if masterAuth != None:
		cmd = createCmd("SLAVEOF %s %s"%(host,port),"CONFIG SET masterauth %s"%masterAuth,"CONFIG REWRITE")
	else:
		cmd = createCmd("SLAVEOF %s %s"%(host,port),"CONFIG REWRITE")
		
	msg = s.sendCmd(cmd)
	s.close()
	if msg == "OK":
		print "create slave %s:%s ok" %_parseHostPort(slaveHostPort)
	else:
		print >>sys.stderr,"create slave %s:%s error" %_parseHostPort(slaveHostPort)

#delete slave or promote a slave to master
def delete(slaveHostPort):
	s = runCmd(*_parseHostPort(slaveHostPort))
	cmd = createCmd("SLAVEOF no one","CONFIG REWRITE")
	msg = s.sendCmd(cmd)
	s.close()
	if msg == "OK":
		print "promote slave %s:%s to master ok"%_parseHostPort(slaveHostPort)
	else:
		print >>sys.stderr,"promote slave %s:%s to master error"%_parseHostPort(slaveHostPort)

#shutdown the redis server
def shutdown(hostPort):
	s = runCmd(*_parseHostPort(hostPort))
	cmd = createCmd("SHUTDOWN")
	msg = s.sendCmd(cmd)
	s.close()
	print "shutdown ok"
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print >>sys.stderr,"USAGE:"
		print >>sys.stderr,"redis-mr.py ACTION [host:port ......]"
		sys.exit(1)
	getattr(sys.modules[__name__],sys.argv[1])(*sys.argv[2:])

