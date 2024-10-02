from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultDeliveryChannel")


@define
class DefaultDeliveryChannel:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        policy (Union[Unset, None, str]):
        media_type (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    channel: Union[Unset, None, str] = UNSET
    policy: Union[Unset, None, str] = UNSET
    media_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        channel = self.channel
        policy = self.policy
        media_type = self.media_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if context is not UNSET:
            field_dict["context"] = context
        if type is not UNSET:
            field_dict["type"] = type
        if channel is not UNSET:
            field_dict["channel"] = channel
        if policy is not UNSET:
            field_dict["policy"] = policy
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        channel = d.pop("channel", UNSET)

        policy = d.pop("policy", UNSET)

        media_type = d.pop("mediaType", UNSET)

        default_delivery_channel = cls(
            id=id,
            context=context,
            type=type,
            channel=channel,
            policy=policy,
            media_type=media_type,
        )

        return default_delivery_channel
