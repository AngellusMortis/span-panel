"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import unittest

from span_panel.client.models.state_of_energy import StateOfEnergy


class TestStateOfEnergy(unittest.TestCase):
    """StateOfEnergy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StateOfEnergy:
        """Test StateOfEnergy
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `StateOfEnergy`
        """
        model = StateOfEnergy()  # noqa: E501
        if include_optional:
            return StateOfEnergy(
                percentage = 56
            )
        else:
            return StateOfEnergy(
        )
        """

    def testStateOfEnergy(self):
        """Test StateOfEnergy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
