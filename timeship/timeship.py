# -*- coding: utf-8 -*-

import datetime

from collections import defaultdict
import numpy as np


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
            return {"__self__": self.value}
        else:
            _ = {
                key: self[key].to_dict()
                for key in self.keys()
            }
            if self.value:
                _.update({"__self__": self.value})
            return _

    def to_array(self):
        if len(self.keys()) == 0:
            return np.array(self.value.starts)
        else:
            _ = np.array([self[key].to_array() for key in self.keys()])
            if self.value:
                _ = np.concatenate(
                    (
                        np.array([self.value.starts]),
                        _,
                    ),
                    axis=0
                )
            return _


class Anchor():
    def __init__(self, id):
        self.id = id
        self.starts, self.stops = [], []
        self.is_active = False

    def __enter__(self):
        self.start()
        current_scope = get_current_scope()
        set_current_scope(
            "/".join([current_scope, self.id]) if len(current_scope) > 0 else self.id
        )
        current_scope = get_current_scope()
        anchors[current_scope].value = self
        return self

    def __exit__(self, *args):
        set_current_scope(get_current_scope().rsplit(self.id, 1)[0])
        self.stop()

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


def get_current_scope():
    global current_scope
    return current_scope


def set_current_scope(id):
    global current_scope
    current_scope = id


current_scope = ""
anchors = rec_defaultdict()
