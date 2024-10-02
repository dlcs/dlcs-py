from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThumbnailPolicy")


@define
class ThumbnailPolicy:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        sizes (Union[Unset, None, List[int]]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    sizes: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        name = self.name
        sizes: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.sizes, Unset):
            if self.sizes is None:
                sizes = None
            else:
                sizes = self.sizes

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
        if sizes is not UNSET:
            field_dict["sizes"] = sizes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        name = d.pop("name", UNSET)

        sizes = cast(List[int], d.pop("sizes", UNSET))

        thumbnail_policy = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            name=name,
            sizes=sizes,
        )

        return thumbnail_policy
