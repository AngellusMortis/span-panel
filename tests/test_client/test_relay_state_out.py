# coding: utf-8

"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import datetime
import unittest

from span_panel.client.models.relay_state_out import RelayStateOut  # noqa: E501


class TestRelayStateOut(unittest.TestCase):
    """RelayStateOut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelayStateOut:
        """Test RelayStateOut
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RelayStateOut`
        """
        model = RelayStateOut()  # noqa: E501
        if include_optional:
            return RelayStateOut(
                relay_state = ''
            )
        else:
            return RelayStateOut(
                relay_state = '',
        )
        """

    def testRelayStateOut(self):
        """Test RelayStateOut"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
