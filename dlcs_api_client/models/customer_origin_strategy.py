from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerOriginStrategy")


@define
class CustomerOriginStrategy:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        regex (Union[Unset, None, str]):
        origin_strategy (Union[Unset, None, str]):
        credentials (Union[Unset, None, str]):
        optimised (Union[Unset, None, bool]):
        order (Union[Unset, None, int]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    regex: Union[Unset, None, str] = UNSET
    origin_strategy: Union[Unset, None, str] = UNSET
    credentials: Union[Unset, None, str] = UNSET
    optimised: Union[Unset, None, bool] = UNSET
    order: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        customer_id = self.customer_id
        regex = self.regex
        origin_strategy = self.origin_strategy
        credentials = self.credentials
        optimised = self.optimised
        order = self.order

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
        if regex is not UNSET:
            field_dict["regex"] = regex
        if origin_strategy is not UNSET:
            field_dict["originStrategy"] = origin_strategy
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if optimised is not UNSET:
            field_dict["optimised"] = optimised
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        regex = d.pop("regex", UNSET)

        origin_strategy = d.pop("originStrategy", UNSET)

        credentials = d.pop("credentials", UNSET)

        optimised = d.pop("optimised", UNSET)

        order = d.pop("order", UNSET)

        customer_origin_strategy = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            customer_id=customer_id,
            regex=regex,
            origin_strategy=origin_strategy,
            credentials=credentials,
            optimised=optimised,
            order=order,
        )

        return customer_origin_strategy
