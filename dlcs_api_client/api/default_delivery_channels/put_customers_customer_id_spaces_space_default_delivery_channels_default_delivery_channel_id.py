from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_delivery_channel import DefaultDeliveryChannel
from ...types import UNSET, Response


def _get_kwargs(
    customer_id: int,
    space: int = 0,
    default_delivery_channel_id: str,
    *,
    json_body: DefaultDeliveryChannel,

) -> Dict[str, Any]:
    

    cookies = {}


    

    json_json_body = json_body.to_dict()



    

    return {
        "method": "put",
        "url": "/customers/{customerId}/spaces/{space}/defaultDeliveryChannels/{defaultDeliveryChannelId}".format(customerId=customer_id,space=space,defaultDeliveryChannelId=default_delivery_channel_id,),
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DefaultDeliveryChannel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DefaultDeliveryChannel.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DefaultDeliveryChannel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    space: int = 0,
    default_delivery_channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DefaultDeliveryChannel,

) -> Response[DefaultDeliveryChannel]:
    """ Update a default delivery channel

    Args:
        customer_id (int):
        space (int):
        default_delivery_channel_id (str):
        json_body (DefaultDeliveryChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DefaultDeliveryChannel]
     """


    kwargs = _get_kwargs(
        customer_id=customer_id,
space=space,
default_delivery_channel_id=default_delivery_channel_id,
json_body=json_body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    customer_id: int,
    space: int = 0,
    default_delivery_channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DefaultDeliveryChannel,

) -> Optional[DefaultDeliveryChannel]:
    """ Update a default delivery channel

    Args:
        customer_id (int):
        space (int):
        default_delivery_channel_id (str):
        json_body (DefaultDeliveryChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DefaultDeliveryChannel
     """


    return sync_detailed(
        customer_id=customer_id,
space=space,
default_delivery_channel_id=default_delivery_channel_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    customer_id: int,
    space: int = 0,
    default_delivery_channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DefaultDeliveryChannel,

) -> Response[DefaultDeliveryChannel]:
    """ Update a default delivery channel

    Args:
        customer_id (int):
        space (int):
        default_delivery_channel_id (str):
        json_body (DefaultDeliveryChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DefaultDeliveryChannel]
     """


    kwargs = _get_kwargs(
        customer_id=customer_id,
space=space,
default_delivery_channel_id=default_delivery_channel_id,
json_body=json_body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    customer_id: int,
    space: int = 0,
    default_delivery_channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DefaultDeliveryChannel,

) -> Optional[DefaultDeliveryChannel]:
    """ Update a default delivery channel

    Args:
        customer_id (int):
        space (int):
        default_delivery_channel_id (str):
        json_body (DefaultDeliveryChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DefaultDeliveryChannel
     """


    return (await asyncio_detailed(
        customer_id=customer_id,
space=space,
default_delivery_channel_id=default_delivery_channel_id,
client=client,
json_body=json_body,

    )).parsed
