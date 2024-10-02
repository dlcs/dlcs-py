from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delivery_channel_policy import DeliveryChannelPolicy
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    customer_id: int,
    delivery_channel_name: str,
    delivery_channel_policy_name: str,
    *,
    json_body: DeliveryChannelPolicy,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/customers/{customerId}/deliveryChannelPolicies/{deliveryChannelName}/{deliveryChannelPolicyName}".format(
            customerId=customer_id,
            deliveryChannelName=delivery_channel_name,
            deliveryChannelPolicyName=delivery_channel_policy_name,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeliveryChannelPolicy, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeliveryChannelPolicy.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DeliveryChannelPolicy, Error]]:
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
    json_body: DeliveryChannelPolicy,
) -> Response[Union[Any, DeliveryChannelPolicy, Error]]:
    r"""Create or update a specified customer delivery channel policy - \"name\" must be specified in URI

     Sample request:

        PUT: /customers/1/deliveryChannelPolicies/iiif-av/my-video-policy
        {
            \"displayName\": \"My Updated Video Policy\",
            \"policyData\": \"[\"video-mp4-720p\"]\"
        }

    Args:
        customer_id (int):
        delivery_channel_name (str):
        delivery_channel_policy_name (str):
        json_body (DeliveryChannelPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeliveryChannelPolicy, Error]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
        delivery_channel_policy_name=delivery_channel_policy_name,
        json_body=json_body,
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
    json_body: DeliveryChannelPolicy,
) -> Optional[Union[Any, DeliveryChannelPolicy, Error]]:
    r"""Create or update a specified customer delivery channel policy - \"name\" must be specified in URI

     Sample request:

        PUT: /customers/1/deliveryChannelPolicies/iiif-av/my-video-policy
        {
            \"displayName\": \"My Updated Video Policy\",
            \"policyData\": \"[\"video-mp4-720p\"]\"
        }

    Args:
        customer_id (int):
        delivery_channel_name (str):
        delivery_channel_policy_name (str):
        json_body (DeliveryChannelPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeliveryChannelPolicy, Error]
    """

    return sync_detailed(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
        delivery_channel_policy_name=delivery_channel_policy_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    delivery_channel_name: str,
    delivery_channel_policy_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DeliveryChannelPolicy,
) -> Response[Union[Any, DeliveryChannelPolicy, Error]]:
    r"""Create or update a specified customer delivery channel policy - \"name\" must be specified in URI

     Sample request:

        PUT: /customers/1/deliveryChannelPolicies/iiif-av/my-video-policy
        {
            \"displayName\": \"My Updated Video Policy\",
            \"policyData\": \"[\"video-mp4-720p\"]\"
        }

    Args:
        customer_id (int):
        delivery_channel_name (str):
        delivery_channel_policy_name (str):
        json_body (DeliveryChannelPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeliveryChannelPolicy, Error]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        delivery_channel_name=delivery_channel_name,
        delivery_channel_policy_name=delivery_channel_policy_name,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    delivery_channel_name: str,
    delivery_channel_policy_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DeliveryChannelPolicy,
) -> Optional[Union[Any, DeliveryChannelPolicy, Error]]:
    r"""Create or update a specified customer delivery channel policy - \"name\" must be specified in URI

     Sample request:

        PUT: /customers/1/deliveryChannelPolicies/iiif-av/my-video-policy
        {
            \"displayName\": \"My Updated Video Policy\",
            \"policyData\": \"[\"video-mp4-720p\"]\"
        }

    Args:
        customer_id (int):
        delivery_channel_name (str):
        delivery_channel_policy_name (str):
        json_body (DeliveryChannelPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeliveryChannelPolicy, Error]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            delivery_channel_name=delivery_channel_name,
            delivery_channel_policy_name=delivery_channel_policy_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
