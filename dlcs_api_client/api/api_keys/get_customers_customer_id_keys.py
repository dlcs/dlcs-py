from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_hydra_collection import ApiKeyHydraCollection
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    customer_id: int,
) -> Dict[str, Any]:

    pass

    return {
        "method": "get",
        "url": "/customers/{customerId}/keys".format(
            customerId=customer_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiKeyHydraCollection, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiKeyHydraCollection.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiKeyHydraCollection, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiKeyHydraCollection, Error]]:
    """Get a list of all the API Keys available for this customer

    Args:
        customer_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKeyHydraCollection, Error]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiKeyHydraCollection, Error]]:
    """Get a list of all the API Keys available for this customer

    Args:
        customer_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKeyHydraCollection, Error]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiKeyHydraCollection, Error]]:
    """Get a list of all the API Keys available for this customer

    Args:
        customer_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKeyHydraCollection, Error]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiKeyHydraCollection, Error]]:
    """Get a list of all the API Keys available for this customer

    Args:
        customer_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKeyHydraCollection, Error]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
        )
    ).parsed
