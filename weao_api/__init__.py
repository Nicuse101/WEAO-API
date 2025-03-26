import urllib.parse
import urllib.request
import json

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
    def __json(data):
        return json.loads(data.decode('utf-8'))

    @staticmethod
    def fetch_roblox_version(*, future=False, android=False):
        """Fetches the current/future Roblox version"""
        return WEAO.__json( WEAO.__send_request("/versions/{}".format("android" if android else "future" if future else "current")) )
    
    @staticmethod
    def fetch_exploit_status(exploit: str = ''):
        """Fetches the exploit's status if defined else all exploits status."""
        if not isinstance(exploit, str):
            raise ValueError("Parameter 'exploit' must be a str")
        
        endpoint = urllib.parse.quote("/status/exploits/{}".format(exploit))

        return WEAO.__json( WEAO.__send_request(endpoint) )
