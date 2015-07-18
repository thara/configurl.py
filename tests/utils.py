# -*- coding: utf-8 -*-
import random
import string

__random_string_source = string.ascii_lowercase + string.ascii_uppercase + string.digits


def random_string(n=None):
    if n is None:
        n = random.randint(1, 128)
    return ''.join(random.choice(__random_string_source) for _ in range(n))


def random_port():
    return random.randint(0, 65536)


def create_url_string(scheme, user, password, hostname, port):
    if port is None:
        return "%s://%s:%s@%s" % (scheme, user, password, hostname)
    else:
        return "%s://%s:%s@%s:%s" % (scheme, user, password, hostname, port)

