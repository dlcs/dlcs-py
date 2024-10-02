from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_optimisation_policy import ImageOptimisationPolicy
    from ..models.partial_collection_view import PartialCollectionView


T = TypeVar("T", bound="ImageOptimisationPolicyHydraCollection")


@define
class ImageOptimisationPolicyHydraCollection:
    """
    Attributes:
        id (Union[Unset, None, str]):
        with_context (Union[Unset, bool]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        total_items (Union[Unset, int]):
        page_size (Union[Unset, None, int]):
        members (Union[Unset, None, List['ImageOptimisationPolicy']]):
        view (Union[Unset, PartialCollectionView]):
    """

    id: Union[Unset, None, str] = UNSET
    with_context: Union[Unset, bool] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    total_items: Union[Unset, int] = UNSET
    page_size: Union[Unset, None, int] = UNSET
    members: Union[Unset, None, List["ImageOptimisationPolicy"]] = UNSET
    view: Union[Unset, "PartialCollectionView"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        with_context = self.with_context
        context = self.context
        type = self.type
        total_items = self.total_items
        page_size = self.page_size
        members: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            if self.members is None:
                members = None
            else:
                members = []
                for members_item_data in self.members:
                    members_item = members_item_data.to_dict()

                    members.append(members_item)

        view: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.view, Unset):
            view = self.view.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if with_context is not UNSET:
            field_dict["withContext"] = with_context
        if context is not UNSET:
            field_dict["context"] = context
        if type is not UNSET:
            field_dict["type"] = type
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if members is not UNSET:
            field_dict["members"] = members
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_optimisation_policy import ImageOptimisationPolicy
        from ..models.partial_collection_view import PartialCollectionView

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        with_context = d.pop("withContext", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        total_items = d.pop("totalItems", UNSET)

        page_size = d.pop("pageSize", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = ImageOptimisationPolicy.from_dict(members_item_data)

            members.append(members_item)

        _view = d.pop("view", UNSET)
        view: Union[Unset, PartialCollectionView]
        if isinstance(_view, Unset):
            view = UNSET
        else:
            view = PartialCollectionView.from_dict(_view)

        image_optimisation_policy_hydra_collection = cls(
            id=id,
            with_context=with_context,
            context=context,
            type=type,
            total_items=total_items,
            page_size=page_size,
            members=members,
            view=view,
        )

        return image_optimisation_policy_hydra_collection
