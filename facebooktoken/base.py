import requests
from urllib import parse
import json


class FacebookTokenRefresherException(Exception):
    pass

class FacebookTokenRefresher:
    base_url = 'https://graph.facebook.com/oauth/access_token'
    debug_token_url = 'https://graph.facebook.com/debug_token'
    client_code_url='https://graph.facebook.com/oauth/client_code'

    def __init__(self, app_id, app_secret, short_access_token,app_access_token,long_term_token, proxy_ip):
        self.app_id = app_id
        self.app_secret = app_secret
        self.short_access_token = short_access_token
        self.proxy_ip = proxy_ip
        self.app_access_token=app_access_token
        self.long_term_token = long_term_token

    def get_app_access_token(self, raise_exception=True):
        params = {
            'grant_type': 'client_credentials',
            'client_id': self.app_id,
            'client_secret': self.app_secret
        }
        proxy_setting={'http': self.proxy_ip,'https': self.proxy_ip}
        print (self.proxy_ip)
        print (proxy_setting)
        print (self.base_url)
        print (params)
        r = requests.get(self.base_url, params=params,proxies=proxy_setting)
        print (r.url)
        print (r.text)
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()
    
    def long_term_token_for_each_client(self,long_term_token, redirect_uri,raise_exception=True):
        
        #get long-term user_access_token for each client from same long-term user_access_token

        #get client_code from long-term user_access_token
        codeResults = self.get_client_code(long_term_token,redirect_uri)
        client_code=codeResults['code']
        print ('temp client_code:'+client_code)

        #get new long-term user_access_token from client_code
        results = self.get_long_term_token_from_client_code(client_code,redirect_uri)
        new_long_access_token=results['access_token']
        print ('new long_access_token for each client:'+new_long_access_token)
        return results
    
    def get_client_code(self,long_term_token, redirect_uri,raise_exception=True):
        params = {
            'client_secret': self.app_secret,
            'client_id': self.app_id,
            'redirect_uri': redirect_uri,
            'access_token':long_term_token
        }
        proxy_setting={'http': self.proxy_ip,'https': self.proxy_ip}
        print (self.proxy_ip)
        print (proxy_setting)
        print (self.client_code_url)
        print (params)
        r = requests.get(self.client_code_url, params=params,proxies=proxy_setting)
        print (r.url)
        print (r.text)
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()
    
    def get_long_term_token_from_client_code(self,client_code, redirect_uri,raise_exception=True):
        params = {
            'code': client_code,
            'client_id': self.app_id,
            'redirect_uri': redirect_uri
        }
        proxy_setting={'http': self.proxy_ip,'https': self.proxy_ip}
        print (self.proxy_ip)
        print (proxy_setting)
        print (self.base_url)
        print (params)
        r = requests.get(self.base_url, params=params,proxies=proxy_setting)
        print (r.url)
        print (r.text)
        if r.status_code == 200:
             return json.loads(r.text)
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()
    
    def exchange_long_term_token(self, raise_exception=True):
        params = {
            'grant_type': 'fb_exchange_token',
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'fb_exchange_token': self.short_access_token
        }
        proxy_setting={'http': self.proxy_ip,'https': self.proxy_ip}
        print (self.proxy_ip)
        print (proxy_setting)
        print (self.base_url)
        print (params)
        r = requests.get(self.base_url, params=params,proxies=proxy_setting)
        print (r.url)
        print (r.text)
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()
    
    def exchange_extend_sso_token(self, raise_exception=True):
        params = {
            'grant_type': 'fb_extend_sso_token',
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'access_token': self.long_term_token
        }
        proxy_setting={'http': self.proxy_ip,'https': self.proxy_ip}
        print (self.proxy_ip)
        print (proxy_setting)
        print (self.base_url)
        print (params)
        r = requests.get(self.base_url, params=params,proxies=proxy_setting)
        print (r.url)
        print (r.text)
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()
    
    def detail(self, app_access_token,raise_exception=True):
        params = {
            'input_token': app_access_token,
            'access_token': self.short_access_token
        }
        
        proxy_setting={'http': self.proxy_ip,'https': self.proxy_ip}
        print (self.proxy_ip)
        print (proxy_setting)
        print (self.debug_token_url)
        print (params)
        r = requests.get(self.debug_token_url, params=params,proxies=proxy_setting)
        print (r.url)
        print (r.text)
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()