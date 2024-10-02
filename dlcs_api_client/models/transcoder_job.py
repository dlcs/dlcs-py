from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcoder_input import TranscoderInput
    from ..models.transcoder_job_user_metadata import TranscoderJobUserMetadata
    from ..models.transcoder_output import TranscoderOutput
    from ..models.transcoder_playlist import TranscoderPlaylist
    from ..models.transcoder_timing import TranscoderTiming


T = TypeVar("T", bound="TranscoderJob")


@define
class TranscoderJob:
    """
    Attributes:
        id (Union[Unset, None, str]):
        output_key_prefix (Union[Unset, None, str]):
        input_ (Union[Unset, TranscoderInput]):
        inputs (Union[Unset, None, List['TranscoderInput']]):
        output (Union[Unset, TranscoderOutput]):
        outputs (Union[Unset, None, List['TranscoderOutput']]):
        pipeline_id (Union[Unset, None, str]):
        status (Union[Unset, None, str]):
        timing (Union[Unset, TranscoderTiming]):
        user_metadata (Union[Unset, None, TranscoderJobUserMetadata]):
        playlists (Union[Unset, None, List['TranscoderPlaylist']]):
    """

    id: Union[Unset, None, str] = UNSET
    output_key_prefix: Union[Unset, None, str] = UNSET
    input_: Union[Unset, "TranscoderInput"] = UNSET
    inputs: Union[Unset, None, List["TranscoderInput"]] = UNSET
    output: Union[Unset, "TranscoderOutput"] = UNSET
    outputs: Union[Unset, None, List["TranscoderOutput"]] = UNSET
    pipeline_id: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET
    timing: Union[Unset, "TranscoderTiming"] = UNSET
    user_metadata: Union[Unset, None, "TranscoderJobUserMetadata"] = UNSET
    playlists: Union[Unset, None, List["TranscoderPlaylist"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        output_key_prefix = self.output_key_prefix
        input_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        inputs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inputs, Unset):
            if self.inputs is None:
                inputs = None
            else:
                inputs = []
                for inputs_item_data in self.inputs:
                    inputs_item = inputs_item_data.to_dict()

                    inputs.append(inputs_item)

        output: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        outputs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.outputs, Unset):
            if self.outputs is None:
                outputs = None
            else:
                outputs = []
                for outputs_item_data in self.outputs:
                    outputs_item = outputs_item_data.to_dict()

                    outputs.append(outputs_item)

        pipeline_id = self.pipeline_id
        status = self.status
        timing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timing, Unset):
            timing = self.timing.to_dict()

        user_metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user_metadata, Unset):
            user_metadata = self.user_metadata.to_dict() if self.user_metadata else None

        playlists: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.playlists, Unset):
            if self.playlists is None:
                playlists = None
            else:
                playlists = []
                for playlists_item_data in self.playlists:
                    playlists_item = playlists_item_data.to_dict()

                    playlists.append(playlists_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if output_key_prefix is not UNSET:
            field_dict["outputKeyPrefix"] = output_key_prefix
        if input_ is not UNSET:
            field_dict["input"] = input_
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if output is not UNSET:
            field_dict["output"] = output
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if status is not UNSET:
            field_dict["status"] = status
        if timing is not UNSET:
            field_dict["timing"] = timing
        if user_metadata is not UNSET:
            field_dict["userMetadata"] = user_metadata
        if playlists is not UNSET:
            field_dict["playlists"] = playlists

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transcoder_input import TranscoderInput
        from ..models.transcoder_job_user_metadata import TranscoderJobUserMetadata
        from ..models.transcoder_output import TranscoderOutput
        from ..models.transcoder_playlist import TranscoderPlaylist
        from ..models.transcoder_timing import TranscoderTiming

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        output_key_prefix = d.pop("outputKeyPrefix", UNSET)

        _input_ = d.pop("input", UNSET)
        input_: Union[Unset, TranscoderInput]
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = TranscoderInput.from_dict(_input_)

        inputs = []
        _inputs = d.pop("inputs", UNSET)
        for inputs_item_data in _inputs or []:
            inputs_item = TranscoderInput.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        _output = d.pop("output", UNSET)
        output: Union[Unset, TranscoderOutput]
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = TranscoderOutput.from_dict(_output)

        outputs = []
        _outputs = d.pop("outputs", UNSET)
        for outputs_item_data in _outputs or []:
            outputs_item = TranscoderOutput.from_dict(outputs_item_data)

            outputs.append(outputs_item)

        pipeline_id = d.pop("pipelineId", UNSET)

        status = d.pop("status", UNSET)

        _timing = d.pop("timing", UNSET)
        timing: Union[Unset, TranscoderTiming]
        if isinstance(_timing, Unset):
            timing = UNSET
        else:
            timing = TranscoderTiming.from_dict(_timing)

        _user_metadata = d.pop("userMetadata", UNSET)
        user_metadata: Union[Unset, None, TranscoderJobUserMetadata]
        if _user_metadata is None:
            user_metadata = None
        elif isinstance(_user_metadata, Unset):
            user_metadata = UNSET
        else:
            user_metadata = TranscoderJobUserMetadata.from_dict(_user_metadata)

        playlists = []
        _playlists = d.pop("playlists", UNSET)
        for playlists_item_data in _playlists or []:
            playlists_item = TranscoderPlaylist.from_dict(playlists_item_data)

            playlists.append(playlists_item)

        transcoder_job = cls(
            id=id,
            output_key_prefix=output_key_prefix,
            input_=input_,
            inputs=inputs,
            output=output,
            outputs=outputs,
            pipeline_id=pipeline_id,
            status=status,
            timing=timing,
            user_metadata=user_metadata,
            playlists=playlists,
        )

        return transcoder_job
