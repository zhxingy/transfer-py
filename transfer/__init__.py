# -*- coding:utf-8 -*-

import re
import json
import urlparse
import requests
import xmltodict


class TransferError(Exception):
    pass


class Transfer(object):

    def __init__(self, service, user=None, password=None, proxy=None, timeout=30):
        self._proxy = {} if proxy is None else {"http": proxy}
        self._timeout = timeout

        netloc = urlparse.urlparse(service).netloc
        if re.search(r'(?P<user>.*):(?P<pwd>.*)@.*', netloc) is None:
            if user is None or password is None:
                raise TransferError("No account number or password was entered")
            netloc = "{}:{}@{}".format(user, password, netloc)

        self._service = "http://{}/api".format(netloc)

    def _request(self, request_params, out_format="json"):
        response = requests.get(self._service, params=request_params, timeout=self._timeout, proxies=self._proxy)
        try:
            response.raise_for_status()
        except requests.HTTPError as err:
            if response.status_code >= 500:
                raise err

        if response.status_code == 401:
            raise TransferError("Login failed, account number or password is wrong")

        response_string = response.text
        if out_format == "str":
            return response_string
        else:
            converted_dict = xmltodict.parse(response_string, encoding="utf-8")
            return json.loads(json.dumps(converted_dict))

    @staticmethod
    def _raise(**kwargs):
        if kwargs.get('@ret', '0') != "0":
            raise TransferError(kwargs['@reason'])

    def index(self):
        response = self._request({"func": "system"})
        self._raise(**response['api_result']['result'])
        return response['api_result']['system']

    def get_config(self):
        return self._request({"func": "conf_file"}, out_format="str")

    def get_live_channel_list(self):
        response = self._request({"func": "live_channellist"})
        self._raise(**response['channellist']['result'])
        channel_list = response['channellist']['channel']
        new_channel_list = []
        for channel in channel_list:
            new_channel = {}
            for k, v in channel.items():
                new_channel[k.strip('@')] = v
            new_channel_list.append(new_channel)

        return new_channel_list

    def get_live_channel(self, cid):
        response = self._request(
            {
                "func": "live_id",
                "id": cid
            }
        )
        self._raise(**response['api_result']['result'])
        channel = response['api_result']['channel']
        new_channel = {}
        for k, v in channel.items():
            new_channel[k.strip('@')] = v

        return new_channel

    def modify_live_channel(self, cid, name=None, time_delay=None):
        if name is None and time_delay is None:
            return

        channel = self.get_live_channel(cid)
        if name is None:
            name = channel['name']
        else:
            time_delay = channel['time_delay']

        response = self._request(
            {
                'func': 'live_modify',
                'id': cid,
                'name': name,
                'time_delay': time_delay
            }
        )
        self._raise(**response['api_object']['result'])

    def delete_live_channel(self, cid):
        response = self._request(
            {
                "func": "live_delete",
                "id": cid
            }
        )
        self._raise(**response['api_object']['result'])

    def reset_live_channel(self, cid):
        response = self._request(
            {
                "func": "live_reset",
                "id": cid
            }
        )
        self._raise(**response['api_object']['result'])

    def add_live_channel(self, cid, name, urls, ptlimpl="std", filetype="forceudp_ts", time_delay=180):
        response = self._request(
            {
                'func': 'live_add',
                'id': cid,
                'url': '$'.join(urls),
                'name': name,
                'ptlimpl': ptlimpl,
                'filetype': filetype,
                'time_delay': time_delay
            }
        )

        self._raise(**response['api_object']['result'])


