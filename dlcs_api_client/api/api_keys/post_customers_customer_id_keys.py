from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key import ApiKey
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    customer_id: int,
) -> Dict[str, Any]:

    pass

    return {
        "method": "post",
        "url": "/customers/{customerId}/keys".format(
            customerId=customer_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiKey, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiKey.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiKey, Error]]:
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
) -> Response[Union[ApiKey, Error]]:
    """Obtain a new API key by posting an empty payload.

    The return value contains both Key and Secret - it is the only time the Secret is visible

     Sample request:

        POST: /customers/1/keys
        { }

    Args:
        customer_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKey, Error]]
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
) -> Optional[Union[ApiKey, Error]]:
    """Obtain a new API key by posting an empty payload.

    The return value contains both Key and Secret - it is the only time the Secret is visible

     Sample request:

        POST: /customers/1/keys
        { }

    Args:
        customer_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKey, Error]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiKey, Error]]:
    """Obtain a new API key by posting an empty payload.

    The return value contains both Key and Secret - it is the only time the Secret is visible

     Sample request:

        POST: /customers/1/keys
        { }

    Args:
        customer_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKey, Error]]
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
) -> Optional[Union[ApiKey, Error]]:
    """Obtain a new API key by posting an empty payload.

    The return value contains both Key and Secret - it is the only time the Secret is visible

     Sample request:

        POST: /customers/1/keys
        { }

    Args:
        customer_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKey, Error]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
        )
    ).parsed
