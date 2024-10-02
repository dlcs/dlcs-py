import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeliveryChannelPolicy")


@define
class DeliveryChannelPolicy:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        policy_data (Union[Unset, None, str]):
        created (Union[Unset, None, datetime.datetime]):
        modified (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    channel: Union[Unset, None, str] = UNSET
    policy_data: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        customer_id = self.customer_id
        name = self.name
        display_name = self.display_name
        channel = self.channel
        policy_data = self.policy_data
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if context is not UNSET:
            field_dict["context"] = context
        if type is not UNSET:
            field_dict["type"] = type
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if channel is not UNSET:
            field_dict["channel"] = channel
        if policy_data is not UNSET:
            field_dict["policyData"] = policy_data
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        customer_id = d.pop("customerId", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        channel = d.pop("channel", UNSET)

        policy_data = d.pop("policyData", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, None, datetime.datetime]
        if _modified is None:
            modified = None
        elif isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        delivery_channel_policy = cls(
            id=id,
            context=context,
            type=type,
            customer_id=customer_id,
            name=name,
            display_name=display_name,
            channel=channel,
            policy_data=policy_data,
            created=created,
            modified=modified,
        )

        return delivery_channel_policy
