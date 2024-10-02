import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Batch")


@define
class Batch:
    """
    Attributes:
        id (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        model_id (Union[Unset, int]):
        customer_id (Union[Unset, int]):
        submitted (Union[Unset, datetime.datetime]):
        count (Union[Unset, int]):
        completed (Union[Unset, int]):
        finished (Union[Unset, None, datetime.datetime]):
        errors (Union[Unset, int]):
        superseded (Union[Unset, bool]):
        est_completion (Union[Unset, None, datetime.datetime]):
        images (Union[Unset, None, str]):
        completed_images (Union[Unset, None, str]):
        error_images (Union[Unset, None, str]):
        test (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    model_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, int] = UNSET
    submitted: Union[Unset, datetime.datetime] = UNSET
    count: Union[Unset, int] = UNSET
    completed: Union[Unset, int] = UNSET
    finished: Union[Unset, None, datetime.datetime] = UNSET
    errors: Union[Unset, int] = UNSET
    superseded: Union[Unset, bool] = UNSET
    est_completion: Union[Unset, None, datetime.datetime] = UNSET
    images: Union[Unset, None, str] = UNSET
    completed_images: Union[Unset, None, str] = UNSET
    error_images: Union[Unset, None, str] = UNSET
    test: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        context = self.context
        type = self.type
        model_id = self.model_id
        customer_id = self.customer_id
        submitted: Union[Unset, str] = UNSET
        if not isinstance(self.submitted, Unset):
            submitted = self.submitted.isoformat()

        count = self.count
        completed = self.completed
        finished: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished, Unset):
            finished = self.finished.isoformat() if self.finished else None

        errors = self.errors
        superseded = self.superseded
        est_completion: Union[Unset, None, str] = UNSET
        if not isinstance(self.est_completion, Unset):
            est_completion = self.est_completion.isoformat() if self.est_completion else None

        images = self.images
        completed_images = self.completed_images
        error_images = self.error_images
        test = self.test

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
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if count is not UNSET:
            field_dict["count"] = count
        if completed is not UNSET:
            field_dict["completed"] = completed
        if finished is not UNSET:
            field_dict["finished"] = finished
        if errors is not UNSET:
            field_dict["errors"] = errors
        if superseded is not UNSET:
            field_dict["superseded"] = superseded
        if est_completion is not UNSET:
            field_dict["estCompletion"] = est_completion
        if images is not UNSET:
            field_dict["images"] = images
        if completed_images is not UNSET:
            field_dict["completedImages"] = completed_images
        if error_images is not UNSET:
            field_dict["errorImages"] = error_images
        if test is not UNSET:
            field_dict["test"] = test

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        context = d.pop("context", UNSET)

        type = d.pop("type", UNSET)

        model_id = d.pop("modelId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        _submitted = d.pop("submitted", UNSET)
        submitted: Union[Unset, datetime.datetime]
        if isinstance(_submitted, Unset):
            submitted = UNSET
        else:
            submitted = isoparse(_submitted)

        count = d.pop("count", UNSET)

        completed = d.pop("completed", UNSET)

        _finished = d.pop("finished", UNSET)
        finished: Union[Unset, None, datetime.datetime]
        if _finished is None:
            finished = None
        elif isinstance(_finished, Unset):
            finished = UNSET
        else:
            finished = isoparse(_finished)

        errors = d.pop("errors", UNSET)

        superseded = d.pop("superseded", UNSET)

        _est_completion = d.pop("estCompletion", UNSET)
        est_completion: Union[Unset, None, datetime.datetime]
        if _est_completion is None:
            est_completion = None
        elif isinstance(_est_completion, Unset):
            est_completion = UNSET
        else:
            est_completion = isoparse(_est_completion)

        images = d.pop("images", UNSET)

        completed_images = d.pop("completedImages", UNSET)

        error_images = d.pop("errorImages", UNSET)

        test = d.pop("test", UNSET)

        batch = cls(
            id=id,
            context=context,
            type=type,
            model_id=model_id,
            customer_id=customer_id,
            submitted=submitted,
            count=count,
            completed=completed,
            finished=finished,
            errors=errors,
            superseded=superseded,
            est_completion=est_completion,
            images=images,
            completed_images=completed_images,
            error_images=error_images,
            test=test,
        )

        return batch
