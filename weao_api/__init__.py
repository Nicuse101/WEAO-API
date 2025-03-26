import urllib.parse
import urllib.request
import json
from types import SimpleNamespace
from enum import Enum

class Platform(Enum):
    """A required field for the 'fetch_roblox_version' function."""
    WINDOWS = 1
    MAC = 2
    ANDROID = 3
    FUTURE_WINDOWS = 4
    FUTURE_MAC = 5

class Version:
    def __init__(self, value: str, date=None):
        self.value = value
        self.date = date

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, str):  
            return self.value == other
        if isinstance(other, Version):
            return self.value == other.value
        return False  

    def __repr__(self):
        return f"Version(value='{self.value}', date='{self.date}')"

class WEAO:
    __base_url = "https://weao.xyz/api"
    __headers = {"User-Agent": "WEAO-3PService", "Content-Type": "application/json"}

    @staticmethod
    def __send_request(endpoint):
        """Sends a request and returns the full response including status, headers, and body."""
        route = WEAO.__base_url + str(endpoint)
        req = urllib.request.Request(route, headers=WEAO.__headers)
        with urllib.request.urlopen(req) as response:
            return response.read()
        
    @staticmethod
    def __dataset(data):
        return json.loads(data.decode('utf-8'), object_hook=lambda d: SimpleNamespace(**d))

    @staticmethod
    def fetch_roblox_version(platform: Platform):
        """Fetches the current/future Roblox version"""
        if not isinstance(platform, Platform):
            raise ValueError("Parameter 'platform' must be an instance of Platform Enum")
        
        platform_map = {
            Platform.WINDOWS: "current",
            Platform.MAC: "current",
            Platform.ANDROID: "android",
            Platform.FUTURE_WINDOWS: "future",
            Platform.FUTURE_MAC: "future"
        }

        endpoint = f"/versions/{platform_map[platform]}"
        dataset = WEAO.__dataset(WEAO.__send_request(endpoint))

        version_keys = {
            Platform.WINDOWS: ("Windows", "WindowsDate"),
            Platform.MAC: ("Mac", "MacDate"),
            Platform.ANDROID: ("Android", "AndroidDate"),
            Platform.FUTURE_WINDOWS: ("Windows", "WindowsDate"),
            Platform.FUTURE_MAC: ("Mac", "MacDate")
        }

        version_key, date_key = version_keys[platform]

        version = getattr(dataset, version_key, "Unknown Version")
        date = getattr(dataset, date_key, "Unknown Date")

        return Version(version, date)
    
    @staticmethod
    def fetch_exploit_status(exploit: str = None):
        """Fetches the exploit's status if defined else all exploits status."""
        if exploit is not None and not isinstance(exploit, str):
            raise ValueError("Parameter 'exploit' must be a str")
        
        endpoint = f"/status/exploits/{urllib.parse.quote(exploit)}" if exploit else "/status/exploits"

        return WEAO.__dataset(WEAO.__send_request(endpoint))
