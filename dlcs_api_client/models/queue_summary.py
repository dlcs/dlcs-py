from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueSummary")


@define
class QueueSummary:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        incoming (Union[Unset, int]):
        priority (Union[Unset, int]):
        timebased (Union[Unset, int]):
        transcode_complete (Union[Unset, int]):
        file (Union[Unset, int]):
        failed (Union[Unset, int]):
        success (Union[Unset, int]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    incoming: Union[Unset, int] = UNSET
    priority: Union[Unset, int] = UNSET
    timebased: Union[Unset, int] = UNSET
    transcode_complete: Union[Unset, int] = UNSET
    file: Union[Unset, int] = UNSET
    failed: Union[Unset, int] = UNSET
    success: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        incoming = self.incoming
        priority = self.priority
        timebased = self.timebased
        transcode_complete = self.transcode_complete
        file = self.file
        failed = self.failed
        success = self.success

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if context is not UNSET:
            field_dict["context"] = context
        if type is not UNSET:
            field_dict["type"] = type
        if incoming is not UNSET:
            field_dict["incoming"] = incoming
        if priority is not UNSET:
            field_dict["priority"] = priority
        if timebased is not UNSET:
            field_dict["timebased"] = timebased
        if transcode_complete is not UNSET:
            field_dict["transcodeComplete"] = transcode_complete
        if file is not UNSET:
            field_dict["file"] = file
        if failed is not UNSET:
            field_dict["failed"] = failed
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        incoming = d.pop("incoming", UNSET)

        priority = d.pop("priority", UNSET)

        timebased = d.pop("timebased", UNSET)

        transcode_complete = d.pop("transcodeComplete", UNSET)

        file = d.pop("file", UNSET)

        failed = d.pop("failed", UNSET)

        success = d.pop("success", UNSET)

        queue_summary = cls(
            id=id,
            context=context,
            type=type,
            incoming=incoming,
            priority=priority,
            timebased=timebased,
            transcode_complete=transcode_complete,
            file=file,
            failed=failed,
            success=success,
        )

        return queue_summary
