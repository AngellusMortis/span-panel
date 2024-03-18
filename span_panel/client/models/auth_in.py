# coding: utf-8

"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
import re  # noqa: F401
from typing import Optional

import orjson as json
from pydantic import BaseModel, Field, StrictStr


class AuthIn(BaseModel):
    """
    AuthIn
    """

    name: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    otp: Optional[StrictStr] = None
    dashboard_password: Optional[StrictStr] = Field(None, alias="dashboardPassword")
    __properties = ["name", "description", "otp", "dashboardPassword"]

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
    def from_json(cls, json_str: str) -> AuthIn:
        """Create an instance of AuthIn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthIn:
        """Create an instance of AuthIn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthIn.parse_obj(obj)

        _obj = AuthIn.parse_obj(
            {
                "name": obj.get("name"),
                "description": obj.get("description"),
                "otp": obj.get("otp"),
                "dashboard_password": obj.get("dashboardPassword"),
            }
        )
        return _obj
