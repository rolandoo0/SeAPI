from decouple import config
from se_request import SeRequest
import json
import aiohttp


class ShipEngineCarrier:
    """
    This class will contain all the methods from ShipEngine's Carriers API Module
    """

    def __init__(self, api_key: str = None) -> None:
        """
        Initialize the class with your ShipEngine API Key
        """
        self.api_key = api_key

    async def list_carriers(self):
        """
        Method to list all available carriers.
        """
        url = "https://api.shipengine.com/v1/carriers"

        payload = {}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.post(headers=headers, payload=payload, url=url)

        return resp

    async def list_carrier_attributes(self, carrier_id: str = None):
        """
        Method to list all available carrier information.
        """
        url = f"https://api.shipengine.com/v1/carriers/{carrier_id}"

        payload = {}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.post(headers=headers, payload=payload, url=url)

        return resp

    async def add_funds_to_carrier(
        self, carrier_id: str = None, currency: str = "usd", amount: float = 0.0
    ):
        """
        Method to add funds to a carrier.
        """
        url = f"https://api.shipengine.com/v1/carriers/{carrier_id}/add_funds"

        payload = {"currency": currency, "amount": amount}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.put(headers=headers, payload=payload, url=url)

        return resp
