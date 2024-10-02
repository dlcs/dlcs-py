import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortalUser")


@define
class PortalUser:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        email (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
        created (Union[Unset, None, datetime.datetime]):
        roles (Union[Unset, None, str]):
        enabled (Union[Unset, None, bool]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    email: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    roles: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        customer_id = self.customer_id
        email = self.email
        password = self.password
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        roles = self.roles
        enabled = self.enabled

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
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if created is not UNSET:
            field_dict["created"] = created
        if roles is not UNSET:
            field_dict["roles"] = roles
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        roles = d.pop("roles", UNSET)

        enabled = d.pop("enabled", UNSET)

        portal_user = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            customer_id=customer_id,
            email=email,
            password=password,
            created=created,
            roles=roles,
            enabled=enabled,
        )

        return portal_user
