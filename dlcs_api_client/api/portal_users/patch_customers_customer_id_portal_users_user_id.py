from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.portal_user import PortalUser
from ...types import Response


def _get_kwargs(
    customer_id: int,
    user_id: str,
    *,
    json_body: PortalUser,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/customers/{customerId}/portalUsers/{userId}".format(
            customerId=customer_id,
            userId=user_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PortalUser]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PortalUser.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, PortalUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: PortalUser,
) -> Response[Union[Error, PortalUser]]:
    """PATCH /customers/{customerId}/portalUsers/{userId}

    Args:
        customer_id (int):
        user_id (str):
        json_body (PortalUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PortalUser]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        user_id=user_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: PortalUser,
) -> Optional[Union[Error, PortalUser]]:
    """PATCH /customers/{customerId}/portalUsers/{userId}

    Args:
        customer_id (int):
        user_id (str):
        json_body (PortalUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PortalUser]
    """

    return sync_detailed(
        customer_id=customer_id,
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: PortalUser,
) -> Response[Union[Error, PortalUser]]:
    """PATCH /customers/{customerId}/portalUsers/{userId}

    Args:
        customer_id (int):
        user_id (str):
        json_body (PortalUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PortalUser]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        user_id=user_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: PortalUser,
) -> Optional[Union[Error, PortalUser]]:
    """PATCH /customers/{customerId}/portalUsers/{userId}

    Args:
        customer_id (int):
        user_id (str):
        json_body (PortalUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PortalUser]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
