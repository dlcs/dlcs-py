from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscoderInput")


@define
class TranscoderInput:
    """
    Attributes:
        aspect_ratio (Union[Unset, None, str]):
        container (Union[Unset, None, str]):
        frame_rate (Union[Unset, None, str]):
        interlaced (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        resolution (Union[Unset, None, str]):
    """

    aspect_ratio: Union[Unset, None, str] = UNSET
    container: Union[Unset, None, str] = UNSET
    frame_rate: Union[Unset, None, str] = UNSET
    interlaced: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    resolution: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        aspect_ratio = self.aspect_ratio
        container = self.container
        frame_rate = self.frame_rate
        interlaced = self.interlaced
        key = self.key
        resolution = self.resolution

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if aspect_ratio is not UNSET:
            field_dict["aspectRatio"] = aspect_ratio
        if container is not UNSET:
            field_dict["container"] = container
        if frame_rate is not UNSET:
            field_dict["frameRate"] = frame_rate
        if interlaced is not UNSET:
            field_dict["interlaced"] = interlaced
        if key is not UNSET:
            field_dict["key"] = key
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aspect_ratio = d.pop("aspectRatio", UNSET)

        container = d.pop("container", UNSET)

        frame_rate = d.pop("frameRate", UNSET)

        interlaced = d.pop("interlaced", UNSET)

        key = d.pop("key", UNSET)

        resolution = d.pop("resolution", UNSET)

        transcoder_input = cls(
            aspect_ratio=aspect_ratio,
            container=container,
            frame_rate=frame_rate,
            interlaced=interlaced,
            key=key,
            resolution=resolution,
        )

        return transcoder_input
