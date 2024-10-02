from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: int,
    query_name: str,
    *,
    args: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["args"] = args

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": "/customers/{customerId}/resources/pdf/{queryName}".format(
            customerId=customer_id,
            queryName=query_name,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
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
    query_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    args: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Deletes PDF generated for queryName using specified arguments.
    This deletes both the control-file and PDF projection.

     Sample request:

        DELETE /customers/2/resources/pdf/my-named-query?args=1/10/teststring

    Args:
        customer_id (int):
        query_name (str):
        args (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        query_name=query_name,
        args=args,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: int,
    query_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    args: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Deletes PDF generated for queryName using specified arguments.
    This deletes both the control-file and PDF projection.

     Sample request:

        DELETE /customers/2/resources/pdf/my-named-query?args=1/10/teststring

    Args:
        customer_id (int):
        query_name (str):
        args (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        customer_id=customer_id,
        query_name=query_name,
        client=client,
        args=args,
    ).parsed


async def asyncio_detailed(
    customer_id: int,
    query_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    args: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Deletes PDF generated for queryName using specified arguments.
    This deletes both the control-file and PDF projection.

     Sample request:

        DELETE /customers/2/resources/pdf/my-named-query?args=1/10/teststring

    Args:
        customer_id (int):
        query_name (str):
        args (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        query_name=query_name,
        args=args,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: int,
    query_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    args: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Deletes PDF generated for queryName using specified arguments.
    This deletes both the control-file and PDF projection.

     Sample request:

        DELETE /customers/2/resources/pdf/my-named-query?args=1/10/teststring

    Args:
        customer_id (int):
        query_name (str):
        args (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            query_name=query_name,
            client=client,
            args=args,
        )
    ).parsed
