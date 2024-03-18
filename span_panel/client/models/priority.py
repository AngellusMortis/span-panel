"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import json
import re  # noqa: F401

from aenum import Enum


class Priority(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    UNKNOWN = "UNKNOWN"
    NON_ESSENTIAL = "NON_ESSENTIAL"
    NICE_TO_HAVE = "NICE_TO_HAVE"
    MUST_HAVE = "MUST_HAVE"

    @classmethod
    def from_json(cls, json_str: str) -> Priority:
        """Create an instance of Priority from a JSON string"""
        return Priority(json.loads(json_str))
