import requests
from urllib import parse
import json


class FacebookTokenRefresherException(Exception):
    pass

class FacebookTokenRefresher:
    base_url = 'https://graph.facebook.com/oauth/access_token'
    debug_token_url = 'https://graph.facebook.com/debug_token'

    def __init__(self, app_id, app_secret, short_access_token, proxy_ip):
        self.app_id = app_id
        self.app_secret = app_secret
        self.short_access_token = short_access_token
        self.proxy_ip = proxy_ip

    def get_fake_access_token(self, raise_exception=True):
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
            return dict(parse.parse_qsl(r.text))
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()
    

    def refresh(self, raise_exception=True):
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
            return dict(parse.parse_qsl(r.text))
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
            return dict(parse.parse_qsl(r.text))
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()