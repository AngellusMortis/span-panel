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
from typing import List, Optional, Union

import orjson as json

try:
    from pydantic.v1 import (
        BaseModel,
        Field,
        StrictBool,
        StrictFloat,
        StrictInt,
        StrictStr,
        conlist,
    )
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist  # type: ignore[assignment]

from span_panel.client.models.priority import Priority
from span_panel.client.models.relay_state import RelayState


class Circuit(BaseModel):
    """
    Circuit
    """

    id: StrictStr = Field(...)
    name: Optional[StrictStr] = None
    relay_state: RelayState = Field(..., alias="relayState")
    instant_power_w: Union[StrictFloat, StrictInt] = Field(..., alias="instantPowerW")
    instant_power_update_time_s: StrictInt = Field(..., alias="instantPowerUpdateTimeS")
    produced_energy_wh: Union[StrictFloat, StrictInt] = Field(
        ..., alias="producedEnergyWh"
    )
    consumed_energy_wh: Union[StrictFloat, StrictInt] = Field(
        ..., alias="consumedEnergyWh"
    )
    energy_accum_update_time_s: StrictInt = Field(..., alias="energyAccumUpdateTimeS")
    tabs: Optional[conlist(StrictInt)] = None
    priority: Priority = Field(...)
    is_user_controllable: StrictBool = Field(..., alias="isUserControllable")
    is_sheddable: StrictBool = Field(..., alias="isSheddable")
    is_never_backup: StrictBool = Field(..., alias="isNeverBackup")
    __properties = [
        "id",
        "name",
        "relayState",
        "instantPowerW",
        "instantPowerUpdateTimeS",
        "producedEnergyWh",
        "consumedEnergyWh",
        "energyAccumUpdateTimeS",
        "tabs",
        "priority",
        "isUserControllable",
        "isSheddable",
        "isNeverBackup",
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
    def from_json(cls, json_str: str) -> Circuit:
        """Create an instance of Circuit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Circuit:
        """Create an instance of Circuit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Circuit.parse_obj(obj)

        _obj = Circuit.parse_obj(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "relay_state": obj.get("relayState"),
                "instant_power_w": obj.get("instantPowerW"),
                "instant_power_update_time_s": obj.get("instantPowerUpdateTimeS"),
                "produced_energy_wh": obj.get("producedEnergyWh"),
                "consumed_energy_wh": obj.get("consumedEnergyWh"),
                "energy_accum_update_time_s": obj.get("energyAccumUpdateTimeS"),
                "tabs": obj.get("tabs"),
                "priority": obj.get("priority"),
                "is_user_controllable": obj.get("isUserControllable"),
                "is_sheddable": obj.get("isSheddable"),
                "is_never_backup": obj.get("isNeverBackup"),
            }
        )
        return _obj
