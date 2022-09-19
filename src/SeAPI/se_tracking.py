from se_request import SeRequest


class ShipEngineTracking:
    """
    This class will contain all the methods from ShipEngine's Tracking API Module
    """

    def __init__(self, ship_engine_api_key: str = None) -> None:
        self.api_key = ship_engine_api_key

    async def start_tracking_package(
        self, carrier_code: str = None, tracking_number: str = None
    ):
        """
        Function to start tracking a package based on tracking number.

        - carrier_code: str.
        - tracking_number: string of the tracking number of the package.
        """
        url = f"https://api.shipengine.com/v1/tracking/start?carrier_code={carrier_code}&tracking_number={tracking_number}"

        payload = {}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.post(self, headers=headers, payload=payload, url=url)

        return resp

    async def stop_tracking_package(
        self, carrier_code: str = None, tracking_number: str = None
    ):
        """
        Stops tracking a package based on tracking number.

        - carrier_code: str
        - tracking_number: string of the tracking number of the package.
        """
        url = f"https://api.shipengine.com/v1/tracking/stop?carrier_code={carrier_code}&tracking_number={tracking_number}"

        payload = {}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
        }

        resp = await SeRequest.post(self, headers=headers, payload=payload, url=url)

        return resp

    async def get_tracking_info(
        self, carrier_code: str = None, tracking_number: str = None
    ):
        """
        Get tracking information about a package.

        - carrier_code: str
        - tracking_number: string of the tracking number of the package.
        """
        url = f"https://api.shipengine.com/v1/tracking?carrier_code={carrier_code}&tracking_number={tracking_number}"

        payload = {}
        headers = {
            "Host": "api.shipengine.com",
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        resp = await SeRequest.get(self, headers=headers, payload=payload, url=url)

        return resp
