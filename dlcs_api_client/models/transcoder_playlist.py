from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscoderPlaylist")


@define
class TranscoderPlaylist:
    """
    Attributes:
        format_ (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        output_keys (Union[Unset, None, List[str]]):
        status (Union[Unset, None, str]):
        status_detail (Union[Unset, None, str]):
    """

    format_: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    output_keys: Union[Unset, None, List[str]] = UNSET
    status: Union[Unset, None, str] = UNSET
    status_detail: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_
        name = self.name
        output_keys: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.output_keys, Unset):
            if self.output_keys is None:
                output_keys = None
            else:
                output_keys = self.output_keys

        status = self.status
        status_detail = self.status_detail

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if name is not UNSET:
            field_dict["name"] = name
        if output_keys is not UNSET:
            field_dict["outputKeys"] = output_keys
        if status is not UNSET:
            field_dict["status"] = status
        if status_detail is not UNSET:
            field_dict["statusDetail"] = status_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = d.pop("format", UNSET)

        name = d.pop("name", UNSET)

        output_keys = cast(List[str], d.pop("outputKeys", UNSET))

        status = d.pop("status", UNSET)

        status_detail = d.pop("statusDetail", UNSET)

        transcoder_playlist = cls(
            format_=format_,
            name=name,
            output_keys=output_keys,
            status=status,
            status_detail=status_detail,
        )

        return transcoder_playlist
