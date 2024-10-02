from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.space import Space
from ...types import Response


def _get_kwargs(
    customer_id: int,
    space_id: int,
    *,
    json_body: Space,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/customers/{customerId}/spaces/{spaceId}".format(
            customerId=customer_id,
            spaceId=space_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails, Space]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Space.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProblemDetails, Space]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    space_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Space,
) -> Response[Union[Any, ProblemDetails, Space]]:
    r"""Create or update a space within this customer. A new space's ID is set by the user in the URL.

     Sample request:

        PUT: /customers/1/spaces/1
        {
            \"@type\":\"Space\",
            \"name\":\"foo\"
        }

    Args:
        customer_id (int):
        space_id (int):
        json_body (Space):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, Space]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space_id=space_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    space_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Space,
) -> Optional[Union[Any, ProblemDetails, Space]]:
    r"""Create or update a space within this customer. A new space's ID is set by the user in the URL.

     Sample request:

        PUT: /customers/1/spaces/1
        {
            \"@type\":\"Space\",
            \"name\":\"foo\"
        }

    Args:
        customer_id (int):
        space_id (int):
        json_body (Space):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, Space]
    """

    return sync_detailed(
        customer_id=customer_id,
        space_id=space_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    space_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Space,
) -> Response[Union[Any, ProblemDetails, Space]]:
    r"""Create or update a space within this customer. A new space's ID is set by the user in the URL.

     Sample request:

        PUT: /customers/1/spaces/1
        {
            \"@type\":\"Space\",
            \"name\":\"foo\"
        }

    Args:
        customer_id (int):
        space_id (int):
        json_body (Space):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, Space]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space_id=space_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    space_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Space,
) -> Optional[Union[Any, ProblemDetails, Space]]:
    r"""Create or update a space within this customer. A new space's ID is set by the user in the URL.

     Sample request:

        PUT: /customers/1/spaces/1
        {
            \"@type\":\"Space\",
            \"name\":\"foo\"
        }

    Args:
        customer_id (int):
        space_id (int):
        json_body (Space):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, Space]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            space_id=space_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
