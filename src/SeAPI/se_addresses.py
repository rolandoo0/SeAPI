from se_request import SeRequest
import json


class ShipEngineAddresses:
    def __init__(self, ship_engine_api_key) -> None:
        self.api_key = ship_engine_api_key

    async def parse_address(self, address: dict = None):
        """
        Parse an address.
        """
        url = "https://api.shipengine.com/v1/addresses/recognize"

        payload = json.dumps(address)
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        resp = await SeRequest.put(self, headers=headers, payload=payload, url=url)

        return resp

    async def validate_address(self, address: dict = None):
        """
        Validate an address.
        """
        url = "https://api.shipengine.com/v1/addresses/validate"

        payload = json.dumps(address)
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        resp = await SeRequest.put(self, headers=headers, payload=payload, url=url)

        return resp
