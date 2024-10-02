from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image import Image
from ...models.image_with_file import ImageWithFile
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    json_body: ImageWithFile,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/customers/{customerId}/spaces/{spaceId}/images/{imageId}".format(
            customerId=customer_id,
            spaceId=space_id,
            imageId=image_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Image, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Image.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Image.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
        response_405 = ProblemDetails.from_dict(response.json())

        return response_405
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INSUFFICIENT_STORAGE:
        response_507 = ProblemDetails.from_dict(response.json())

        return response_507
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = ProblemDetails.from_dict(response.json())

        return response_501
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ProblemDetails.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Image, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ImageWithFile,
) -> Response[Union[Image, ProblemDetails]]:
    r"""Create or update asset at specified ID.

    PUT requests always trigger reingesting of asset - in general batch processing should be preferred.

    Image + File assets are ingested synchronously. Timebased assets are ingested asynchronously.

    \"File\" property should be base64 encoded image, if included.

     Sample request:

        PUT: /customers/1/spaces/1/images/my-image
        {
            \"@type\":\"Image\",
            \"family\": \"I\",
            \"origin\": \"https://example.text/.../image.jpeg\",
            \"mediaType\": \"image/jpeg\",
            \"string1\": \"my-metadata\"
        }

    Args:
        customer_id (int):
        space_id (int):
        image_id (str):
        json_body (ImageWithFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Image, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space_id=space_id,
        image_id=image_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ImageWithFile,
) -> Optional[Union[Image, ProblemDetails]]:
    r"""Create or update asset at specified ID.

    PUT requests always trigger reingesting of asset - in general batch processing should be preferred.

    Image + File assets are ingested synchronously. Timebased assets are ingested asynchronously.

    \"File\" property should be base64 encoded image, if included.

     Sample request:

        PUT: /customers/1/spaces/1/images/my-image
        {
            \"@type\":\"Image\",
            \"family\": \"I\",
            \"origin\": \"https://example.text/.../image.jpeg\",
            \"mediaType\": \"image/jpeg\",
            \"string1\": \"my-metadata\"
        }

    Args:
        customer_id (int):
        space_id (int):
        image_id (str):
        json_body (ImageWithFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Image, ProblemDetails]
    """

    return sync_detailed(
        customer_id=customer_id,
        space_id=space_id,
        image_id=image_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ImageWithFile,
) -> Response[Union[Image, ProblemDetails]]:
    r"""Create or update asset at specified ID.

    PUT requests always trigger reingesting of asset - in general batch processing should be preferred.

    Image + File assets are ingested synchronously. Timebased assets are ingested asynchronously.

    \"File\" property should be base64 encoded image, if included.

     Sample request:

        PUT: /customers/1/spaces/1/images/my-image
        {
            \"@type\":\"Image\",
            \"family\": \"I\",
            \"origin\": \"https://example.text/.../image.jpeg\",
            \"mediaType\": \"image/jpeg\",
            \"string1\": \"my-metadata\"
        }

    Args:
        customer_id (int):
        space_id (int):
        image_id (str):
        json_body (ImageWithFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Image, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        space_id=space_id,
        image_id=image_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    space_id: int,
    image_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ImageWithFile,
) -> Optional[Union[Image, ProblemDetails]]:
    r"""Create or update asset at specified ID.

    PUT requests always trigger reingesting of asset - in general batch processing should be preferred.

    Image + File assets are ingested synchronously. Timebased assets are ingested asynchronously.

    \"File\" property should be base64 encoded image, if included.

     Sample request:

        PUT: /customers/1/spaces/1/images/my-image
        {
            \"@type\":\"Image\",
            \"family\": \"I\",
            \"origin\": \"https://example.text/.../image.jpeg\",
            \"mediaType\": \"image/jpeg\",
            \"string1\": \"my-metadata\"
        }

    Args:
        customer_id (int):
        space_id (int):
        image_id (str):
        json_body (ImageWithFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Image, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            space_id=space_id,
            image_id=image_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
