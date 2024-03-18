"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Optional

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class WifiAccessPoint(BaseModel):
    """
    WifiAccessPoint
    """

    bssid: StrictStr = Field(...)
    ssid: StrictStr = Field(...)
    signal: StrictInt = Field(...)
    frequency: StrictStr = Field(...)
    encrypted: StrictBool = Field(...)
    connected: StrictBool = Field(...)
    error: Optional[StrictStr] = ""
    __properties = [
        "bssid",
        "ssid",
        "signal",
        "frequency",
        "encrypted",
        "connected",
        "error",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> WifiAccessPoint:
        """Create an instance of WifiAccessPoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WifiAccessPoint:
        """Create an instance of WifiAccessPoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WifiAccessPoint.parse_obj(obj)

        _obj = WifiAccessPoint.parse_obj(
            {
                "bssid": obj.get("bssid"),
                "ssid": obj.get("ssid"),
                "signal": obj.get("signal"),
                "frequency": obj.get("frequency"),
                "encrypted": obj.get("encrypted"),
                "connected": obj.get("connected"),
                "error": obj.get("error") if obj.get("error") is not None else "",
            },
        )
        return _obj
