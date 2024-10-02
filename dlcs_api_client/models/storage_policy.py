from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoragePolicy")


@define
class StoragePolicy:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, None, str]):
        maximum_number_of_stored_images (Union[Unset, int]):
        maximum_total_size_of_stored_images (Union[Unset, int]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, None, str] = UNSET
    maximum_number_of_stored_images: Union[Unset, int] = UNSET
    maximum_total_size_of_stored_images: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        maximum_number_of_stored_images = self.maximum_number_of_stored_images
        maximum_total_size_of_stored_images = self.maximum_total_size_of_stored_images

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
        if maximum_number_of_stored_images is not UNSET:
            field_dict["maximumNumberOfStoredImages"] = maximum_number_of_stored_images
        if maximum_total_size_of_stored_images is not UNSET:
            field_dict["maximumTotalSizeOfStoredImages"] = maximum_total_size_of_stored_images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        maximum_number_of_stored_images = d.pop("maximumNumberOfStoredImages", UNSET)

        maximum_total_size_of_stored_images = d.pop("maximumTotalSizeOfStoredImages", UNSET)

        storage_policy = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            maximum_number_of_stored_images=maximum_number_of_stored_images,
            maximum_total_size_of_stored_images=maximum_total_size_of_stored_images,
        )

        return storage_policy
