from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.origin_strategy import OriginStrategy
from ...types import Response


def _get_kwargs(
    origin_strategy_id: str,
) -> Dict[str, Any]:

    pass

    return {
        "method": "get",
        "url": "/originStrategies/{originStrategyId}".format(
            originStrategyId=origin_strategy_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, OriginStrategy]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OriginStrategy.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, OriginStrategy]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    origin_strategy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, OriginStrategy]]:
    """Get details of specified origin strategy

    Args:
        origin_strategy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, OriginStrategy]]
    """

    kwargs = _get_kwargs(
        origin_strategy_id=origin_strategy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    origin_strategy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, OriginStrategy]]:
    """Get details of specified origin strategy

    Args:
        origin_strategy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, OriginStrategy]
    """

    return sync_detailed(
        origin_strategy_id=origin_strategy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    origin_strategy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, OriginStrategy]]:
    """Get details of specified origin strategy

    Args:
        origin_strategy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, OriginStrategy]]
    """

    kwargs = _get_kwargs(
        origin_strategy_id=origin_strategy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    origin_strategy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, OriginStrategy]]:
    """Get details of specified origin strategy

    Args:
        origin_strategy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, OriginStrategy]
    """

    return (
        await asyncio_detailed(
            origin_strategy_id=origin_strategy_id,
            client=client,
        )
    ).parsed
