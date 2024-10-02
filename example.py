from dlcs_api_client import AuthenticatedClient, submit_batch
from dlcs_api_client.models import ImageHydraCollection

client = AuthenticatedClient(base_url="https://dlcs.digirati.io", token="xxx", prefix="Basic")
response = submit_batch(client=client, customer_id=1, json_body=ImageHydraCollection(
    members=[],
))
