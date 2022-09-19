from datetime import datetime
from se_request import SeRequest


class ShipEnginePickups:
    """
    ShipEngine API Pickups Module
    """

    def __init__(self, ship_engine_api) -> None:
        self.api_key = ship_engine_api

    async def list_scheduled_pickups(self):
        """
        Method to list all scheduled pickups.
        """
        url = "https://api.shipengine.com/v1/pickups"

        payload = {}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.get(self, headers=headers, payload=payload, url=url)

        return resp

    async def create_pickup(
        self,
        label_ids: list = None,
        contact_name: str = None,
        contact_email: str = None,
        contact_phone: str = None,
        pickup_window_start: str = datetime.today().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        pickup_window_end: str = datetime.today().strftime("%Y-%m-%dT%16:%M:%S.000Z"),
    ):
        """
        Method to create a pickup.
        """
        url = "https://api.shipengine.com/v1/pickups"

        payload = {
            "label_ids": label_ids,
            "contact_details": {
                "name": contact_name,
                "email": contact_email,
                "phone": contact_phone,
            },
            "pickup_notes": "string",
            "pickup_window": {
                "start_at": pickup_window_start,
                "end_at": pickup_window_end,
            },
        }
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.post(self, headers=headers, payload=payload, url=url)

        return resp

    async def get_pickup_info(self, pickup_id: str = None):
        """
        Method to get info about a pickup.
        """
        url = f"https://api.shipengine.com/v1/pickups/{pickup_id}"

        payload = {}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.get(self, headers=headers, payload=payload, url=url)

        return resp

    async def delete_pickup(self, pickup_id: str = None):
        """
        Method to delete a pickup.
        """
        url = f"https://api.shipengine.com/v1/pickups/{pickup_id}"

        payload = {}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.delete(self, headers=headers, payload=payload, url=url)

        return resp
