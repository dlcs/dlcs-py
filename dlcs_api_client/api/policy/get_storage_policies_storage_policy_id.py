from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.storage_policy import StoragePolicy
from ...types import Response


def _get_kwargs(
    storage_policy_id: str,
) -> Dict[str, Any]:

    pass

    return {
        "method": "get",
        "url": "/storagePolicies/{storagePolicyId}".format(
            storagePolicyId=storage_policy_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, StoragePolicy]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StoragePolicy.from_dict(response.json())

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
) -> Response[Union[Error, StoragePolicy]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_policy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, StoragePolicy]]:
    """Get details of specified storage policy

    Args:
        storage_policy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, StoragePolicy]]
    """

    kwargs = _get_kwargs(
        storage_policy_id=storage_policy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_policy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, StoragePolicy]]:
    """Get details of specified storage policy

    Args:
        storage_policy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, StoragePolicy]
    """

    return sync_detailed(
        storage_policy_id=storage_policy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_policy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, StoragePolicy]]:
    """Get details of specified storage policy

    Args:
        storage_policy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, StoragePolicy]]
    """

    kwargs = _get_kwargs(
        storage_policy_id=storage_policy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_policy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, StoragePolicy]]:
    """Get details of specified storage policy

    Args:
        storage_policy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, StoragePolicy]
    """

    return (
        await asyncio_detailed(
            storage_policy_id=storage_policy_id,
            client=client,
        )
    ).parsed
