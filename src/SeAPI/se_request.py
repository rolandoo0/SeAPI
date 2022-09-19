import aiohttp


class SeRequest:
    """
    Base request class for ShipEngine.
    """

    def __init__(self) -> None:
        pass

    async def post(
        self,
        headers: dict = None,
        payload: dict = None,
        url: str = None,
    ):
        """
        Aysnc POST Request for ShipEngine.
        """
        session = aiohttp.ClientSession()
        async with session.post(url, headers=headers, data=payload) as response:
            resp = await response.json()

        return resp

    async def get(
        self,
        headers: dict = None,
        payload: dict = None,
        url: str = None,
    ):
        """
        Aysnc GET Request for ShipEngine.
        """
        session = aiohttp.ClientSession()
        async with session.get(url, headers=headers, data=payload) as response:
            resp = await response.json()

        return resp

    async def delete(self, headers: dict = None, payload: dict = None, url: str = None):
        """
        Aysnc DELETE Request for ShipEngine.
        """
        session = aiohttp.ClientSession()
        async with session.delete(url, headers=headers, data=payload) as response:
            resp = await response.json()

        return resp

    async def put(self, headers: dict = None, payload: dict = None, url: str = None):
        """
        Aysnc PUT Request for ShipEngine.
        """
        session = aiohttp.ClientSession()
        async with session.put(url, headers=headers, data=payload) as response:
            resp = await response.json()

        return resp
