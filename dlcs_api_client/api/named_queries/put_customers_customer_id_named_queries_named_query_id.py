from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.named_query import NamedQuery
from ...types import Response


def _get_kwargs(
    customer_id: int,
    named_query_id: str,
    *,
    json_body: NamedQuery,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/customers/{customerId}/namedQueries/{namedQueryId}".format(
            customerId=customer_id,
            namedQueryId=named_query_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, NamedQuery]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NamedQuery.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, NamedQuery]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    named_query_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NamedQuery,
) -> Response[Union[Error, NamedQuery]]:
    r"""Update an existing Named Query owned by the user - currently, only the template can be modified

     Sample request:

        PUT: /customers/1/namedQueries/a90d6e44-4cdb-410b-999e-30c2ea3955b2
        {
            \"template\":\"space=example-updated\"
        }

    Args:
        customer_id (int):
        named_query_id (str):
        json_body (NamedQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, NamedQuery]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        named_query_id=named_query_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    named_query_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NamedQuery,
) -> Optional[Union[Error, NamedQuery]]:
    r"""Update an existing Named Query owned by the user - currently, only the template can be modified

     Sample request:

        PUT: /customers/1/namedQueries/a90d6e44-4cdb-410b-999e-30c2ea3955b2
        {
            \"template\":\"space=example-updated\"
        }

    Args:
        customer_id (int):
        named_query_id (str):
        json_body (NamedQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, NamedQuery]
    """

    return sync_detailed(
        customer_id=customer_id,
        named_query_id=named_query_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    named_query_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NamedQuery,
) -> Response[Union[Error, NamedQuery]]:
    r"""Update an existing Named Query owned by the user - currently, only the template can be modified

     Sample request:

        PUT: /customers/1/namedQueries/a90d6e44-4cdb-410b-999e-30c2ea3955b2
        {
            \"template\":\"space=example-updated\"
        }

    Args:
        customer_id (int):
        named_query_id (str):
        json_body (NamedQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, NamedQuery]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        named_query_id=named_query_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    named_query_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NamedQuery,
) -> Optional[Union[Error, NamedQuery]]:
    r"""Update an existing Named Query owned by the user - currently, only the template can be modified

     Sample request:

        PUT: /customers/1/namedQueries/a90d6e44-4cdb-410b-999e-30c2ea3955b2
        {
            \"template\":\"space=example-updated\"
        }

    Args:
        customer_id (int):
        named_query_id (str):
        json_body (NamedQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, NamedQuery]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            named_query_id=named_query_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
