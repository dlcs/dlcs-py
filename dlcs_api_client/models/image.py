import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define
from dateutil.parser import isoparse

from ..models.asset_family import AssetFamily
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_channel import DeliveryChannel


T = TypeVar("T", bound="Image")


@define
class Image:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        storage_identifier (Union[Unset, None, str]):
        model_id (Union[Unset, None, str]):
        space (Union[Unset, int]):
        image_service (Union[Unset, None, str]):
        degraded_info_json (Union[Unset, None, str]):
        thumbnail_image_service (Union[Unset, None, str]):
        thumbnail400 (Union[Unset, None, str]):
        created (Union[Unset, None, datetime.datetime]):
        origin (Union[Unset, None, str]):
        max_unauthorised (Union[Unset, None, int]):
        queued (Union[Unset, None, datetime.datetime]):
        dequeued (Union[Unset, None, datetime.datetime]):
        finished (Union[Unset, None, datetime.datetime]):
        ingesting (Union[Unset, None, bool]):
        error (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        string1 (Union[Unset, None, str]):
        string2 (Union[Unset, None, str]):
        string3 (Union[Unset, None, str]):
        number1 (Union[Unset, None, int]):
        number2 (Union[Unset, None, int]):
        number3 (Union[Unset, None, int]):
        duration (Union[Unset, None, int]):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        metadata (Union[Unset, None, str]):
        storage (Union[Unset, None, str]):
        media_type (Union[Unset, None, str]):
        family (Union[Unset, AssetFamily]):
        text (Union[Unset, None, str]):
        text_type (Union[Unset, None, str]):
        delivery_channels (Union[Unset, None, List['DeliveryChannel']]):
        roles (Union[Unset, None, List[str]]):
        batch (Union[Unset, None, str]):
        image_optimisation_policy (Union[Unset, None, str]):
        thumbnail_policy (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    storage_identifier: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, None, str] = UNSET
    space: Union[Unset, int] = UNSET
    image_service: Union[Unset, None, str] = UNSET
    degraded_info_json: Union[Unset, None, str] = UNSET
    thumbnail_image_service: Union[Unset, None, str] = UNSET
    thumbnail400: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    origin: Union[Unset, None, str] = UNSET
    max_unauthorised: Union[Unset, None, int] = UNSET
    queued: Union[Unset, None, datetime.datetime] = UNSET
    dequeued: Union[Unset, None, datetime.datetime] = UNSET
    finished: Union[Unset, None, datetime.datetime] = UNSET
    ingesting: Union[Unset, None, bool] = UNSET
    error: Union[Unset, None, str] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    string1: Union[Unset, None, str] = UNSET
    string2: Union[Unset, None, str] = UNSET
    string3: Union[Unset, None, str] = UNSET
    number1: Union[Unset, None, int] = UNSET
    number2: Union[Unset, None, int] = UNSET
    number3: Union[Unset, None, int] = UNSET
    duration: Union[Unset, None, int] = UNSET
    width: Union[Unset, None, int] = UNSET
    height: Union[Unset, None, int] = UNSET
    metadata: Union[Unset, None, str] = UNSET
    storage: Union[Unset, None, str] = UNSET
    media_type: Union[Unset, None, str] = UNSET
    family: Union[Unset, AssetFamily] = UNSET
    text: Union[Unset, None, str] = UNSET
    text_type: Union[Unset, None, str] = UNSET
    delivery_channels: Union[Unset, None, List["DeliveryChannel"]] = UNSET
    roles: Union[Unset, None, List[str]] = UNSET
    batch: Union[Unset, None, str] = UNSET
    image_optimisation_policy: Union[Unset, None, str] = UNSET
    thumbnail_policy: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        customer_id = self.customer_id
        storage_identifier = self.storage_identifier
        model_id = self.model_id
        space = self.space
        image_service = self.image_service
        degraded_info_json = self.degraded_info_json
        thumbnail_image_service = self.thumbnail_image_service
        thumbnail400 = self.thumbnail400
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        origin = self.origin
        max_unauthorised = self.max_unauthorised
        queued: Union[Unset, None, str] = UNSET
        if not isinstance(self.queued, Unset):
            queued = self.queued.isoformat() if self.queued else None

        dequeued: Union[Unset, None, str] = UNSET
        if not isinstance(self.dequeued, Unset):
            dequeued = self.dequeued.isoformat() if self.dequeued else None

        finished: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished, Unset):
            finished = self.finished.isoformat() if self.finished else None

        ingesting = self.ingesting
        error = self.error
        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        string1 = self.string1
        string2 = self.string2
        string3 = self.string3
        number1 = self.number1
        number2 = self.number2
        number3 = self.number3
        duration = self.duration
        width = self.width
        height = self.height
        metadata = self.metadata
        storage = self.storage
        media_type = self.media_type
        family: Union[Unset, int] = UNSET
        if not isinstance(self.family, Unset):
            family = self.family.value

        text = self.text
        text_type = self.text_type
        delivery_channels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.delivery_channels, Unset):
            if self.delivery_channels is None:
                delivery_channels = None
            else:
                delivery_channels = []
                for delivery_channels_item_data in self.delivery_channels:
                    delivery_channels_item = delivery_channels_item_data.to_dict()

                    delivery_channels.append(delivery_channels_item)

        roles: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.roles, Unset):
            if self.roles is None:
                roles = None
            else:
                roles = self.roles

        batch = self.batch
        image_optimisation_policy = self.image_optimisation_policy
        thumbnail_policy = self.thumbnail_policy

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
        if storage_identifier is not UNSET:
            field_dict["storageIdentifier"] = storage_identifier
        if model_id is not UNSET:
            field_dict["modelId"] = model_id
        if space is not UNSET:
            field_dict["space"] = space
        if image_service is not UNSET:
            field_dict["imageService"] = image_service
        if degraded_info_json is not UNSET:
            field_dict["degradedInfoJson"] = degraded_info_json
        if thumbnail_image_service is not UNSET:
            field_dict["thumbnailImageService"] = thumbnail_image_service
        if thumbnail400 is not UNSET:
            field_dict["thumbnail400"] = thumbnail400
        if created is not UNSET:
            field_dict["created"] = created
        if origin is not UNSET:
            field_dict["origin"] = origin
        if max_unauthorised is not UNSET:
            field_dict["maxUnauthorised"] = max_unauthorised
        if queued is not UNSET:
            field_dict["queued"] = queued
        if dequeued is not UNSET:
            field_dict["dequeued"] = dequeued
        if finished is not UNSET:
            field_dict["finished"] = finished
        if ingesting is not UNSET:
            field_dict["ingesting"] = ingesting
        if error is not UNSET:
            field_dict["error"] = error
        if tags is not UNSET:
            field_dict["tags"] = tags
        if string1 is not UNSET:
            field_dict["string1"] = string1
        if string2 is not UNSET:
            field_dict["string2"] = string2
        if string3 is not UNSET:
            field_dict["string3"] = string3
        if number1 is not UNSET:
            field_dict["number1"] = number1
        if number2 is not UNSET:
            field_dict["number2"] = number2
        if number3 is not UNSET:
            field_dict["number3"] = number3
        if duration is not UNSET:
            field_dict["duration"] = duration
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if storage is not UNSET:
            field_dict["storage"] = storage
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if family is not UNSET:
            field_dict["family"] = family
        if text is not UNSET:
            field_dict["text"] = text
        if text_type is not UNSET:
            field_dict["textType"] = text_type
        if delivery_channels is not UNSET:
            field_dict["deliveryChannels"] = delivery_channels
        if roles is not UNSET:
            field_dict["roles"] = roles
        if batch is not UNSET:
            field_dict["batch"] = batch
        if image_optimisation_policy is not UNSET:
            field_dict["imageOptimisationPolicy"] = image_optimisation_policy
        if thumbnail_policy is not UNSET:
            field_dict["thumbnailPolicy"] = thumbnail_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_channel import DeliveryChannel

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        customer_id = d.pop("customerId", UNSET)

        storage_identifier = d.pop("storageIdentifier", UNSET)

        model_id = d.pop("modelId", UNSET)

        space = d.pop("space", UNSET)

        image_service = d.pop("imageService", UNSET)

        degraded_info_json = d.pop("degradedInfoJson", UNSET)

        thumbnail_image_service = d.pop("thumbnailImageService", UNSET)

        thumbnail400 = d.pop("thumbnail400", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        origin = d.pop("origin", UNSET)

        max_unauthorised = d.pop("maxUnauthorised", UNSET)

        _queued = d.pop("queued", UNSET)
        queued: Union[Unset, None, datetime.datetime]
        if _queued is None:
            queued = None
        elif isinstance(_queued, Unset):
            queued = UNSET
        else:
            queued = isoparse(_queued)

        _dequeued = d.pop("dequeued", UNSET)
        dequeued: Union[Unset, None, datetime.datetime]
        if _dequeued is None:
            dequeued = None
        elif isinstance(_dequeued, Unset):
            dequeued = UNSET
        else:
            dequeued = isoparse(_dequeued)

        _finished = d.pop("finished", UNSET)
        finished: Union[Unset, None, datetime.datetime]
        if _finished is None:
            finished = None
        elif isinstance(_finished, Unset):
            finished = UNSET
        else:
            finished = isoparse(_finished)

        ingesting = d.pop("ingesting", UNSET)

        error = d.pop("error", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        string1 = d.pop("string1", UNSET)

        string2 = d.pop("string2", UNSET)

        string3 = d.pop("string3", UNSET)

        number1 = d.pop("number1", UNSET)

        number2 = d.pop("number2", UNSET)

        number3 = d.pop("number3", UNSET)

        duration = d.pop("duration", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        metadata = d.pop("metadata", UNSET)

        storage = d.pop("storage", UNSET)

        media_type = d.pop("mediaType", UNSET)

        _family = d.pop("family", UNSET)
        family: Union[Unset, AssetFamily]
        if isinstance(_family, Unset):
            family = UNSET
        else:
            family = AssetFamily(_family)

        text = d.pop("text", UNSET)

        text_type = d.pop("textType", UNSET)

        delivery_channels = []
        _delivery_channels = d.pop("deliveryChannels", UNSET)
        for delivery_channels_item_data in _delivery_channels or []:
            delivery_channels_item = DeliveryChannel.from_dict(delivery_channels_item_data)

            delivery_channels.append(delivery_channels_item)

        roles = cast(List[str], d.pop("roles", UNSET))

        batch = d.pop("batch", UNSET)

        image_optimisation_policy = d.pop("imageOptimisationPolicy", UNSET)

        thumbnail_policy = d.pop("thumbnailPolicy", UNSET)

        image = cls(
            id=id,
            context=context,
            type=type,
            customer_id=customer_id,
            storage_identifier=storage_identifier,
            model_id=model_id,
            space=space,
            image_service=image_service,
            degraded_info_json=degraded_info_json,
            thumbnail_image_service=thumbnail_image_service,
            thumbnail400=thumbnail400,
            created=created,
            origin=origin,
            max_unauthorised=max_unauthorised,
            queued=queued,
            dequeued=dequeued,
            finished=finished,
            ingesting=ingesting,
            error=error,
            tags=tags,
            string1=string1,
            string2=string2,
            string3=string3,
            number1=number1,
            number2=number2,
            number3=number3,
            duration=duration,
            width=width,
            height=height,
            metadata=metadata,
            storage=storage,
            media_type=media_type,
            family=family,
            text=text,
            text_type=text_type,
            delivery_channels=delivery_channels,
            roles=roles,
            batch=batch,
            image_optimisation_policy=image_optimisation_policy,
            thumbnail_policy=thumbnail_policy,
        )

        return image
