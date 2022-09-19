from datetime import datetime
from decouple import config
import json
import aiohttp
from se_request import SeRequest


class ShipEngineLabels:
    """
    Class for ShipEngine API labels module.
    """

    def __init__(self, ship_engine_api_key: str = None) -> None:
        self.api_key = ship_engine_api_key

    async def create_return_label(
        self,
        ship_to: dict = None,
        ship_from: dict = None,
        packages: list = None,
    ):

        dictionary = {
            "charge_event": "carrier_default",
            "is_return_label": True,
            "shipment": {
                "service_code": "ups_ground",
                "ship_to": ship_to,
                "ship_from": ship_from,
                "insurance_provider": "carrier",
                "packages": packages,
            },
        }

        payload = json.dumps(dictionary)
        url = "https://api.shipengine.com/v1/labels"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.post(headers=headers, payload=payload, url=url)

        return resp

    async def get_label_information(self, label_id: str = None):
        """
        Get label information.
        """
        payload = {}
        url = f"https://api.shipengine.com/v1/labels/{label_id}"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.get(headers=headers, payload=payload, url=url)

        return resp

    async def void_label(self, label_id: str = None):
        """
        Void label.
        """
        payload = {}
        url = f"https://api.shipengine.com/v1/labels/{label_id}/void"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.put(headers=headers, payload=payload, url=url)

        return resp

    async def get_label_tracking_information(self, label_id: str = None):
        """
        Get label information.
        """
        payload = {}
        url = f"https://api.shipengine.com/v1/labels/{label_id}/track"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.get(headers=headers, payload=payload, url=url)

        return resp

    async def list_labels(self):
        """
        List labels.
        """
        payload = {}
        url = f"https://api.shipengine.com/v1/labels"
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.get(headers=headers, payload=payload, url=url)

        return resp
