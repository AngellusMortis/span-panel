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
from typing import Union

import orjson as json
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt

from span_panel.client.models.relay_state import RelayState


class Branch(BaseModel):
    """
    Branch
    """

    id: StrictInt = Field(...)
    relay_state: RelayState = Field(..., alias="relayState")
    instant_power_w: Union[StrictFloat, StrictInt] = Field(..., alias="instantPowerW")
    imported_active_energy_wh: Union[StrictFloat, StrictInt] = Field(
        ..., alias="importedActiveEnergyWh"
    )
    exported_active_energy_wh: Union[StrictFloat, StrictInt] = Field(
        ..., alias="exportedActiveEnergyWh"
    )
    measure_start_ts_ms: StrictInt = Field(..., alias="measureStartTsMs")
    measure_duration_ms: StrictInt = Field(..., alias="measureDurationMs")
    is_measure_valid: StrictBool = Field(..., alias="isMeasureValid")
    __properties = [
        "id",
        "relayState",
        "instantPowerW",
        "importedActiveEnergyWh",
        "exportedActiveEnergyWh",
        "measureStartTsMs",
        "measureDurationMs",
        "isMeasureValid",
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
    def from_json(cls, json_str: str) -> Branch:
        """Create an instance of Branch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Branch:
        """Create an instance of Branch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Branch.parse_obj(obj)

        _obj = Branch.parse_obj(
            {
                "id": obj.get("id"),
                "relay_state": obj.get("relayState"),
                "instant_power_w": obj.get("instantPowerW"),
                "imported_active_energy_wh": obj.get("importedActiveEnergyWh"),
                "exported_active_energy_wh": obj.get("exportedActiveEnergyWh"),
                "measure_start_ts_ms": obj.get("measureStartTsMs"),
                "measure_duration_ms": obj.get("measureDurationMs"),
                "is_measure_valid": obj.get("isMeasureValid"),
            }
        )
        return _obj
