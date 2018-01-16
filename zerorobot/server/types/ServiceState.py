# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for ServiceState
"""
from .EnumServiceStateState import EnumServiceStateState
from six import string_types

from . import client_support


class ServiceState(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type category: string_types
        :type state: EnumServiceStateState
        :type tag: string_types
        :rtype: ServiceState
        """

        return ServiceState(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'ServiceState'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.category = client_support.set_property('category', data, data_types, False, [], False, True, class_name)
        data_types = [EnumServiceStateState]
        self.state = client_support.set_property('state', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.tag = client_support.set_property('tag', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
