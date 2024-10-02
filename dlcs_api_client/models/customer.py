import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Customer")


@define
class Customer:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        portal_users (Union[Unset, None, str]):
        named_queries (Union[Unset, None, str]):
        origin_strategies (Union[Unset, None, str]):
        delivery_channel_policies (Union[Unset, None, str]):
        default_delivery_channels (Union[Unset, None, str]):
        auth_services (Union[Unset, None, str]):
        role_providers (Union[Unset, None, str]):
        roles (Union[Unset, None, str]):
        queue (Union[Unset, None, str]):
        spaces (Union[Unset, None, str]):
        all_images (Union[Unset, None, str]):
        storage (Union[Unset, None, str]):
        keys (Union[Unset, None, str]):
        custom_headers (Union[Unset, None, str]):
        administrator (Union[Unset, None, bool]):
        created (Union[Unset, None, datetime.datetime]):
        accepted_agreement (Union[Unset, None, bool]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    portal_users: Union[Unset, None, str] = UNSET
    named_queries: Union[Unset, None, str] = UNSET
    origin_strategies: Union[Unset, None, str] = UNSET
    delivery_channel_policies: Union[Unset, None, str] = UNSET
    default_delivery_channels: Union[Unset, None, str] = UNSET
    auth_services: Union[Unset, None, str] = UNSET
    role_providers: Union[Unset, None, str] = UNSET
    roles: Union[Unset, None, str] = UNSET
    queue: Union[Unset, None, str] = UNSET
    spaces: Union[Unset, None, str] = UNSET
    all_images: Union[Unset, None, str] = UNSET
    storage: Union[Unset, None, str] = UNSET
    keys: Union[Unset, None, str] = UNSET
    custom_headers: Union[Unset, None, str] = UNSET
    administrator: Union[Unset, None, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    accepted_agreement: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        name = self.name
        display_name = self.display_name
        portal_users = self.portal_users
        named_queries = self.named_queries
        origin_strategies = self.origin_strategies
        delivery_channel_policies = self.delivery_channel_policies
        default_delivery_channels = self.default_delivery_channels
        auth_services = self.auth_services
        role_providers = self.role_providers
        roles = self.roles
        queue = self.queue
        spaces = self.spaces
        all_images = self.all_images
        storage = self.storage
        keys = self.keys
        custom_headers = self.custom_headers
        administrator = self.administrator
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        accepted_agreement = self.accepted_agreement

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
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if portal_users is not UNSET:
            field_dict["portalUsers"] = portal_users
        if named_queries is not UNSET:
            field_dict["namedQueries"] = named_queries
        if origin_strategies is not UNSET:
            field_dict["originStrategies"] = origin_strategies
        if delivery_channel_policies is not UNSET:
            field_dict["deliveryChannelPolicies"] = delivery_channel_policies
        if default_delivery_channels is not UNSET:
            field_dict["defaultDeliveryChannels"] = default_delivery_channels
        if auth_services is not UNSET:
            field_dict["authServices"] = auth_services
        if role_providers is not UNSET:
            field_dict["roleProviders"] = role_providers
        if roles is not UNSET:
            field_dict["roles"] = roles
        if queue is not UNSET:
            field_dict["queue"] = queue
        if spaces is not UNSET:
            field_dict["spaces"] = spaces
        if all_images is not UNSET:
            field_dict["allImages"] = all_images
        if storage is not UNSET:
            field_dict["storage"] = storage
        if keys is not UNSET:
            field_dict["keys"] = keys
        if custom_headers is not UNSET:
            field_dict["customHeaders"] = custom_headers
        if administrator is not UNSET:
            field_dict["administrator"] = administrator
        if created is not UNSET:
            field_dict["created"] = created
        if accepted_agreement is not UNSET:
            field_dict["acceptedAgreement"] = accepted_agreement

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        portal_users = d.pop("portalUsers", UNSET)

        named_queries = d.pop("namedQueries", UNSET)

        origin_strategies = d.pop("originStrategies", UNSET)

        delivery_channel_policies = d.pop("deliveryChannelPolicies", UNSET)

        default_delivery_channels = d.pop("defaultDeliveryChannels", UNSET)

        auth_services = d.pop("authServices", UNSET)

        role_providers = d.pop("roleProviders", UNSET)

        roles = d.pop("roles", UNSET)

        queue = d.pop("queue", UNSET)

        spaces = d.pop("spaces", UNSET)

        all_images = d.pop("allImages", UNSET)

        storage = d.pop("storage", UNSET)

        keys = d.pop("keys", UNSET)

        custom_headers = d.pop("customHeaders", UNSET)

        administrator = d.pop("administrator", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        accepted_agreement = d.pop("acceptedAgreement", UNSET)

        customer = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            name=name,
            display_name=display_name,
            portal_users=portal_users,
            named_queries=named_queries,
            origin_strategies=origin_strategies,
            delivery_channel_policies=delivery_channel_policies,
            default_delivery_channels=default_delivery_channels,
            auth_services=auth_services,
            role_providers=role_providers,
            roles=roles,
            queue=queue,
            spaces=spaces,
            all_images=all_images,
            storage=storage,
            keys=keys,
            custom_headers=custom_headers,
            administrator=administrator,
            created=created,
            accepted_agreement=accepted_agreement,
        )

        return customer
