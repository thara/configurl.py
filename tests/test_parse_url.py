# -*- coding: utf-8 -*-
import pytest

import configurl

from .utils import create_url_string, random_string


def test_parse(url_string, scheme, user, password, hostname, port):
    expected = {
        "SCHEME": scheme.lower(),
        "USER": user,
        "PASSWORD": password,
        "HOST": hostname.lower(),
        "PORT": port,
    }

    result = configurl.parse(url_string)
    assert result == expected


class TestWithEmptyScheme:
    """ case of empty scheme """

    @pytest.fixture()
    def scheme(self):
        return ""

    def test_raise_exception(self, url_string):
        with pytest.raises(configurl.Error):
            configurl.parse(url_string)


class TestWithEmptyHostname:
    """ case of empty hostname """
    @pytest.fixture()
    def hostname(self):
        return ""

    def test_raise_exception(self, url_string):
        with pytest.raises(configurl.Error):
            configurl.parse(url_string)


class TestWithEmptyPortNumber:
    """ case of empty port number """

    @pytest.fixture()
    def port(self):
        return ""

    def test_success_with_empty_port_number(self, url_string):
        setting = configurl.parse(url_string)
        assert setting["PORT"] == ''

