#This File's name is getToken.py
def getToken():
	import urllib3, json
	r = urllib3.PoolManager().request('GET', 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=YCMSAhotdtVVKgeabGEeHI7V&client_secret=yGYtfbOCHEdGO3cjuex7U8zSvPyUPIuu')
	return json.loads(r.data)['access_token']