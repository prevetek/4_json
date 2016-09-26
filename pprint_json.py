#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys


def load_data(filepath):
    f = open(filepath, "r")
    data = f.read()
    return data


def pretty_print_json(data):
    parser = json.loads(data)
    pretty = json.dumps(parser, ensure_ascii=False, indent=4, sort_keys=True)
    return pretty


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Укажите путь к json файлу")
    else:
        if len(sys.argv) >= 3:
            print("Много параметров, необходимо указать только путь к json файлу")
        else:
            try:
                data = load_data(sys.argv[1])
                print(pretty_print_json(data))
            except FileNotFoundError:
                print("Указанного файла не существует")
            except json.decoder.JSONDecodeError:
                print("Указанный фаил поврежден")



