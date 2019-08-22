# -*- coding: utf-8 -*-

import time

import timeship


def main():
    timeship.anchor("a/b/y")
    time.sleep(1)
    with timeship.Anchor("a"):
        with timeship.Anchor("b"):
            with timeship.Anchor("c"):
                time.sleep(2)
    from IPython import embed; embed()
    print(timeship.anchors.to_dict())


if __name__ == '__main__':
    main()
