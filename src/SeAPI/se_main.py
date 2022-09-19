from se_addresses import ShipEngineAddresses
from se_webhooks import ShipEngineWebhooks
from se_request import SeRequest
from se_carriers import ShipEngineCarriers
from se_labels import ShipEngineLabels
from se_pickups import ShipEnginePickups
import json


class ShipEngine(
    ShipEngineAddresses,
    ShipEngineWebhooks,
    SeRequest,
    ShipEngineCarriers,
    ShipEngineLabels,
    ShipEnginePickups,
):
    def __init__(self, ship_engine_api_key) -> None:
        self.api_key = ship_engine_api_key
