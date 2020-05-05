# -*- coding:utf-8 -*-

from transfer import Transfer, TransferError


class TESTTransfer(Transfer):

    def run(self):
        test_funcs = [
            {
                "id": 1,
                "name": "index",
                "action": self.index,
            },
            {
                "id": 2,
                "name": "get_config",
                "action": self.get_config,
            },
            {
                "id": 3,
                "name": "get_live_channel_list",
                "action": self.get_live_channel_list,
            },
            {
                "id": 4,
                "name": "add_live_channel",
                "action": self.add_live_channel,
                "args": {
                    "name": "test add",
                    "cid": "test",
                    "urls": ["https://cctvtxyh5c.liveplay.myqcloud.com/live/cdrmcctv1_1_td.m3u8"],
                    "ptlimpl": "hls",
                    "filetype": "ts",
                    "time_delay": 180
                }
            },
            {
                "id": 5,
                "name": "get_live_channel",
                "action": self.get_live_channel,
                "args": {"cid": "test"}
            },
            {
                "id": 6,
                "name": "modify_live_channel",
                "action": self.modify_live_channel,
                "args": {"name": "test modify", "cid": "test"}
            },
            {
                "id": 7,
                "name": "reset_live_channel",
                "action": self.reset_live_channel,
                "args": {"cid": "test"}
            },
            {
                "id": 8,
                "name": "delete_live_channel",
                "action": self.delete_live_channel,
                "args": {"cid": "test"}
            },
        ]

        print "test transfer api funcs"
        for test_fun in test_funcs:
            try:
                test_fun['action'](**test_fun.get('args', {}))
            except TransferError as err:
                print "[{}] test func {} ==> failure".format(test_fun['id'], test_fun['name'])
                print "error: {}".format(err)
                return

            print "[{}] test func {} ==> ok".format(test_fun['id'], test_fun['name'])



