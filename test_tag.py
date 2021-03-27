import datetime
from selenium import webdriver

import pytest
import allure
import yaml
from jsonpath import jsonpath

from service.tag import Tag

@allure.feature("TestTag")
class TestTag:
    def setup_class(self):
        ##资源初始化
        self.tag=Tag()
        self.tagid=''
        self.group_id='etWtwhEQAAX_WVyJDmfF_Nx3nX2al-Og'

    def teardown_class(self):
        ##资源恢复
        pass
    #
    # @pytest.mark.parametrize("tag_id,tag_name",[
    #                          ['etWtwhEQAAUZvpV2eI58HtpYFSBR5nuQ','ukulele']
    #                          ,['etWtwhEQAAUZvpV2eI58HtpYFSBR5nuQ','ukulele-中文']
    #                          ,['etWtwhEQAAUZvpV2eI58HtpYFSBR5nuQ','ukulele-  ']])
    RESULT_LINK='https://github.com/yanli27/TestFramwork'
    @pytest.mark.parametrize("tag_id,tag_name" ,yaml.load(open('tag_par.yaml','r'),Loader=yaml.FullLoader))
    @allure.story("测试tag的编辑")
    @allure.testcase(RESULT_LINK,'链接')
    @allure.title("测试tag的编辑")
    def test_tag_edit(self,tag_id,tag_name):
        tagname = tag_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
        print('tagname',tagname)
        group_name='uku group'
        id=tag_id
        # r=self.tag.list()
        with allure.step("更新tagname"):
            r=self.tag.update(id,tagname)
        with allure.step("列出更新后的tag列表"):
            r=self.tag.list()

        tags=[
              tag
              for group in r.json()['tag_group'] if group['group_name'] == group_name
              for tag in group['tag'] if tag['name'] == tagname]
        # print('tags',r.json()['tag_group'])
        with allure.step("判断是否更新成功"):
            assert tags !=[]
            assert jsonpath(r.json(),f"$..[?(@.name=='{tagname}')]")[0]['name']==tagname
        newTagname = str(jsonpath(r.json(), f"$..[?(@.name=='{tagname}')]"))
        allure.attach('插入txt：' + newTagname, 'tag',attachment_type=allure.attachment_type.TEXT)
        driver.get()

    @allure.story("测试tag的新增")
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

    @allure.story("列出所有tags")
    def test_list(self):
        self.tag.list()

    @allure.story("删除tag")
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

    @allure.story('删除group')
    def test_delete_group(self):
        self.tag.delete_group(["etWtwhEQAAsSp0ujrSGTqYKqyfvkoxXA"])

    @allure.story('删除tag')
    def test_delete_tag(self):
        self.tag.delete_tag(["etWtwhEQAAvZrYlpgRWxYz2EClCL2jDg"])
