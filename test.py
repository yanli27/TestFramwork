import yaml
def test_yaml():
    data=yaml.load(open('tag_par.yaml', 'r'),Loader=yaml.FullLoader)
    print(data)