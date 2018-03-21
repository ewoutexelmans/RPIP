import socket
import os

from slackclient import SlackClient

path = os.path.join(os.path.expanduser('~pi'),'rpip','jaar2','myIp')


def getIp():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	connected = False
	while not connected:
		try:
			s.connect(("gmail.com",80))
			connected = True
		except Exception as e:
			pass
	ip_address = s.getsockname()[0]
	s.close()
	return ip_address

def postIp(ip):
	token = "xoxp-154174916502-152816805521-153496385266-85efd12889dffa402e945522228b2cce"
	sc = SlackClient(token)
	resp = sc.api_call(
		"chat.postMessage",
		channel = "@ewout",
		text = "Het ip addres van de raspberry pi van Ewout is "+ip
	)

def compareIp(ip , path):
	ip_file = open(path,"r+")
	if ip_file.mode == 'r+':
		old_ip = ip_file.read()
		if ip != old_ip:
			postIp(getIp())
			ip_file.seek(0)
			ip_file.truncate()
			ip_file.write(ip)
		else:
			postIp("hetzelfde")
	ip_file.close

compareIp(getIp() , path)
