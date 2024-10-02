from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscoderTiming")


@define
class TranscoderTiming:
    """
    Attributes:
        finish_time_millis (Union[Unset, int]):
        start_time_millis (Union[Unset, int]):
        submit_time_millis (Union[Unset, int]):
    """

    finish_time_millis: Union[Unset, int] = UNSET
    start_time_millis: Union[Unset, int] = UNSET
    submit_time_millis: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        finish_time_millis = self.finish_time_millis
        start_time_millis = self.start_time_millis
        submit_time_millis = self.submit_time_millis

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if finish_time_millis is not UNSET:
            field_dict["finishTimeMillis"] = finish_time_millis
        if start_time_millis is not UNSET:
            field_dict["startTimeMillis"] = start_time_millis
        if submit_time_millis is not UNSET:
            field_dict["submitTimeMillis"] = submit_time_millis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        finish_time_millis = d.pop("finishTimeMillis", UNSET)

        start_time_millis = d.pop("startTimeMillis", UNSET)

        submit_time_millis = d.pop("submitTimeMillis", UNSET)

        transcoder_timing = cls(
            finish_time_millis=finish_time_millis,
            start_time_millis=start_time_millis,
            submit_time_millis=submit_time_millis,
        )

        return transcoder_timing
