from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    customer_id: int,
    delivery_channel_name: str,
    delivery_channel_policy_name: str,
) -> Dict[str, Any]:

    pass

    return {
        "method": "delete",
        "url": "/customers/{customerId}/deliveryChannelPolicies/{deliveryChannelName}/{deliveryChannelPolicyName}".format(
            customerId=customer_id,
            deliveryChannelName=delivery_channel_name,
            deliveryChannelPolicyName=delivery_channel_policy_name,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, None)
        return response_202
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
    delivery_channel_name: str,
    delivery_channel_policy_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ProblemDetails]]:
    """Delete a specified delivery channel policy

    Args:
        customer_id (int):
        delivery_channel_name (str):
        delivery_channel_policy_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
        delivery_channel_policy_name=delivery_channel_policy_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    delivery_channel_name: str,
    delivery_channel_policy_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete a specified delivery channel policy

    Args:
        customer_id (int):
        delivery_channel_name (str):
        delivery_channel_policy_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
        delivery_channel_policy_name=delivery_channel_policy_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    delivery_channel_name: str,
    delivery_channel_policy_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ProblemDetails]]:
    """Delete a specified delivery channel policy

    Args:
        customer_id (int):
        delivery_channel_name (str):
        delivery_channel_policy_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
        delivery_channel_policy_name=delivery_channel_policy_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    delivery_channel_name: str,
    delivery_channel_policy_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete a specified delivery channel policy

    Args:
        customer_id (int):
        delivery_channel_name (str):
        delivery_channel_policy_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            delivery_channel_name=delivery_channel_name,
            delivery_channel_policy_name=delivery_channel_policy_name,
            client=client,
        )
    ).parsed
