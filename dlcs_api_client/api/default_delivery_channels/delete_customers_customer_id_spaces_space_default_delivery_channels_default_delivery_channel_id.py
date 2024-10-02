from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response


def _get_kwargs(
    customer_id: int,
    space: int = 0,
    default_delivery_channel_id: str,

) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "delete",
        "url": "/customers/{customerId}/spaces/{space}/defaultDeliveryChannels/{defaultDeliveryChannelId}".format(customerId=customer_id,space=space,defaultDeliveryChannelId=default_delivery_channel_id,),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ProblemDetails]]:
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

) -> Response[Union[Any, ProblemDetails]]:
    """ Delete an individual customer accessible default delivery channel (customer specific + system)

    Args:
        customer_id (int):
        space (int):
        default_delivery_channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        customer_id=customer_id,
space=space,
default_delivery_channel_id=default_delivery_channel_id,

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

) -> Optional[Union[Any, ProblemDetails]]:
    """ Delete an individual customer accessible default delivery channel (customer specific + system)

    Args:
        customer_id (int):
        space (int):
        default_delivery_channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
     """


    return sync_detailed(
        customer_id=customer_id,
space=space,
default_delivery_channel_id=default_delivery_channel_id,
client=client,

    ).parsed

async def asyncio_detailed(
    customer_id: int,
    space: int = 0,
    default_delivery_channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, ProblemDetails]]:
    """ Delete an individual customer accessible default delivery channel (customer specific + system)

    Args:
        customer_id (int):
        space (int):
        default_delivery_channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        customer_id=customer_id,
space=space,
default_delivery_channel_id=default_delivery_channel_id,

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

) -> Optional[Union[Any, ProblemDetails]]:
    """ Delete an individual customer accessible default delivery channel (customer specific + system)

    Args:
        customer_id (int):
        space (int):
        default_delivery_channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
     """


    return (await asyncio_detailed(
        customer_id=customer_id,
space=space,
default_delivery_channel_id=default_delivery_channel_id,
client=client,

    )).parsed
