from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NamedQuery")


@define
class NamedQuery:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        global_ (Union[Unset, None, bool]):
        template (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    global_: Union[Unset, None, bool] = UNSET
    template: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        customer_id = self.customer_id
        name = self.name
        global_ = self.global_
        template = self.template

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
        if name is not UNSET:
            field_dict["name"] = name
        if global_ is not UNSET:
            field_dict["global"] = global_
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        name = d.pop("name", UNSET)

        global_ = d.pop("global", UNSET)

        template = d.pop("template", UNSET)

        named_query = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            customer_id=customer_id,
            name=name,
            global_=global_,
            template=template,
        )

        return named_query
