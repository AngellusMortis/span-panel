"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import unittest

from span_panel.client.models.priority_in import PriorityIn


class TestPriorityIn(unittest.TestCase):
    """PriorityIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriorityIn:
        """Test PriorityIn
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PriorityIn`
        """
        model = PriorityIn()  # noqa: E501
        if include_optional:
            return PriorityIn(
                priority = 'UNKNOWN'
            )
        else:
            return PriorityIn(
                priority = 'UNKNOWN',
        )
        """

    def testPriorityIn(self):
        """Test PriorityIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
