# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SourceRepository(Model):
    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'identifier': {'key': 'id', 'type': 'str'},
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'authorization_info': {'key': 'authorizationInfo', 'type': 'AuthorizationInfo'},
    }

    def __init__(self, type=None, identifier=None, default_branch=None, authorization_info = None):
        self.type = type
        self.identifier = identifier
        self.default_branch = default_branch
        self.authorization_info = authorization_info
