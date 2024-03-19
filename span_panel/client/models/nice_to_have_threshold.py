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
from pydantic import BaseModel

from span_panel.client.models.state_of_energy import StateOfEnergy


class NiceToHaveThreshold(BaseModel):
    """
    NiceToHaveThreshold
    """

    nice_to_have_threshold_low_soe: Optional[StateOfEnergy] = None
    nice_to_have_threshold_high_soe: Optional[StateOfEnergy] = None
    __properties = ["nice_to_have_threshold_low_soe", "nice_to_have_threshold_high_soe"]

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
    def from_json(cls, json_str: str) -> NiceToHaveThreshold:
        """Create an instance of NiceToHaveThreshold from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of nice_to_have_threshold_low_soe
        if self.nice_to_have_threshold_low_soe:
            _dict["nice_to_have_threshold_low_soe"] = (
                self.nice_to_have_threshold_low_soe.to_dict()
            )
        # override the default output from pydantic by calling `to_dict()` of nice_to_have_threshold_high_soe
        if self.nice_to_have_threshold_high_soe:
            _dict["nice_to_have_threshold_high_soe"] = (
                self.nice_to_have_threshold_high_soe.to_dict()
            )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NiceToHaveThreshold:
        """Create an instance of NiceToHaveThreshold from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NiceToHaveThreshold.parse_obj(obj)

        _obj = NiceToHaveThreshold.parse_obj(
            {
                "nice_to_have_threshold_low_soe": (
                    StateOfEnergy.from_dict(obj.get("nice_to_have_threshold_low_soe"))
                    if obj.get("nice_to_have_threshold_low_soe") is not None
                    else None
                ),
                "nice_to_have_threshold_high_soe": (
                    StateOfEnergy.from_dict(obj.get("nice_to_have_threshold_high_soe"))
                    if obj.get("nice_to_have_threshold_high_soe") is not None
                    else None
                ),
            }
        )
        return _obj