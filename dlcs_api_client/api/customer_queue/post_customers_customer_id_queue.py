from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_hydra_collection import ImageHydraCollection
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    customer_id: int,
    *,
    json_body: ImageHydraCollection,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/customers/{customerId}/queue".format(
            customerId=customer_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProblemDetails]]:
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
    json_body: ImageHydraCollection,
) -> Response[Union[Any, ProblemDetails]]:
    r"""Create a batch of images to ingest.

    These will be enqueued for processing and asynchronously ingested

     Sample request:

        POST: /customers/99/queue
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\": \"Collection\",
            \"member\": [
            {
                \"id\": \"foo\",
                \"space\": 1,
                \"origin\": \"https://example.origin/foo.jpg\",
                \"family\": \"I\",
                \"mediaType\": \"image/jpeg\"
            },
            {
                \"id\": \"bar\",
                \"space\": 2,
                \"origin\": \"https://example.origin/movie.mp4\",
                \"family\": \"T\",
                \"mediaType\": \"video/mp4\"
            }
        }

    Args:
        customer_id (int):
        json_body (ImageHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
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
    json_body: ImageHydraCollection,
) -> Optional[Union[Any, ProblemDetails]]:
    r"""Create a batch of images to ingest.

    These will be enqueued for processing and asynchronously ingested

     Sample request:

        POST: /customers/99/queue
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\": \"Collection\",
            \"member\": [
            {
                \"id\": \"foo\",
                \"space\": 1,
                \"origin\": \"https://example.origin/foo.jpg\",
                \"family\": \"I\",
                \"mediaType\": \"image/jpeg\"
            },
            {
                \"id\": \"bar\",
                \"space\": 2,
                \"origin\": \"https://example.origin/movie.mp4\",
                \"family\": \"T\",
                \"mediaType\": \"video/mp4\"
            }
        }

    Args:
        customer_id (int):
        json_body (ImageHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
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
    json_body: ImageHydraCollection,
) -> Response[Union[Any, ProblemDetails]]:
    r"""Create a batch of images to ingest.

    These will be enqueued for processing and asynchronously ingested

     Sample request:

        POST: /customers/99/queue
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\": \"Collection\",
            \"member\": [
            {
                \"id\": \"foo\",
                \"space\": 1,
                \"origin\": \"https://example.origin/foo.jpg\",
                \"family\": \"I\",
                \"mediaType\": \"image/jpeg\"
            },
            {
                \"id\": \"bar\",
                \"space\": 2,
                \"origin\": \"https://example.origin/movie.mp4\",
                \"family\": \"T\",
                \"mediaType\": \"video/mp4\"
            }
        }

    Args:
        customer_id (int):
        json_body (ImageHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
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
    json_body: ImageHydraCollection,
) -> Optional[Union[Any, ProblemDetails]]:
    r"""Create a batch of images to ingest.

    These will be enqueued for processing and asynchronously ingested

     Sample request:

        POST: /customers/99/queue
        {
            \"@context\": \"http://www.w3.org/ns/hydra/context.jsonld\",
            \"@type\": \"Collection\",
            \"member\": [
            {
                \"id\": \"foo\",
                \"space\": 1,
                \"origin\": \"https://example.origin/foo.jpg\",
                \"family\": \"I\",
                \"mediaType\": \"image/jpeg\"
            },
            {
                \"id\": \"bar\",
                \"space\": 2,
                \"origin\": \"https://example.origin/movie.mp4\",
                \"family\": \"T\",
                \"mediaType\": \"video/mp4\"
            }
        }

    Args:
        customer_id (int):
        json_body (ImageHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
