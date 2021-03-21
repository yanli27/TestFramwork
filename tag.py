import requests
import json
import datetime

from service.base_api import BaseApi

class Tag(BaseApi):
    def __init__(self):
        super().__init__()
        # self.token=self.get_token()


    #"group_id": "etWtwhEQAAX_WVyJDmfF_Nx3nX2al-Og",
    #"group_name": "uku group",
    #tag_id:etWtwhEQAASYttJQxaxEUboJ1eHoigPg
    def list(self,groupid=None):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params":{"access_token":self.token},
            "json":{
                "tag_id": [],
                "group_id":[groupid]
            }
        }
        r=self.send(data)
        return r
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
        #                   , params={
        #         "access_token": self.token
        #     }
        #                   , json={
        #         "tag_id": [],
        #         "group_id":[groupid]
        #     }
        #                   )
        # print(json.dumps(r.json(), indent=2))
        # return r


    def update(self, tagid,tagname):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "id": tagid,
                "name": tagname
            }
        }
        r=self.send(data)
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag'
        #                   , params={
        #         "access_token": self.token
        #     },json={
        #         "id": tagid,
        #         "name": tagname
        #     })
        # print(json.dumps(r.json(), indent=2))
        return r

    def add(self, groupname,tag,**kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                        "group_name": groupname,
                        "tag":tag,
                        **kwargs
                    }
        }
        r=self.send(data)
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        #                   params={"access_token": self.token},
        #                   json={
        #                       "group_name": groupname,
        #                       "tag":tag,
        #                       **kwargs
        #                       # "tag": [{
        #                       #     "name": tag,
        #                       # }
        #                       # ]
        #                   }
        #                   )
        # # print(json.dumps(r.json(), indent=2))
        return r

    def delete(self,tagid):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                        "tag_id": [
                            tagid
                        ]
                    }
        }
        r=self.send(data)
        # r= requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #                  params={
        #                      "access_token":self.token
        #                  },
        #                  json={
        #                      "tag_id": [
        #                          tagid
        #                      ]
        #                  })
        # print(json.dumps(r.json(),indent=2))
        return r

    def delete_group(self,group_id):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params":{"access_token":self.token},
            "json":{
            "group_id":group_id
        }
        }
        # r=requests.post(
        #   "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
        #   params={"access_token":self.token},
        #   json={
        #       "group_id":group_id
        #   }
        #
        # )
        r=self.send(data)
        # print(json.dumps(r.json(),indent=2))
        return r

    def delete_tag(self,tag_id):
        # r=requests.post(
        #     "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
        #     params={"access_token":self.token},
        #     json={
        #         "tag_id":tag_id
        #     }
        # )
        # print(json.dumps(r.json(),indent=2))
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "tag_id":tag_id
            }
        }
        r=self.send(data)
        return r