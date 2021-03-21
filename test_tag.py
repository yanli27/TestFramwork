import requests
import json
import datetime
from service.tag import Tag
from jsonpath import jsonpath
import pytest
import yaml

class TestTag:
    def setup_class(self):
        self.tag=Tag()
        self.tagid=''
        self.group_id='etWtwhEQAAX_WVyJDmfF_Nx3nX2al-Og'

    def teardown_class(self):
        pass
    #
    # @pytest.mark.parametrize("tag_id,tag_name",[
    #                          ['etWtwhEQAAUZvpV2eI58HtpYFSBR5nuQ','ukulele']
    #                          ,['etWtwhEQAAUZvpV2eI58HtpYFSBR5nuQ','ukulele-中文']
    #                          ,['etWtwhEQAAUZvpV2eI58HtpYFSBR5nuQ','ukulele-  ']])
    @pytest.mark.parametrize("tag_id,tag_name" ,yaml.load(open('tag_par.yaml','r'),Loader=yaml.FullLoader))
    def test_tag_edit(self,tag_id,tag_name):
        tagname = tag_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
        print('tagname',tagname)
        group_name='uku group'
        id=tag_id
        # r=self.tag.list()
        r=self.tag.update(id,tagname)
        r=self.tag.list()

        tags=[
              tag
              for group in r.json()['tag_group'] if group['group_name'] == group_name
              for tag in group['tag'] if tag['name'] == tagname]
        print('tags',r.json()['tag_group'])
        assert tags !=[]
        print('tagname', jsonpath(r.json(), f"$..[?(@.name=='{tagname}')]"))
        assert jsonpath(r.json(),f"$..[?(@.name=='{tagname}')]")[0]['name']==tagname


    def test_add_tag(self):
        group_name='uku group'
        tag1 = 'test add tag' + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
        tag2 = 'test add tag 2' + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
        tag3 = 'test add tag 3' + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
        tag = [
            {"name": tag1},
            {"name": tag2},
            {"name": tag3},
        ]
        self.tag.add(groupname=group_name, tag=tag)

    def test_list(self):
        self.tag.list()

    def test_delete_tag(self):
        r = self.tag.list(self.group_id)
        tags=[
            tag
            for group in r.json()['tag_group']
            for tag in group['tag'] if tag['deleted'] is False
        ]
        print(tags)
        self.tagid = tags[0]['id']
        # print(r.json()['tag_group'][0]['tag'][0])
        self.tag.delete(self.tagid)

        def test_delete_group(self):
            self.tag.delete_group(["etWtwhEQAAsSp0ujrSGTqYKqyfvkoxXA"])

        def test_delete_tag(self):
            self.tag.delete_tag(["etWtwhEQAAvZrYlpgRWxYz2EClCL2jDg"])
