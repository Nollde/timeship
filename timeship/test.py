# -*- coding: utf-8 -*-

import time

import timeship


def main():
    timeship.anchor("a/b")
    time.sleep(1)
    timeship.anchor("a/c")
    time.sleep(1)
    timeship.anchor("a/b/x")
    time.sleep(1)
    timeship.anchor("a/b/y")
    time.sleep(1)
    from IPython import embed; embed()

    print(timeship.anchors.to_dict())


if __name__ == '__main__':
    main()
