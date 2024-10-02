from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomHeader")


@define
class CustomHeader:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        role (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
        space_id (Union[Unset, None, int]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    role: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    space_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        customer_id = self.customer_id
        role = self.role
        key = self.key
        value = self.value
        space_id = self.space_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if context is not UNSET:
            field_dict["context"] = context
        if type is not UNSET:
            field_dict["type"] = type
        if model_id is not UNSET:
            field_dict["modelId"] = model_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if role is not UNSET:
            field_dict["role"] = role
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        role = d.pop("role", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        space_id = d.pop("spaceId", UNSET)

        custom_header = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            customer_id=customer_id,
            role=role,
            key=key,
            value=value,
            space_id=space_id,
        )

        return custom_header
