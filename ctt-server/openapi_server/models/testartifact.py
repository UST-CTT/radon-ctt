# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.policy_test import PolicyTest
from openapi_server import util

from openapi_server.models.policy_test import PolicyTest  # noqa: E501

class Testartifact(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, policy_tests=None, project_id=None, status=None):  # noqa: E501
        """Testartifact - a model defined in OpenAPI

        :param id: The id of this Testartifact.  # noqa: E501
        :type id: int
        :param policy_tests: The policy_tests of this Testartifact.  # noqa: E501
        :type policy_tests: List[PolicyTest]
        :param project_id: The project_id of this Testartifact.  # noqa: E501
        :type project_id: int
        :param status: The status of this Testartifact.  # noqa: E501
        :type status: str
        """
        self.openapi_types = {
            'id': int,
            'policy_tests': List[PolicyTest],
            'project_id': int,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'policy_tests': 'policyTests',
            'project_id': 'projectId',
            'status': 'status'
        }

        self._id = id
        self._policy_tests = policy_tests
        self._project_id = project_id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Testartifact':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Testartifact of this Testartifact.  # noqa: E501
        :rtype: Testartifact
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Testartifact.


        :return: The id of this Testartifact.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Testartifact.


        :param id: The id of this Testartifact.
        :type id: int
        """

        self._id = id

    @property
    def policy_tests(self):
        """Gets the policy_tests of this Testartifact.


        :return: The policy_tests of this Testartifact.
        :rtype: List[PolicyTest]
        """
        return self._policy_tests

    @policy_tests.setter
    def policy_tests(self, policy_tests):
        """Sets the policy_tests of this Testartifact.


        :param policy_tests: The policy_tests of this Testartifact.
        :type policy_tests: List[PolicyTest]
        """

        self._policy_tests = policy_tests

    @property
    def project_id(self):
        """Gets the project_id of this Testartifact.


        :return: The project_id of this Testartifact.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Testartifact.


        :param project_id: The project_id of this Testartifact.
        :type project_id: int
        """

        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this Testartifact.


        :return: The status of this Testartifact.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Testartifact.


        :param status: The status of this Testartifact.
        :type status: str
        """

        self._status = status
