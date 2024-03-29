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

try:
    from pydantic.v1 import BaseModel, Field
except ImportError:
    from pydantic import BaseModel, Field  # type: ignore[assignment]

from span_panel.client.models.boolean_in import BooleanIn
from span_panel.client.models.circuit_name_in import CircuitNameIn
from span_panel.client.models.priority_in import PriorityIn
from span_panel.client.models.relay_state_in import RelayStateIn


class BodySetCircuitStateApiV1CircuitsCircuitIdPost(BaseModel):
    """
    BodySetCircuitStateApiV1CircuitsCircuitIdPost
    """

    relay_state_in: Optional[RelayStateIn] = Field(None, alias="relayStateIn")
    priority_in: Optional[PriorityIn] = Field(None, alias="priorityIn")
    circuit_name_in: Optional[CircuitNameIn] = Field(None, alias="circuitNameIn")
    user_controllable_in: Optional[BooleanIn] = Field(None, alias="userControllableIn")
    sheddable_in: Optional[BooleanIn] = Field(None, alias="sheddableIn")
    never_backup_in: Optional[BooleanIn] = Field(None, alias="neverBackupIn")
    __properties = [
        "relayStateIn",
        "priorityIn",
        "circuitNameIn",
        "userControllableIn",
        "sheddableIn",
        "neverBackupIn",
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
    def from_json(cls, json_str: str) -> BodySetCircuitStateApiV1CircuitsCircuitIdPost:
        """Create an instance of BodySetCircuitStateApiV1CircuitsCircuitIdPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of relay_state_in
        if self.relay_state_in:
            _dict["relayStateIn"] = self.relay_state_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority_in
        if self.priority_in:
            _dict["priorityIn"] = self.priority_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of circuit_name_in
        if self.circuit_name_in:
            _dict["circuitNameIn"] = self.circuit_name_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_controllable_in
        if self.user_controllable_in:
            _dict["userControllableIn"] = self.user_controllable_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sheddable_in
        if self.sheddable_in:
            _dict["sheddableIn"] = self.sheddable_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of never_backup_in
        if self.never_backup_in:
            _dict["neverBackupIn"] = self.never_backup_in.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BodySetCircuitStateApiV1CircuitsCircuitIdPost:
        """Create an instance of BodySetCircuitStateApiV1CircuitsCircuitIdPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BodySetCircuitStateApiV1CircuitsCircuitIdPost.parse_obj(obj)

        _obj = BodySetCircuitStateApiV1CircuitsCircuitIdPost.parse_obj(
            {
                "relay_state_in": (
                    RelayStateIn.from_dict(obj.get("relayStateIn"))
                    if obj.get("relayStateIn") is not None
                    else None
                ),
                "priority_in": (
                    PriorityIn.from_dict(obj.get("priorityIn"))
                    if obj.get("priorityIn") is not None
                    else None
                ),
                "circuit_name_in": (
                    CircuitNameIn.from_dict(obj.get("circuitNameIn"))
                    if obj.get("circuitNameIn") is not None
                    else None
                ),
                "user_controllable_in": (
                    BooleanIn.from_dict(obj.get("userControllableIn"))
                    if obj.get("userControllableIn") is not None
                    else None
                ),
                "sheddable_in": (
                    BooleanIn.from_dict(obj.get("sheddableIn"))
                    if obj.get("sheddableIn") is not None
                    else None
                ),
                "never_backup_in": (
                    BooleanIn.from_dict(obj.get("neverBackupIn"))
                    if obj.get("neverBackupIn") is not None
                    else None
                ),
            }
        )
        return _obj
