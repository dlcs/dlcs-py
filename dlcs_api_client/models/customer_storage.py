import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerStorage")


@define
class CustomerStorage:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        space_id (Union[Unset, None, int]):
        number_of_stored_images (Union[Unset, None, int]):
        total_size_of_stored_images (Union[Unset, None, int]):
        total_size_of_thumbnails (Union[Unset, None, int]):
        last_calculated (Union[Unset, None, datetime.datetime]):
        storage_policy (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    space_id: Union[Unset, None, int] = UNSET
    number_of_stored_images: Union[Unset, None, int] = UNSET
    total_size_of_stored_images: Union[Unset, None, int] = UNSET
    total_size_of_thumbnails: Union[Unset, None, int] = UNSET
    last_calculated: Union[Unset, None, datetime.datetime] = UNSET
    storage_policy: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        customer_id = self.customer_id
        space_id = self.space_id
        number_of_stored_images = self.number_of_stored_images
        total_size_of_stored_images = self.total_size_of_stored_images
        total_size_of_thumbnails = self.total_size_of_thumbnails
        last_calculated: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_calculated, Unset):
            last_calculated = self.last_calculated.isoformat() if self.last_calculated else None

        storage_policy = self.storage_policy

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
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id
        if number_of_stored_images is not UNSET:
            field_dict["numberOfStoredImages"] = number_of_stored_images
        if total_size_of_stored_images is not UNSET:
            field_dict["totalSizeOfStoredImages"] = total_size_of_stored_images
        if total_size_of_thumbnails is not UNSET:
            field_dict["totalSizeOfThumbnails"] = total_size_of_thumbnails
        if last_calculated is not UNSET:
            field_dict["lastCalculated"] = last_calculated
        if storage_policy is not UNSET:
            field_dict["storagePolicy"] = storage_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        customer_id = d.pop("customerId", UNSET)

        space_id = d.pop("spaceId", UNSET)

        number_of_stored_images = d.pop("numberOfStoredImages", UNSET)

        total_size_of_stored_images = d.pop("totalSizeOfStoredImages", UNSET)

        total_size_of_thumbnails = d.pop("totalSizeOfThumbnails", UNSET)

        _last_calculated = d.pop("lastCalculated", UNSET)
        last_calculated: Union[Unset, None, datetime.datetime]
        if _last_calculated is None:
            last_calculated = None
        elif isinstance(_last_calculated, Unset):
            last_calculated = UNSET
        else:
            last_calculated = isoparse(_last_calculated)

        storage_policy = d.pop("storagePolicy", UNSET)

        customer_storage = cls(
            id=id,
            context=context,
            type=type,
            customer_id=customer_id,
            space_id=space_id,
            number_of_stored_images=number_of_stored_images,
            total_size_of_stored_images=total_size_of_stored_images,
            total_size_of_thumbnails=total_size_of_thumbnails,
            last_calculated=last_calculated,
            storage_policy=storage_policy,
        )

        return customer_storage
