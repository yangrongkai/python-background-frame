# coding=UTF-8
# coding=UTF-8

'''
Created on 2016年8月3日

@author: Administrator
'''

# import python standard package
import time
import json
import unittest
import urllib.request
import test.settings

# import thread package

# import my project package
from tuoen.utils.common.signature import unique_parms, generate_signature


class APITestCase(unittest.TestCase):

    _test_url = "http://localhost:{}/api/".format(test.settings.TEST_PORT)

    def _get_current_time(self):
        return int(time.time())

    def _generate_signature(self, parms):
        unique_string, length = unique_parms(parms)
        return generate_signature(unique_string, length)

    def _get_api_url(self):
        return self._test_url

    def _combination_parms(self, **kwargs):
        parms = {
                    "timestamp": self._get_current_time()
                 }
        parms.update(kwargs)
        sign = self._generate_signature(parms)
        parms.update({"sign": sign})
        return parms

    def _connect(cls, url, data):
        postdata = urllib.parse.urlencode(data)
        postdata = postdata.encode('utf-8')
        result = ""
        with urllib.request.urlopen(url, postdata) as rep:
            result = rep.read().decode()
        return result

    def _parse(self, response_text):
        return json.loads(response_text)

    def _get_response_data(self, result):
        status = result['status']
        self.assertEqual(status, 1, result.get("msg", ""))
        return result['data']

    def access_api(self, method, **parms):
        access_parms = self._combination_parms(method=method, **parms)
        response_text = self._connect(self._get_api_url(), access_parms)
        result = self._parse(response_text)
        return self._get_response_data(result)
