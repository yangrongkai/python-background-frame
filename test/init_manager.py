# coding=UTF-8

import init_envt

from tuoen.utils.common.single import Single

from test.init import CustomerInitiator


class InitManager(Single):

    def __init__(self):
        self._is_finished = False
        self._root_list = self._load()

    def _load(self):
        customer_root = CustomerInitiator()
        return customer_root,

    def run(self):
        if not self._root_list:
            raise RuntimeWarning("please to loading Initiator")

        for _root in self._root_list:
            _root.run()

    @classmethod
    def get_manager(cls):
        return InitManager()


if __name__ == "__main__":
    InitManager.get_manager().run()
