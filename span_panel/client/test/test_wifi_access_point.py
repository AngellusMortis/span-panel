"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import unittest

from span_panel.client.models.wifi_access_point import WifiAccessPoint


class TestWifiAccessPoint(unittest.TestCase):
    """WifiAccessPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WifiAccessPoint:
        """Test WifiAccessPoint
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `WifiAccessPoint`
        """
        model = WifiAccessPoint()  # noqa: E501
        if include_optional:
            return WifiAccessPoint(
                bssid = '',
                ssid = '',
                signal = 56,
                frequency = '',
                encrypted = True,
                connected = True,
                error = ''
            )
        else:
            return WifiAccessPoint(
                bssid = '',
                ssid = '',
                signal = 56,
                frequency = '',
                encrypted = True,
                connected = True,
        )
        """

    def testWifiAccessPoint(self):
        """Test WifiAccessPoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
