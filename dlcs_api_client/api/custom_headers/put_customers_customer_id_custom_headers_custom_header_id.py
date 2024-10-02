from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_header import CustomHeader
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    customer_id: int,
    custom_header_id: str,
    *,
    json_body: CustomHeader,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/customers/{customerId}/customHeaders/{customHeaderId}".format(
            customerId=customer_id,
            customHeaderId=custom_header_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CustomHeader, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CustomHeader.from_dict(response.json())

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
) -> Response[Union[CustomHeader, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    custom_header_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomHeader,
) -> Response[Union[CustomHeader, Error]]:
    r"""Update an existing Custom Header owned by the calling user

     Sample request:

        PUT: /customers/1/customHeaders/3abc55fd-eb2d-47e8-8966-5f71d8e26476
        {
            \"key\": \"my-new-key\",
            \"value\": \"my-new-value\"
            (optional) \"space\": 2
            (optional) \"role\": \"https://api.dlcs.digirati.io/customers/1/roles/my-new-role\"
        }

    Args:
        customer_id (int):
        custom_header_id (str):
        json_body (CustomHeader):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomHeader, Error]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        custom_header_id=custom_header_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    custom_header_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomHeader,
) -> Optional[Union[CustomHeader, Error]]:
    r"""Update an existing Custom Header owned by the calling user

     Sample request:

        PUT: /customers/1/customHeaders/3abc55fd-eb2d-47e8-8966-5f71d8e26476
        {
            \"key\": \"my-new-key\",
            \"value\": \"my-new-value\"
            (optional) \"space\": 2
            (optional) \"role\": \"https://api.dlcs.digirati.io/customers/1/roles/my-new-role\"
        }

    Args:
        customer_id (int):
        custom_header_id (str):
        json_body (CustomHeader):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomHeader, Error]
    """

    return sync_detailed(
        customer_id=customer_id,
        custom_header_id=custom_header_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    custom_header_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomHeader,
) -> Response[Union[CustomHeader, Error]]:
    r"""Update an existing Custom Header owned by the calling user

     Sample request:

        PUT: /customers/1/customHeaders/3abc55fd-eb2d-47e8-8966-5f71d8e26476
        {
            \"key\": \"my-new-key\",
            \"value\": \"my-new-value\"
            (optional) \"space\": 2
            (optional) \"role\": \"https://api.dlcs.digirati.io/customers/1/roles/my-new-role\"
        }

    Args:
        customer_id (int):
        custom_header_id (str):
        json_body (CustomHeader):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomHeader, Error]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        custom_header_id=custom_header_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    custom_header_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomHeader,
) -> Optional[Union[CustomHeader, Error]]:
    r"""Update an existing Custom Header owned by the calling user

     Sample request:

        PUT: /customers/1/customHeaders/3abc55fd-eb2d-47e8-8966-5f71d8e26476
        {
            \"key\": \"my-new-key\",
            \"value\": \"my-new-value\"
            (optional) \"space\": 2
            (optional) \"role\": \"https://api.dlcs.digirati.io/customers/1/roles/my-new-role\"
        }

    Args:
        customer_id (int):
        custom_header_id (str):
        json_body (CustomHeader):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomHeader, Error]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            custom_header_id=custom_header_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
