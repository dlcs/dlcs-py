from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    delete_from: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["deleteFrom"] = delete_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": "/customers/{customerId}/spaces/{spaceId}/images/{imageId}".format(
            customerId=customer_id,
            spaceId=space_id,
            imageId=image_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    delete_from: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """DELETE asset at specified location. This will remove asset immediately, generated derivatives will
    be picked up
    and processed eventually.

    Args:
        customer_id (int):
        space_id (int):
        image_id (str):
        delete_from (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space_id=space_id,
        image_id=image_id,
        delete_from=delete_from,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    delete_from: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """DELETE asset at specified location. This will remove asset immediately, generated derivatives will
    be picked up
    and processed eventually.

    Args:
        customer_id (int):
        space_id (int):
        image_id (str):
        delete_from (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        customer_id=customer_id,
        space_id=space_id,
        image_id=image_id,
        client=client,
        delete_from=delete_from,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    delete_from: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """DELETE asset at specified location. This will remove asset immediately, generated derivatives will
    be picked up
    and processed eventually.

    Args:
        customer_id (int):
        space_id (int):
        image_id (str):
        delete_from (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space_id=space_id,
        image_id=image_id,
        delete_from=delete_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    delete_from: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """DELETE asset at specified location. This will remove asset immediately, generated derivatives will
    be picked up
    and processed eventually.

    Args:
        customer_id (int):
        space_id (int):
        image_id (str):
        delete_from (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            space_id=space_id,
            image_id=image_id,
            client=client,
            delete_from=delete_from,
        )
    ).parsed
