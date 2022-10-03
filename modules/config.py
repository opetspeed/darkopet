import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "14962361"))
API_HASH = getenv("API_HASH", "2ef6a48ef5a9f2149cf2124bd3c86728")
BOT_USERNAME = getenv("BOT_USERNAME", "saytapibot")
BOT_TOKEN = getenv("BOT_TOKEN", "5447592829:AAG0WIbhBAwLaMVCrCZVmfq1JYLsODgOEK4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQAoctknGFNlEjts3IIhckFpXm0bz7ctBJfc2JT1K3ORSI4uE5jp8WoXYUEsZJ5xFzZAj7Mq5Y7Sfa_Z8OwUCp4VCPvOWdmNEJImmjqFNfrj2BiG4kzBj8wSkvFVCGO7hVZMhke9E7UnZKdowbjj75G1cBJDrxYHq6N8RZobcjtAFmqTHCjPkduTjSkvyZBr7l23S60hvT8gL906GilhSUizEu0nDjTFN0tbnrCPT4cZ7PNMPBgst7kH50h7an9cB0P4TEb1ZfJjEEb4C8ayoR9R7i1NQvrKBPUCGEMPowIhKbw1cnO2DWsiYvYIviZoAViLfe3gSH2RKLlDTJJgHwVdAAAAAU3NrZcA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5626738417").split()))
aiohttpsession = aiohttp.ClientSession()
