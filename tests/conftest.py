# -*- coding: utf-8 -*-
import pytest

from . import utils


@pytest.fixture()
def scheme():
    return utils.random_string()


@pytest.fixture()
def user():
    return utils.random_string()


@pytest.fixture()
def password():
    return utils.random_string()


@pytest.fixture()
def hostname():
    return utils.random_string()


@pytest.fixture()
def port():
    return utils.random_port()


@pytest.fixture()
def url_string(scheme, user, password, hostname, port):
    return utils.create_url_string(scheme, user, password, hostname, port)
