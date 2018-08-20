# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for Eco
"""
from six import string_types

from . import client_support


class Eco(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type cat: string_types
        :type count: int
        :type message: string_types
        :type message_pub: string_types
        :type time_first: int
        :type time_last: int
        :type trace: string_types
        :rtype: Eco
        """

        return Eco(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Eco'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.cat = client_support.set_property('cat', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.count = client_support.set_property('count', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.message = client_support.set_property('message', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.message_pub = client_support.set_property(
            'message_pub', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.time_first = client_support.set_property(
            'time_first', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.time_last = client_support.set_property('time_last', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.trace = client_support.set_property('trace', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
