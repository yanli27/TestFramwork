import json
import requests

class BaseApi:
    params = {}
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww34b6c139b7788b0e'
        corpsecret = 'wYmLfimI3JvgoXIHi48DXsa1gMo3XrIKGGEkFISePys'
        data = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{'corpid': corpid, 'corpsecret': corpsecret}
        }
        r=self.send(data)
        token = r.json()['access_token']
        print(token)
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r