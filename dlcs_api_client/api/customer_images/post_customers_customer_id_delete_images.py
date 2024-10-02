from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identifier_only_hydra_collection import IdentifierOnlyHydraCollection
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: int,
    *,
    json_body: IdentifierOnlyHydraCollection,
    delete_from: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["deleteFrom"] = delete_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/customers/{customerId}/deleteImages".format(
            customerId=customer_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
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
    json_body: IdentifierOnlyHydraCollection,
    delete_from: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    r"""Accepts a list of image identifiers, will delete those that exist from DB

     Sample request:

        POST: /customers/1/deleteImages
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
        delete_from (Union[Unset, None, str]):
        json_body (IdentifierOnlyHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        json_body=json_body,
        delete_from=delete_from,
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
    delete_from: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    r"""Accepts a list of image identifiers, will delete those that exist from DB

     Sample request:

        POST: /customers/1/deleteImages
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
        delete_from (Union[Unset, None, str]):
        json_body (IdentifierOnlyHydraCollection):

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
        delete_from=delete_from,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IdentifierOnlyHydraCollection,
    delete_from: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    r"""Accepts a list of image identifiers, will delete those that exist from DB

     Sample request:

        POST: /customers/1/deleteImages
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
        delete_from (Union[Unset, None, str]):
        json_body (IdentifierOnlyHydraCollection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        json_body=json_body,
        delete_from=delete_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IdentifierOnlyHydraCollection,
    delete_from: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    r"""Accepts a list of image identifiers, will delete those that exist from DB

     Sample request:

        POST: /customers/1/deleteImages
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
        delete_from (Union[Unset, None, str]):
        json_body (IdentifierOnlyHydraCollection):

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
            delete_from=delete_from,
        )
    ).parsed
