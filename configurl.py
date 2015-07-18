# -*- coding: utf-8 -*-

__version__ = "0.0.1"

from urllib import parse as urlparse


def parse(url):
    """ Parse a config URL. """
    parsed = urlparse.urlparse(url)

    if len(parsed.scheme) <= 0:
        raise Error("scheme is empty in url.")

    if parsed.hostname is None:
        raise Error("hostname is emtpy in url.")

    config = {
        "SCHEME": parsed.scheme,
        "USER": parsed.username or '',
        "PASSWORD": parsed.password or '',
        "HOST": parsed.hostname,
        "PORT": parsed.port or '',
    }

    return config


class Error(Exception):
    """ Exception from configurl """
