from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delivery_channel_policy_hydra_collection import DeliveryChannelPolicyHydraCollection
from ...types import Response


def _get_kwargs(
    customer_id: int,
    delivery_channel_name: str,
) -> Dict[str, Any]:

    pass

    return {
        "method": "get",
        "url": "/customers/{customerId}/deliveryChannelPolicies/{deliveryChannelName}".format(
            customerId=customer_id,
            deliveryChannelName=delivery_channel_name,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeliveryChannelPolicyHydraCollection]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeliveryChannelPolicyHydraCollection.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeliveryChannelPolicyHydraCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    delivery_channel_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeliveryChannelPolicyHydraCollection]:
    """Get a collection of the customer's delivery channel policies for a specific channel

    Args:
        customer_id (int):
        delivery_channel_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryChannelPolicyHydraCollection]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    delivery_channel_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeliveryChannelPolicyHydraCollection]:
    """Get a collection of the customer's delivery channel policies for a specific channel

    Args:
        customer_id (int):
        delivery_channel_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryChannelPolicyHydraCollection
    """

    return sync_detailed(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    delivery_channel_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeliveryChannelPolicyHydraCollection]:
    """Get a collection of the customer's delivery channel policies for a specific channel

    Args:
        customer_id (int):
        delivery_channel_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryChannelPolicyHydraCollection]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    delivery_channel_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeliveryChannelPolicyHydraCollection]:
    """Get a collection of the customer's delivery channel policies for a specific channel

    Args:
        customer_id (int):
        delivery_channel_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryChannelPolicyHydraCollection
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            delivery_channel_name=delivery_channel_name,
            client=client,
        )
    ).parsed
