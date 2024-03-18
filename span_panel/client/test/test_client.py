"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import unittest

from span_panel.client.models.client import Client


class TestClient(unittest.TestCase):
    """Client unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Client:
        """Test Client
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Client`
        """
        model = Client()  # noqa: E501
        if include_optional:
            return Client(
                description = '',
                issued_at = 56,
                allowed_endpoint_groups = span_panel.client.models.allowed_endpoint_groups.AllowedEndpointGroups(
                    delete = [
                        ''
                        ], 
                    get = [
                        ''
                        ], 
                    post = [
                        ''
                        ], 
                    push = [
                        ''
                        ], )
            )
        else:
            return Client(
                allowed_endpoint_groups = span_panel.client.models.allowed_endpoint_groups.AllowedEndpointGroups(
                    delete = [
                        ''
                        ], 
                    get = [
                        ''
                        ], 
                    post = [
                        ''
                        ], 
                    push = [
                        ''
                        ], ),
        )
        """

    def testClient(self):
        """Test Client"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
