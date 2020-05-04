# -*- coding:utf-8 -*-

import os
from transfer import Transfer,TransferError


def test():
    test_server = os.environ.get('TEST_SERVER')
    test_username = os.environ.get('TEST_USER')
    test_password = os.environ.get('TEST_PWD')
    print "test transfer func"
    if test_server is None or test_username is None or test_password is None:
        print "test connect to server ==> failure"
        print "error failed to obtain an environment variable"
        return

    ts = Transfer(service=test_server, user=test_username, password=test_password)

    print "[1] test func index"
    try:
        ts.index()
    except TransferError as err:
        print "[1] test func index ==> failure"
        print "err: {}".format(err)
        return
    else:
        print "[1] test func index ==> ok"

    print "[2] test func get_config"
    try:
        ts.get_config()
    except TransferError as err:
        print "[2] test func get_config ==> failure"
        print "err: {}".format(err)
        return
    else:
        print "[2] test func get_config ==> ok"

    print "[1] test func get_live_channel_list"
    try:
        ts.get_live_channel_list()
    except TransferError as err:
        print "[1] test func index ==> failure"
        print "err: {}".format(err)
        return
    else:
        print "[1] test func index ==> ok"

    print "[1] test func index"
    try:
        ts.index()
    except TransferError as err:
        print "[1] test func index ==> failure"
        print "err: {}".format(err)
        return
    else:
        print "[1] test func index ==> ok"


test()