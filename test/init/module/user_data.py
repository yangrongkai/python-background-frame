# coding=UTF-8

import random

from test.common.init.base import BaseInitiator

from model.models import RoleType, GenderType, SourceType, PlatformType,\
        User, Customer


class CustomerInitiator(BaseInitiator):

    _role_type = RoleType.CUSTOMER

    def _get_test_data(self, num=10):
        name_prefix = "TEST"
        phone_prefix = "155"
        nick_prefix = "NICK"
        photo_url = ""
        city = "武汉"
        address = "武昌路安阳街{}号"
        passwd = "123456"

        for index in range(num):
            phone = phone_prefix + str(index).rjust(8, "0")
            yield {
                'phone': phone,
                'account': phone,
                'passwd': passwd,
                'role_type': self._role_type,
                'plat_type': random.choice(PlatformType.CHOICES)[0],
                'nick': nick_prefix + str(index),
                'photo_url': photo_url,
            }, {
                'source': random.choice(SourceType.CHOICES)[0],
                'name': name_prefix + str(index),
                'gender': random.choice(GenderType.CHOICES)[0],
                'city': city,
                'address': address.format(str(index))
            }

    def init_data(self):
        for user_infos, role_infos in self._get_test_data():
            user = User.create(**user_infos)
            Customer.create(user=user, **role_infos)
