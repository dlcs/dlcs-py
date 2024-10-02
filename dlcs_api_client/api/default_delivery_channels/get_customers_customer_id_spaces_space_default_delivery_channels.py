from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_delivery_channel_hydra_collection import DefaultDeliveryChannelHydraCollection
from ...types import Response


def _get_kwargs(
    customer_id: int,
    space: int = 0,
) -> Dict[str, Any]:

    pass

    return {
        "method": "get",
        "url": "/customers/{customerId}/spaces/{space}/defaultDeliveryChannels".format(
            customerId=customer_id,
            space=space,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DefaultDeliveryChannelHydraCollection]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DefaultDeliveryChannelHydraCollection.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DefaultDeliveryChannelHydraCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    space: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DefaultDeliveryChannelHydraCollection]:
    """Get paged list of all customer accessible default delivery channels (customer specific + system)

    Supports ?page= and ?pageSize= query parameters

    Args:
        customer_id (int):
        space (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DefaultDeliveryChannelHydraCollection]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space=space,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    space: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DefaultDeliveryChannelHydraCollection]:
    """Get paged list of all customer accessible default delivery channels (customer specific + system)

    Supports ?page= and ?pageSize= query parameters

    Args:
        customer_id (int):
        space (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DefaultDeliveryChannelHydraCollection
    """

    return sync_detailed(
        customer_id=customer_id,
        space=space,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    space: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DefaultDeliveryChannelHydraCollection]:
    """Get paged list of all customer accessible default delivery channels (customer specific + system)

    Supports ?page= and ?pageSize= query parameters

    Args:
        customer_id (int):
        space (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DefaultDeliveryChannelHydraCollection]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space=space,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    space: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DefaultDeliveryChannelHydraCollection]:
    """Get paged list of all customer accessible default delivery channels (customer specific + system)

    Supports ?page= and ?pageSize= query parameters

    Args:
        customer_id (int):
        space (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DefaultDeliveryChannelHydraCollection
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            space=space,
            client=client,
        )
    ).parsed
