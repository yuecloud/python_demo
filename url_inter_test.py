import requests
import pytest

#get请求查看v2ex的接口，查看返回值是否正常
class TestV2exApi():
    domain = 'https://www.v2ex.com/'
    def test_node(self):
        path = 'api/nodes/show.json?name=python'
        url = self.domain + path
        res = requests.get(url).json()
        assert res['id'] == 90
        assert res['name'] == 'python'
        assert  res['parent_node_name'] =="programming"


if __name__=="__main__":
    pytest.main(['--self-contained-html','--html','report/report.html'])
