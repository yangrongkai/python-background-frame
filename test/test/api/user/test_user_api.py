# coding=UTF-8

import json

from test.common.testcase.api_test_case import APITestCase


class TestUserAPI(APITestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_register(self):
        """ test user to register """

        method = "patient.tuoen.user.customer.register"
        phone = "15512345678"
        passwd = "123456"
        verify_code = "1231"
        role_type = 1
        other_infos = json.dumps({'name': 'yrk', 'city': 'hahahha'})

        result = self.access_api(method=method, phone=phone, passwd=passwd,\
                        verify_code=verify_code, role_type=role_type,\
                                other_infos=other_infos)

        self.assertTrue('auth_token' in result)
        self.assertTrue('expire_time' in result)
        self.assertTrue('renewal_flag' in result)
