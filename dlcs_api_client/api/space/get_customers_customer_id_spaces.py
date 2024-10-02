from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.space_hydra_collection import SpaceHydraCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: int,
    *,
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = -1,
    order_by: Union[Unset, None, str] = UNSET,
    order_by_descending: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["orderBy"] = order_by

    params["orderByDescending"] = order_by_descending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/customers/{customerId}/spaces".format(
            customerId=customer_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SpaceHydraCollection]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SpaceHydraCollection.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SpaceHydraCollection]:
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
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = -1,
    order_by: Union[Unset, None, str] = UNSET,
    order_by_descending: Union[Unset, None, str] = UNSET,
) -> Response[SpaceHydraCollection]:
    """Get details of all spaces for customer.

    Args:
        customer_id (int):
        page (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: -1.
        order_by (Union[Unset, None, str]):
        order_by_descending (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SpaceHydraCollection]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        page=page,
        page_size=page_size,
        order_by=order_by,
        order_by_descending=order_by_descending,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = -1,
    order_by: Union[Unset, None, str] = UNSET,
    order_by_descending: Union[Unset, None, str] = UNSET,
) -> Optional[SpaceHydraCollection]:
    """Get details of all spaces for customer.

    Args:
        customer_id (int):
        page (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: -1.
        order_by (Union[Unset, None, str]):
        order_by_descending (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SpaceHydraCollection
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        page=page,
        page_size=page_size,
        order_by=order_by,
        order_by_descending=order_by_descending,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = -1,
    order_by: Union[Unset, None, str] = UNSET,
    order_by_descending: Union[Unset, None, str] = UNSET,
) -> Response[SpaceHydraCollection]:
    """Get details of all spaces for customer.

    Args:
        customer_id (int):
        page (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: -1.
        order_by (Union[Unset, None, str]):
        order_by_descending (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SpaceHydraCollection]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        page=page,
        page_size=page_size,
        order_by=order_by,
        order_by_descending=order_by_descending,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = -1,
    order_by: Union[Unset, None, str] = UNSET,
    order_by_descending: Union[Unset, None, str] = UNSET,
) -> Optional[SpaceHydraCollection]:
    """Get details of all spaces for customer.

    Args:
        customer_id (int):
        page (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: -1.
        order_by (Union[Unset, None, str]):
        order_by_descending (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SpaceHydraCollection
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            page=page,
            page_size=page_size,
            order_by=order_by,
            order_by_descending=order_by_descending,
        )
    ).parsed
