from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_origin_strategy import CustomerOriginStrategy
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    customer_id: int,
    *,
    json_body: CustomerOriginStrategy,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/customers/{customerId}/originStrategies".format(
            customerId=customer_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = Error.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error]]:
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
    json_body: CustomerOriginStrategy,
) -> Response[Union[Any, Error]]:
    r"""Update an origin strategy owned by the user

     Sample request:
        POST: /customers/1/originStrategies
        {
             \"regex\": \"http[s]?://(.*).my-regex.com\",
             \"order\": \"1\",
             \"strategy\": \"basic-http-authentication\",
             \"credentials\": \"{ \\"user\\": \\"my-username\\", \\"password\\": \\"my-password\\" }\",
             \"optimised\": \"false\"
        }

    Args:
        customer_id (int):
        json_body (CustomerOriginStrategy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomerOriginStrategy,
) -> Optional[Union[Any, Error]]:
    r"""Update an origin strategy owned by the user

     Sample request:
        POST: /customers/1/originStrategies
        {
             \"regex\": \"http[s]?://(.*).my-regex.com\",
             \"order\": \"1\",
             \"strategy\": \"basic-http-authentication\",
             \"credentials\": \"{ \\"user\\": \\"my-username\\", \\"password\\": \\"my-password\\" }\",
             \"optimised\": \"false\"
        }

    Args:
        customer_id (int):
        json_body (CustomerOriginStrategy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomerOriginStrategy,
) -> Response[Union[Any, Error]]:
    r"""Update an origin strategy owned by the user

     Sample request:
        POST: /customers/1/originStrategies
        {
             \"regex\": \"http[s]?://(.*).my-regex.com\",
             \"order\": \"1\",
             \"strategy\": \"basic-http-authentication\",
             \"credentials\": \"{ \\"user\\": \\"my-username\\", \\"password\\": \\"my-password\\" }\",
             \"optimised\": \"false\"
        }

    Args:
        customer_id (int):
        json_body (CustomerOriginStrategy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomerOriginStrategy,
) -> Optional[Union[Any, Error]]:
    r"""Update an origin strategy owned by the user

     Sample request:
        POST: /customers/1/originStrategies
        {
             \"regex\": \"http[s]?://(.*).my-regex.com\",
             \"order\": \"1\",
             \"strategy\": \"basic-http-authentication\",
             \"credentials\": \"{ \\"user\\": \\"my-username\\", \\"password\\": \\"my-password\\" }\",
             \"optimised\": \"false\"
        }

    Args:
        customer_id (int):
        json_body (CustomerOriginStrategy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
