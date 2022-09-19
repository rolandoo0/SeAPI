from decouple import config
import json
import aiohttp
from se_request import SeRequest


class ShipEngineWebhooks:
    """
    Class to handle all ShipEngine Webhooks.
    """

    def __init__(self, api_key: str = None) -> None:
        self.api_key = api_key

    async def create_webhook(self, webhook, event: str = "tracking"):
        """
        Set tracking webhooks.
        """
        url = "https://api.shipengine.com/v1/environment/webhooks"

        payload = json.dumps({"url": webhook, "event": event})
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        resp = await SeRequest.post(headers=headers, payload=payload, url=url)

        return resp

    async def delete_webhooks(self, webhook_id: str = None):
        """
        Delete tracking webhook.
        """
        payload = {}
        url = f"https://api.shipengine.com/v1/environment/webhooks{webhook_id}"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        resp = await SeRequest.delete(headers=headers, payload=payload, url=url)

        return resp

    async def list_webhooks(self):
        """
        Get all webhooks.
        """
        payload = {}
        url = f"https://api.shipengine.com/v1/environment/webhooks"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        resp = await SeRequest.get(headers=headers, payload=payload, url=url)

        return resp

    async def get_webhook(self, webhook_id: str = None):
        """
        Get tracking webhook.
        """
        payload = {}
        url = f"https://api.shipengine.com/v1/environment/webhooks{webhook_id}"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        resp = await SeRequest.get(headers=headers, payload=payload, url=url)

        return resp

    async def update_webhook(self, webhook_id: str = None, webhook_url: str = None):
        """
        Update tracking webhook.
        """
        payload = json.dumps({"url": webhook_url})
        url = f"https://api.shipengine.com/v1/environment/webhooks{webhook_id}"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        resp = await SeRequest.put(headers=headers, payload=payload, url=url)

        return resp
