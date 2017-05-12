#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by why001

import sys
import os
import re
import zipfile
import plistlib

def ipa_name_from_arguments():
    argvs = sys.argv
    ipa_name = None
    if len(argvs) >= 2:
        ipa_name = argvs[1]
    else:
        print('please input the name of ipa or apk!')
        print('for exmaple: python ipaparser.py google.ipa')
    return ipa_name

def plist_path_with_ipa_path(ipa_path):
    ipa_file = zipfile.ZipFile(ipa_path)
    name_list = ipa_file.namelist()

    regex = re.compile(r'Payload/[^/]+.app/Info.plist')
    result = list(filter(regex.search, name_list))
    if result:
        return result[0]

def plist_info_with_path(plist_path, ipa_path):
    ipa_file = zipfile.ZipFile(ipa_path)
    plist_data = ipa_file.read(plist_path)
    plist_root = plistlib.loads(plist_data)
    return plist_root

def info_of_plist_property(plist_info, property_name):
    value = plist_info[property_name]
    print(property_name + ' is ' + str(value))
    return value

if __name__ == '__main__':
    ipa_name = ipa_name_from_arguments()

    ipa_path = os.path.join(os.getcwd(), ipa_name)
    plist_path = plist_path_with_ipa_path(ipa_path)
    plist_info = plist_info_with_path(plist_path, ipa_path)
    info_of_plist_property(plist_info, 'CFBundleVersion')
