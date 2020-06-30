#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiaoxiaowukong
# datetime:2020/6/30 上午11:03
# software: PyCharm
import sys

import os
import util
import config
import shutil


def split(i_path, o_path):
    zoom = 17
    for index in range(2, 21, 1):
        print (index)
        output_path = os.path.join(o_path, str(index))
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        print(zoom)
        min_x, min_y = util.get_tile_num(config.range[zoom][index][1], config.range[zoom][index][2], zoom)
        max_x, max_y = util.get_tile_num(config.range[zoom][index][0], config.range[zoom][index][3], zoom)
        for root, dirs, files in os.walk(i_path):
            for name in files:
                if os.path.splitext(name)[-1] == ".png":
                    [z, x, y] = os.path.splitext(name)[0].split("-")
                    if int(x) > int(min_x) and int(x) < int(max_x) and int(y) > int(min_y) and int(y) < int(max_y):
                        try:
                            shutil.move(os.path.join(root, name), "{}/{}".format(output_path, name))
                        except Exception as e:
                            print(e.message)


if __name__ == '__main__':
    args = sys.argv[1:]
    i_path = args[0]
    o_path = args[1]
    if not os.path.exists(i_path) or not os.path.exists(o_path):
        print("dir is not exist")
        exit(1)
    split(i_path, o_path)
