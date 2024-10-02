import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Space")


@define
class Space:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        model_id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        created (Union[Unset, None, datetime.datetime]):
        default_tags (Union[Unset, None, List[str]]):
        max_unauthorised (Union[Unset, None, int]):
        approximate_number_of_images (Union[Unset, None, int]):
        default_roles (Union[Unset, None, List[str]]):
        images (Union[Unset, None, str]):
        default_delivery_channels (Union[Unset, None, str]):
        metadata (Union[Unset, None, str]):
        storage (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    model_id: Union[Unset, None, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    default_tags: Union[Unset, None, List[str]] = UNSET
    max_unauthorised: Union[Unset, None, int] = UNSET
    approximate_number_of_images: Union[Unset, None, int] = UNSET
    default_roles: Union[Unset, None, List[str]] = UNSET
    images: Union[Unset, None, str] = UNSET
    default_delivery_channels: Union[Unset, None, str] = UNSET
    metadata: Union[Unset, None, str] = UNSET
    storage: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        customer_id = self.customer_id
        model_id = self.model_id
        name = self.name
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        default_tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.default_tags, Unset):
            if self.default_tags is None:
                default_tags = None
            else:
                default_tags = self.default_tags

        max_unauthorised = self.max_unauthorised
        approximate_number_of_images = self.approximate_number_of_images
        default_roles: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.default_roles, Unset):
            if self.default_roles is None:
                default_roles = None
            else:
                default_roles = self.default_roles

        images = self.images
        default_delivery_channels = self.default_delivery_channels
        metadata = self.metadata
        storage = self.storage

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
        if model_id is not UNSET:
            field_dict["modelId"] = model_id
        if name is not UNSET:
            field_dict["name"] = name
        if created is not UNSET:
            field_dict["created"] = created
        if default_tags is not UNSET:
            field_dict["defaultTags"] = default_tags
        if max_unauthorised is not UNSET:
            field_dict["maxUnauthorised"] = max_unauthorised
        if approximate_number_of_images is not UNSET:
            field_dict["approximateNumberOfImages"] = approximate_number_of_images
        if default_roles is not UNSET:
            field_dict["defaultRoles"] = default_roles
        if images is not UNSET:
            field_dict["images"] = images
        if default_delivery_channels is not UNSET:
            field_dict["defaultDeliveryChannels"] = default_delivery_channels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if storage is not UNSET:
            field_dict["storage"] = storage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        customer_id = d.pop("customerId", UNSET)

        model_id = d.pop("modelId", UNSET)

        name = d.pop("name", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        default_tags = cast(List[str], d.pop("defaultTags", UNSET))

        max_unauthorised = d.pop("maxUnauthorised", UNSET)

        approximate_number_of_images = d.pop("approximateNumberOfImages", UNSET)

        default_roles = cast(List[str], d.pop("defaultRoles", UNSET))

        images = d.pop("images", UNSET)

        default_delivery_channels = d.pop("defaultDeliveryChannels", UNSET)

        metadata = d.pop("metadata", UNSET)

        storage = d.pop("storage", UNSET)

        space = cls(
            id=id,
            context=context,
            type=type,
            customer_id=customer_id,
            model_id=model_id,
            name=name,
            created=created,
            default_tags=default_tags,
            max_unauthorised=max_unauthorised,
            approximate_number_of_images=approximate_number_of_images,
            default_roles=default_roles,
            images=images,
            default_delivery_channels=default_delivery_channels,
            metadata=metadata,
            storage=storage,
        )

        return space
