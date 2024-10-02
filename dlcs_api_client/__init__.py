""" A client library for accessing DLCS API """

from .api.customer_queue.post_customers_customer_id_queue import sync_detailed as submit_batch, \
    asyncio_detailed as submit_batch_async
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
    "submit_batch",
    "submit_batch_async"
)
