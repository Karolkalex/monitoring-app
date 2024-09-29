import asyncio
from bleak import BleakClient

SENSOR_ADDRESS = "DEVICE_BLUETOOTH_ADDRESS"  # Replace with the actual sensor's Bluetooth address
HEART_RATE_UUID = "HEART_RATE_UUID"          # Replace with your sensor's heart rate characteristic UUID

class Sensor:
    def __init__(self, address):
        self.address = address
        self.client = None

    async def connect(self):
        self.client = BleakClient(self.address)
        await self.client.connect()

    async def get_heart_rate(self):
        heart_rate = await self.client.read_gatt_char(HEART_RATE_UUID)
        return int.from_bytes(heart_rate, byteorder='little')

    async def disconnect(self):
        await self.client.disconnect()

# Example usage (run this part in your main event loop)
# sensor = Sensor(SENSOR_ADDRESS)
# await sensor.connect()
# heart_rate = await sensor.get_heart_rate()
# await sensor.disconnect()