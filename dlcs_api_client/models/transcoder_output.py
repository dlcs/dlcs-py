from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscoderOutput")


@define
class TranscoderOutput:
    """
    Attributes:
        id (Union[Unset, None, str]):
        duration (Union[Unset, int]):
        duration_millis (Union[Unset, int]):
        file_size (Union[Unset, int]):
        height (Union[Unset, int]):
        width (Union[Unset, int]):
        key (Union[Unset, None, str]):
        status (Union[Unset, None, str]):
        status_detail (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    duration: Union[Unset, int] = UNSET
    duration_millis: Union[Unset, int] = UNSET
    file_size: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    width: Union[Unset, int] = UNSET
    key: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET
    status_detail: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        duration = self.duration
        duration_millis = self.duration_millis
        file_size = self.file_size
        height = self.height
        width = self.width
        key = self.key
        status = self.status
        status_detail = self.status_detail

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_millis is not UNSET:
            field_dict["durationMillis"] = duration_millis
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if key is not UNSET:
            field_dict["key"] = key
        if status is not UNSET:
            field_dict["status"] = status
        if status_detail is not UNSET:
            field_dict["statusDetail"] = status_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        duration = d.pop("duration", UNSET)

        duration_millis = d.pop("durationMillis", UNSET)

        file_size = d.pop("fileSize", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        key = d.pop("key", UNSET)

        status = d.pop("status", UNSET)

        status_detail = d.pop("statusDetail", UNSET)

        transcoder_output = cls(
            id=id,
            duration=duration,
            duration_millis=duration_millis,
            file_size=file_size,
            height=height,
            width=width,
            key=key,
            status=status,
            status_detail=status_detail,
        )

        return transcoder_output
