from facebooktoken import FacebookTokenRefresher

app_id = ""
app_secret=""
proxy_ip='http://proxy.***.****.com:8080'
app_access_token=""
short_access_token=""
redirect_uri="https://***.***.***.com/test/FacebookAuthRedirect"
ftr = FacebookTokenRefresher(
	app_id=app_id,
	app_secret=app_secret,
	short_access_token=short_access_token,
	app_access_token=app_access_token,
	proxy_ip=proxy_ip
)

#get access_token=client_id|client_secret
#results = ftr.get_app_access_token()

#exchange long-term token
#results = ftr.exchange_long_term_token()
long_term_token=results['access_token']
print ('long_term_token:'+long_term_token)

#get token detail
#results = ftr.detail(app_access_token,checked_access_token)

#get client code from long-term token
results = ftr.get_client_code(long_term_token,redirect_uri)
client_code=results['code']
print ('client_code:'+client_code)

result = ftr.get_long_term_token_from_client_code(client_code,redirect_uri)
new_long_access_token=results['access_token']
print ('new_long_access_token:'+new_long_access_token)
print ('1323423')