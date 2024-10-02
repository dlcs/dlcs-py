from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.identifier_only_hydra_collection import IdentifierOnlyHydraCollection
from ...models.image_hydra_collection import ImageHydraCollection
from ...types import Response


def _get_kwargs(
    customer_id: int,
    *,
    json_body: IdentifierOnlyHydraCollection,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/customers/{customerId}/allImages".format(
            customerId=customer_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ImageHydraCollection]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImageHydraCollection.from_dict(response.json())

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
) -> Response[Union[Error, ImageHydraCollection]]:
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
    json_body: IdentifierOnlyHydraCollection,
) -> Response[Union[Error, ImageHydraCollection]]:
    r"""Accepts a list of image identifiers, will return a list of matching images.

    This endpoint doesn't support paging - all results are returned in single page

     Sample request:

        POST: /customers/1/allImages
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\":\"Collection\",
            \"member\": [
                { \"id\": \"1/1/foo\" },
                { \"id\": \"1/99/bar\" }
            ]
        }

    Args:
        customer_id (int):
        json_body (IdentifierOnlyHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ImageHydraCollection]]
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
    json_body: IdentifierOnlyHydraCollection,
) -> Optional[Union[Error, ImageHydraCollection]]:
    r"""Accepts a list of image identifiers, will return a list of matching images.

    This endpoint doesn't support paging - all results are returned in single page

     Sample request:

        POST: /customers/1/allImages
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\":\"Collection\",
            \"member\": [
                { \"id\": \"1/1/foo\" },
                { \"id\": \"1/99/bar\" }
            ]
        }

    Args:
        customer_id (int):
        json_body (IdentifierOnlyHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ImageHydraCollection]
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
    json_body: IdentifierOnlyHydraCollection,
) -> Response[Union[Error, ImageHydraCollection]]:
    r"""Accepts a list of image identifiers, will return a list of matching images.

    This endpoint doesn't support paging - all results are returned in single page

     Sample request:

        POST: /customers/1/allImages
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\":\"Collection\",
            \"member\": [
                { \"id\": \"1/1/foo\" },
                { \"id\": \"1/99/bar\" }
            ]
        }

    Args:
        customer_id (int):
        json_body (IdentifierOnlyHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ImageHydraCollection]]
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
    json_body: IdentifierOnlyHydraCollection,
) -> Optional[Union[Error, ImageHydraCollection]]:
    r"""Accepts a list of image identifiers, will return a list of matching images.

    This endpoint doesn't support paging - all results are returned in single page

     Sample request:

        POST: /customers/1/allImages
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\":\"Collection\",
            \"member\": [
                { \"id\": \"1/1/foo\" },
                { \"id\": \"1/99/bar\" }
            ]
        }

    Args:
        customer_id (int):
        json_body (IdentifierOnlyHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ImageHydraCollection]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
