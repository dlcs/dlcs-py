from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntryPoint")


@define
class EntryPoint:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        customers (Union[Unset, None, str]):
        origin_strategies (Union[Unset, None, str]):
        portal_roles (Union[Unset, None, str]):
        image_optimisation_policies (Union[Unset, None, str]):
        thumbnail_policies (Union[Unset, None, str]):
        storage_policies (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    customers: Union[Unset, None, str] = UNSET
    origin_strategies: Union[Unset, None, str] = UNSET
    portal_roles: Union[Unset, None, str] = UNSET
    image_optimisation_policies: Union[Unset, None, str] = UNSET
    thumbnail_policies: Union[Unset, None, str] = UNSET
    storage_policies: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        customers = self.customers
        origin_strategies = self.origin_strategies
        portal_roles = self.portal_roles
        image_optimisation_policies = self.image_optimisation_policies
        thumbnail_policies = self.thumbnail_policies
        storage_policies = self.storage_policies

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if context is not UNSET:
            field_dict["context"] = context
        if type is not UNSET:
            field_dict["type"] = type
        if customers is not UNSET:
            field_dict["customers"] = customers
        if origin_strategies is not UNSET:
            field_dict["originStrategies"] = origin_strategies
        if portal_roles is not UNSET:
            field_dict["portalRoles"] = portal_roles
        if image_optimisation_policies is not UNSET:
            field_dict["imageOptimisationPolicies"] = image_optimisation_policies
        if thumbnail_policies is not UNSET:
            field_dict["thumbnailPolicies"] = thumbnail_policies
        if storage_policies is not UNSET:
            field_dict["storagePolicies"] = storage_policies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        customers = d.pop("customers", UNSET)

        origin_strategies = d.pop("originStrategies", UNSET)

        portal_roles = d.pop("portalRoles", UNSET)

        image_optimisation_policies = d.pop("imageOptimisationPolicies", UNSET)

        thumbnail_policies = d.pop("thumbnailPolicies", UNSET)

        storage_policies = d.pop("storagePolicies", UNSET)

        entry_point = cls(
            id=id,
            context=context,
            type=type,
            customers=customers,
            origin_strategies=origin_strategies,
            portal_roles=portal_roles,
            image_optimisation_policies=image_optimisation_policies,
            thumbnail_policies=thumbnail_policies,
            storage_policies=storage_policies,
        )

        return entry_point
