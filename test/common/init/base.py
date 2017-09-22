# coding=UTF-8


class BaseInitiator(object):

    def __init__(self, initiator=None, *initiators):
        self._initiators = [initiator] if initiator is not None else []
        if initiators:
            self._initiators.extend(initiators)

    def init_data(self):
        raise NotImplementedError("please implement this interface!")

    def add(self, initiator, *initiators):
        self._initiator.append(initiator)
        if initiators:
            self._initiator.extend(initiators)

    def remove(self, initiator, *initiators):
        self._initiators.remove(initiator)
        for _initiator in self._initiators:
            self._initiators.remove(_initiator)

    def run(self):
        self.init_data()
        if self._initiators:
            for _initator in self._initiators:
                _initator.init_data()
