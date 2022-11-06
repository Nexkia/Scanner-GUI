import time
import adafruit_ble
from adafruit_ble.advertising.standard import Advertisement


def scanning() -> tuple:
    ble = adafruit_ble.BLERadio()  # pylint: disable=no-member
    timeout_scan = time.time() + 25
    results = set()
    while time.time() < timeout_scan:
        for adv in ble.start_scan(Advertisement, timeout=10):
            if not adv.address.string:
                continue
            if not adv.complete_name:
                continue
            results.add(f"name={adv.complete_name} mac={adv.address.string}")
        ble.stop_scan()
    return tuple(ble_device for ble_device in results)