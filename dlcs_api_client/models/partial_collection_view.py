from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialCollectionView")


@define
class PartialCollectionView:
    """
    Attributes:
        id (Union[Unset, None, str]):
        with_context (Union[Unset, bool]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        first (Union[Unset, None, str]):
        previous (Union[Unset, None, str]):
        next_ (Union[Unset, None, str]):
        last (Union[Unset, None, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        total_pages (Union[Unset, int]):
    """

    id: Union[Unset, None, str] = UNSET
    with_context: Union[Unset, bool] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    first: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    next_: Union[Unset, None, str] = UNSET
    last: Union[Unset, None, str] = UNSET
    page: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        with_context = self.with_context
        context = self.context
        type = self.type
        first = self.first
        previous = self.previous
        next_ = self.next_
        last = self.last
        page = self.page
        page_size = self.page_size
        total_pages = self.total_pages

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
        if first is not UNSET:
            field_dict["first"] = first
        if previous is not UNSET:
            field_dict["previous"] = previous
        if next_ is not UNSET:
            field_dict["next"] = next_
        if last is not UNSET:
            field_dict["last"] = last
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        with_context = d.pop("withContext", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        first = d.pop("first", UNSET)

        previous = d.pop("previous", UNSET)

        next_ = d.pop("next", UNSET)

        last = d.pop("last", UNSET)

        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        partial_collection_view = cls(
            id=id,
            with_context=with_context,
            context=context,
            type=type,
            first=first,
            previous=previous,
            next_=next_,
            last=last,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

        return partial_collection_view
