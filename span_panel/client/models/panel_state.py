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
from typing import Union

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

from span_panel.client.models.branch import Branch
from span_panel.client.models.feedthrough_energy import FeedthroughEnergy
from span_panel.client.models.main_meter_energy import MainMeterEnergy
from span_panel.client.models.relay_state import RelayState


class PanelState(BaseModel):
    """
    PanelState
    """

    main_relay_state: RelayState = Field(..., alias="mainRelayState")
    main_meter_energy: MainMeterEnergy = Field(..., alias="mainMeterEnergy")
    instant_grid_power_w: Union[StrictFloat, StrictInt] = Field(
        ...,
        alias="instantGridPowerW",
    )
    feedthrough_power_w: Union[StrictFloat, StrictInt] = Field(
        ...,
        alias="feedthroughPowerW",
    )
    feedthrough_energy: FeedthroughEnergy = Field(..., alias="feedthroughEnergy")
    grid_sample_start_ms: StrictInt = Field(..., alias="gridSampleStartMs")
    grid_sample_end_ms: StrictInt = Field(..., alias="gridSampleEndMs")
    dsm_grid_state: StrictStr = Field(..., alias="dsmGridState")
    dsm_state: StrictStr = Field(..., alias="dsmState")
    current_run_config: StrictStr = Field(..., alias="currentRunConfig")
    branches: conlist(Branch) = Field(...)
    __properties = [
        "mainRelayState",
        "mainMeterEnergy",
        "instantGridPowerW",
        "feedthroughPowerW",
        "feedthroughEnergy",
        "gridSampleStartMs",
        "gridSampleEndMs",
        "dsmGridState",
        "dsmState",
        "currentRunConfig",
        "branches",
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
    def from_json(cls, json_str: str) -> PanelState:
        """Create an instance of PanelState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of main_meter_energy
        if self.main_meter_energy:
            _dict["mainMeterEnergy"] = self.main_meter_energy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feedthrough_energy
        if self.feedthrough_energy:
            _dict["feedthroughEnergy"] = self.feedthrough_energy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in branches (list)
        _items = []
        if self.branches:
            for _item in self.branches:
                if _item:
                    _items.append(_item.to_dict())
            _dict["branches"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PanelState:
        """Create an instance of PanelState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PanelState.parse_obj(obj)

        _obj = PanelState.parse_obj(
            {
                "main_relay_state": obj.get("mainRelayState"),
                "main_meter_energy": (
                    MainMeterEnergy.from_dict(obj.get("mainMeterEnergy"))
                    if obj.get("mainMeterEnergy") is not None
                    else None
                ),
                "instant_grid_power_w": obj.get("instantGridPowerW"),
                "feedthrough_power_w": obj.get("feedthroughPowerW"),
                "feedthrough_energy": (
                    FeedthroughEnergy.from_dict(obj.get("feedthroughEnergy"))
                    if obj.get("feedthroughEnergy") is not None
                    else None
                ),
                "grid_sample_start_ms": obj.get("gridSampleStartMs"),
                "grid_sample_end_ms": obj.get("gridSampleEndMs"),
                "dsm_grid_state": obj.get("dsmGridState"),
                "dsm_state": obj.get("dsmState"),
                "current_run_config": obj.get("currentRunConfig"),
                "branches": (
                    [Branch.from_dict(_item) for _item in obj.get("branches")]
                    if obj.get("branches") is not None
                    else None
                ),
            },
        )
        return _obj
