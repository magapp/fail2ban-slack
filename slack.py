# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: t -*-
# vi: set ft=python sts=4 ts=4 sw=4 noet :

import GeoIP
import requests
import json
from fail2ban.server.actions import ActionBase, CallingMap
# apt-get install geoip-database python3-geoip

class SlackAction(ActionBase):

    def __init__(self, jail, name, hookurl):
        super(SlackAction, self).__init__(jail, name)
        self.jail = jail
        self.name = name
        self.hookurl = hookurl
        self.gi = GeoIP.open("/usr/share/GeoIP/GeoIP.dat", GeoIP.GEOIP_MEMORY_CACHE | GeoIP.GEOIP_CHECK_CACHE)

    def _sendSlack(self, msg):
        payload = {'text': msg}
        r = requests.post(self.hookurl, data=json.dumps(payload))

    def start(self):
        pass

    def stop(self):
        pass

    def ban(self, aInfo):
        ip = aInfo["ip"]
        country = self.gi.country_name_by_addr(ip)
        self._sendSlack("Banned '%s' (%s)" % (ip, country))

    def unban(self, aInfo):
        pass

Action = SlackAction
