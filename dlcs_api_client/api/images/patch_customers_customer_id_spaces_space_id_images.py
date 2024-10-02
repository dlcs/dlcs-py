from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.image_hydra_collection import ImageHydraCollection
from ...types import Response


def _get_kwargs(
    customer_id: int,
    space_id: int,
    *,
    json_body: ImageHydraCollection,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/customers/{customerId}/spaces/{spaceId}/images".format(
            customerId=customer_id,
            spaceId=space_id,
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
    space_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ImageHydraCollection,
) -> Response[Union[Error, ImageHydraCollection]]:
    r"""PATCH a collection of images.
    This is for bulk patch operations on images in the same space.

     Sample request:

        PATCH: /customers/1/spaces/5/images
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\": \"Collection\",
            \"member\": [
            {
                \"id\": \"identifier-1\",
                \"string3\": \"patched\"
            }]
        }

    Args:
        customer_id (int):
        space_id (int):
        json_body (ImageHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ImageHydraCollection]]
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
    json_body: ImageHydraCollection,
) -> Optional[Union[Error, ImageHydraCollection]]:
    r"""PATCH a collection of images.
    This is for bulk patch operations on images in the same space.

     Sample request:

        PATCH: /customers/1/spaces/5/images
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\": \"Collection\",
            \"member\": [
            {
                \"id\": \"identifier-1\",
                \"string3\": \"patched\"
            }]
        }

    Args:
        customer_id (int):
        space_id (int):
        json_body (ImageHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ImageHydraCollection]
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
    json_body: ImageHydraCollection,
) -> Response[Union[Error, ImageHydraCollection]]:
    r"""PATCH a collection of images.
    This is for bulk patch operations on images in the same space.

     Sample request:

        PATCH: /customers/1/spaces/5/images
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\": \"Collection\",
            \"member\": [
            {
                \"id\": \"identifier-1\",
                \"string3\": \"patched\"
            }]
        }

    Args:
        customer_id (int):
        space_id (int):
        json_body (ImageHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ImageHydraCollection]]
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
    json_body: ImageHydraCollection,
) -> Optional[Union[Error, ImageHydraCollection]]:
    r"""PATCH a collection of images.
    This is for bulk patch operations on images in the same space.

     Sample request:

        PATCH: /customers/1/spaces/5/images
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\": \"Collection\",
            \"member\": [
            {
                \"id\": \"identifier-1\",
                \"string3\": \"patched\"
            }]
        }

    Args:
        customer_id (int):
        space_id (int):
        json_body (ImageHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ImageHydraCollection]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            space_id=space_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
