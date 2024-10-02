from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKey")


@define
class ApiKey:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        key (Union[Unset, None, str]):
        secret (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    key: Union[Unset, None, str] = UNSET
    secret: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        customer_id = self.customer_id
        key = self.key
        secret = self.secret
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if context is not UNSET:
            field_dict["context"] = context
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if key is not UNSET:
            field_dict["key"] = key
        if secret is not UNSET:
            field_dict["secret"] = secret
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        customer_id = d.pop("customerId", UNSET)

        key = d.pop("key", UNSET)

        secret = d.pop("secret", UNSET)

        type = d.pop("type", UNSET)

        api_key = cls(
            id=id,
            context=context,
            customer_id=customer_id,
            key=key,
            secret=secret,
            type=type,
        )

        return api_key
