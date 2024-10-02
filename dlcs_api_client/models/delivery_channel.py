from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeliveryChannel")


@define
class DeliveryChannel:
    """
    Attributes:
        id (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        policy (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    channel: Union[Unset, None, str] = UNSET
    policy: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        context = self.context
        channel = self.channel
        policy = self.policy

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if context is not UNSET:
            field_dict["context"] = context
        if channel is not UNSET:
            field_dict["channel"] = channel
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        context = d.pop("context", UNSET)

        channel = d.pop("channel", UNSET)

        policy = d.pop("policy", UNSET)

        delivery_channel = cls(
            id=id,
            type=type,
            context=context,
            channel=channel,
            policy=policy,
        )

        return delivery_channel
