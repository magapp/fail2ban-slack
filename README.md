# fail2ban-slack

This is an action for fail2ban that notify Slack which IP and country the IP belongs to that was banned.

Install with these steps:

* Copy slack.py to /etc/fail2ban/action.d.
* Setup an incoming web hook on you Slack account and remeber the URL.
* In a jail, type something like this, replace slack hook with the URL from step 2.

```[wordpress]
enabled = true
filter = wordpress
port = http,https
logpath = /var/log/apache2/access.log
action = slack.py[hookurl="https://hooks.slack.com/services/T040xxxxx/xxxxxxxxxx/xxxxxxxxx"]
```

Banned IP adresses will now show up on slack togheter with the country the IP originates from.

NOTE:
This plugin depends on a couple of Python modules and is only tested on Ubuntu. You need fail2ban version 0.9.0 or newer. On Ubuntu, install the module with this:

	apt-get install geoip-database python3-geoip
