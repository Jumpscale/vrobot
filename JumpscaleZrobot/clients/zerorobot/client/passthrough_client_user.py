# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.


class PassThroughClientUser:
    def __init__(self, http_client):
        self._http_client = http_client

    def set_zrobotuser_header(self, val):
        """" Set header ZrobotUser to '<val>'"""
        self._http_client.set_header('Authorization', val)  # for backward compatibility with 0.6.x
        return self._http_client.set_header('ZrobotUser', val)