# -*- coding: utf-8 -*-

import datetime

from collections import defaultdict


class rec_defaultdict(defaultdict):

    def __init__(self, *args, **kwargs):
        self.value = None
        super(rec_defaultdict, self).__init__(self.__class__, *args, **kwargs)

    def __getitem__(self, key):
        if '/' not in key:
            return super(rec_defaultdict, self).__getitem__(key)
        else:
            id, key = key.split("/", 1)
            return self[id][key]

    def to_dict(self):
        if len(self.keys()) == 0:
            return self.value.starts
        else:
            return {
                key: self[key].to_dict()
                for key in self.keys()
            }


class Anchor():
    def __init__(self, id):
        self.id = id
        self.starts, self.stops = [], []
        self.is_active = False

    def start(self):
        self.starts.append(datetime.datetime.now())
        self.is_active = True

    def stop(self):
        self.stops.append(datetime.datetime.now())
        self.is_active = False


def anchor(id=None):
    if id is None:
        [anchor.stop for anchor in anchors.values() if anchor.is_active]
    elif id in anchors.keys():
        anchors[id].start()
    else:
        anchor = Anchor(id)
        anchor.start()
        anchors[id].value = anchor


def plot():
    pass


anchors = rec_defaultdict()
