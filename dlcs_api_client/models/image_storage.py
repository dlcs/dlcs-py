import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageStorage")


@define
class ImageStorage:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        space_id (Union[Unset, int]):
        thumbnail_size (Union[Unset, int]):
        size (Union[Unset, int]):
        last_checked (Union[Unset, None, datetime.datetime]):
        checking_in_progress (Union[Unset, bool]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    space_id: Union[Unset, int] = UNSET
    thumbnail_size: Union[Unset, int] = UNSET
    size: Union[Unset, int] = UNSET
    last_checked: Union[Unset, None, datetime.datetime] = UNSET
    checking_in_progress: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        customer_id = self.customer_id
        space_id = self.space_id
        thumbnail_size = self.thumbnail_size
        size = self.size
        last_checked: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_checked, Unset):
            last_checked = self.last_checked.isoformat() if self.last_checked else None

        checking_in_progress = self.checking_in_progress

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
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id
        if thumbnail_size is not UNSET:
            field_dict["thumbnailSize"] = thumbnail_size
        if size is not UNSET:
            field_dict["size"] = size
        if last_checked is not UNSET:
            field_dict["lastChecked"] = last_checked
        if checking_in_progress is not UNSET:
            field_dict["checkingInProgress"] = checking_in_progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        space_id = d.pop("spaceId", UNSET)

        thumbnail_size = d.pop("thumbnailSize", UNSET)

        size = d.pop("size", UNSET)

        _last_checked = d.pop("lastChecked", UNSET)
        last_checked: Union[Unset, None, datetime.datetime]
        if _last_checked is None:
            last_checked = None
        elif isinstance(_last_checked, Unset):
            last_checked = UNSET
        else:
            last_checked = isoparse(_last_checked)

        checking_in_progress = d.pop("checkingInProgress", UNSET)

        image_storage = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            customer_id=customer_id,
            space_id=space_id,
            thumbnail_size=thumbnail_size,
            size=size,
            last_checked=last_checked,
            checking_in_progress=checking_in_progress,
        )

        return image_storage
