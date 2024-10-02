from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerQueue")


@define
class CustomerQueue:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        size (Union[Unset, int]):
        batches_waiting (Union[Unset, int]):
        images_waiting (Union[Unset, int]):
        batches (Union[Unset, None, str]):
        images (Union[Unset, None, str]):
        active (Union[Unset, None, str]):
        recent (Union[Unset, None, str]):
        priority (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    size: Union[Unset, int] = UNSET
    batches_waiting: Union[Unset, int] = UNSET
    images_waiting: Union[Unset, int] = UNSET
    batches: Union[Unset, None, str] = UNSET
    images: Union[Unset, None, str] = UNSET
    active: Union[Unset, None, str] = UNSET
    recent: Union[Unset, None, str] = UNSET
    priority: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        customer_id = self.customer_id
        size = self.size
        batches_waiting = self.batches_waiting
        images_waiting = self.images_waiting
        batches = self.batches
        images = self.images
        active = self.active
        recent = self.recent
        priority = self.priority

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
        if size is not UNSET:
            field_dict["size"] = size
        if batches_waiting is not UNSET:
            field_dict["batchesWaiting"] = batches_waiting
        if images_waiting is not UNSET:
            field_dict["imagesWaiting"] = images_waiting
        if batches is not UNSET:
            field_dict["batches"] = batches
        if images is not UNSET:
            field_dict["images"] = images
        if active is not UNSET:
            field_dict["active"] = active
        if recent is not UNSET:
            field_dict["recent"] = recent
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        customer_id = d.pop("customerId", UNSET)

        size = d.pop("size", UNSET)

        batches_waiting = d.pop("batchesWaiting", UNSET)

        images_waiting = d.pop("imagesWaiting", UNSET)

        batches = d.pop("batches", UNSET)

        images = d.pop("images", UNSET)

        active = d.pop("active", UNSET)

        recent = d.pop("recent", UNSET)

        priority = d.pop("priority", UNSET)

        customer_queue = cls(
            id=id,
            context=context,
            type=type,
            customer_id=customer_id,
            size=size,
            batches_waiting=batches_waiting,
            images_waiting=images_waiting,
            batches=batches,
            images=images,
            active=active,
            recent=recent,
            priority=priority,
        )

        return customer_queue
