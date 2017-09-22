# coding=UTF-8

'''
Created on 2016年8月24日

@author: Administrator
'''

# import python standard package

# import thread package

# import my project package
from tuoen.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_tuoen',
        'USER': 'root',
        'PASSWORD': 'yangrongkai',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}

TEST_PORT = "8080"
