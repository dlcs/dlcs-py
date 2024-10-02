from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.image_hydra_collection import ImageHydraCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: int,
    batch_id: int,
    *,
    q: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/customers/{customerId}/queue/batches/{batchId}/images".format(
            customerId=customer_id,
            batchId=batch_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ImageHydraCollection]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImageHydraCollection.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, ImageHydraCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    batch_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, ImageHydraCollection]]:
    """
    Args:
        customer_id (int):
        batch_id (int):
        q (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ImageHydraCollection]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        batch_id=batch_id,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    batch_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, ImageHydraCollection]]:
    """
    Args:
        customer_id (int):
        batch_id (int):
        q (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ImageHydraCollection]
    """

    return sync_detailed(
        customer_id=customer_id,
        batch_id=batch_id,
        client=client,
        q=q,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    batch_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, ImageHydraCollection]]:
    """
    Args:
        customer_id (int):
        batch_id (int):
        q (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ImageHydraCollection]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        batch_id=batch_id,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    batch_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, ImageHydraCollection]]:
    """
    Args:
        customer_id (int):
        batch_id (int):
        q (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ImageHydraCollection]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            batch_id=batch_id,
            client=client,
            q=q,
        )
    ).parsed
