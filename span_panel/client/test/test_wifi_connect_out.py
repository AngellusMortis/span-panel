"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import unittest

from span_panel.client.models.wifi_connect_out import WifiConnectOut


class TestWifiConnectOut(unittest.TestCase):
    """WifiConnectOut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WifiConnectOut:
        """Test WifiConnectOut
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `WifiConnectOut`
        """
        model = WifiConnectOut()  # noqa: E501
        if include_optional:
            return WifiConnectOut(
                bssid = '',
                ssid = '',
                signal = 56,
                encrypted = True,
                connected = True,
                error = ''
            )
        else:
            return WifiConnectOut(
                bssid = '',
                ssid = '',
                signal = 56,
                encrypted = True,
                connected = True,
                error = '',
        )
        """

    def testWifiConnectOut(self):
        """Test WifiConnectOut"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
