#!/usr/bin/python3
"""load_from_json_file function"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    list_argv = []
    for arg in sys.argv[1:]:
        list_argv.append(arg)

    existing_data = load_from_json_file('add_item.json')
    existing_data.extend(list_argv)

    save_to_json_file(existing_data, 'add_item.json')

    load_from_json_file('add_item.json')


if __name__ == "__main__":
    main()
