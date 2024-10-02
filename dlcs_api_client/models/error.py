from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@define
class Error:
    """
    Attributes:
        id (Union[Unset, None, str]):
        with_context (Union[Unset, bool]):
        context (Union[Unset, None, str]):
        status_code (Union[Unset, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        error_type_uri (Union[Unset, None, str]):
        status (Union[Unset, int]):
        detail (Union[Unset, None, str]):
        instance (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    with_context: Union[Unset, bool] = UNSET
    context: Union[Unset, None, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    error_type_uri: Union[Unset, None, str] = UNSET
    status: Union[Unset, int] = UNSET
    detail: Union[Unset, None, str] = UNSET
    instance: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        with_context = self.with_context
        context = self.context
        status_code = self.status_code
        title = self.title
        description = self.description
        type = self.type
        error_type_uri = self.error_type_uri
        status = self.status
        detail = self.detail
        instance = self.instance

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if with_context is not UNSET:
            field_dict["withContext"] = with_context
        if context is not UNSET:
            field_dict["context"] = context
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if type is not UNSET:
            field_dict["type"] = type
        if error_type_uri is not UNSET:
            field_dict["errorTypeUri"] = error_type_uri
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        with_context = d.pop("withContext", UNSET)

        context = d.pop("context", UNSET)

        status_code = d.pop("statusCode", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        type = d.pop("type", UNSET)

        error_type_uri = d.pop("errorTypeUri", UNSET)

        status = d.pop("status", UNSET)

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        error = cls(
            id=id,
            with_context=with_context,
            context=context,
            status_code=status_code,
            title=title,
            description=description,
            type=type,
            error_type_uri=error_type_uri,
            status=status,
            detail=detail,
            instance=instance,
        )

        return error
