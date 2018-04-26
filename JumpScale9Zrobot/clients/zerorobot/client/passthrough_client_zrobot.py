# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.


class PassThroughClientZrobot:
    def __init__(self, http_client):
        self._http_client = http_client

    def set_authorization_header(self, val):
        """" Set header Authorization to '<val>'"""
        return self._http_client.set_header('Zrobot', val)
