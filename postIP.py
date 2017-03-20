import socket
from slackclient import SlackClient

def getIp():
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	connected=False
	while not connected:
		try:	
			s.connect(("gmail.com",80))
			connected = True
		except Exception as e:
			pass
	ip_address=s.getsockname()[0]
	s.close()
	return ip_address

def postIp(post_Ip):
	token = "xoxp-154174916502-152816805521-153496385266-85efd12889dffa402e945522228b2cce"
	sc = SlackClient(token)
	resp = sc.api_call(
		"chat.postMessage",
		channel="#rpip",
		text="Het ip addres van de raspberry pi van Ewout is: "+post_Ip
	)
postIp(getIp())
