from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_delivery_channel import DefaultDeliveryChannel
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    customer_id: int,
    space: int = 0,
    *,
    json_body: DefaultDeliveryChannel,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/customers/{customerId}/spaces/{space}/defaultDeliveryChannels".format(
            customerId=customer_id,
            space=space,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
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
    space: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DefaultDeliveryChannel,
) -> Response[Union[Any, ProblemDetails]]:
    """Create a single default delivery channel

    Args:
        customer_id (int):
        space (int):
        json_body (DefaultDeliveryChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space=space,
        json_body=json_body,
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
    json_body: DefaultDeliveryChannel,
) -> Optional[Union[Any, ProblemDetails]]:
    """Create a single default delivery channel

    Args:
        customer_id (int):
        space (int):
        json_body (DefaultDeliveryChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        customer_id=customer_id,
        space=space,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    space: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DefaultDeliveryChannel,
) -> Response[Union[Any, ProblemDetails]]:
    """Create a single default delivery channel

    Args:
        customer_id (int):
        space (int):
        json_body (DefaultDeliveryChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space=space,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    space: int = 0,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DefaultDeliveryChannel,
) -> Optional[Union[Any, ProblemDetails]]:
    """Create a single default delivery channel

    Args:
        customer_id (int):
        space (int):
        json_body (DefaultDeliveryChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            space=space,
            client=client,
            json_body=json_body,
        )
    ).parsed
