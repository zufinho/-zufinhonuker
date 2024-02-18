import requests
import sys

if len(sys.argv) != 4:
    print("Usage: <guild_id> <bot_token> <role_id>")
    sys.exit(1)

guild_id, bot_token, role_id = sys.argv[1], sys.argv[2], sys.argv[3]

api_url = f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}"
headers = {
    "Authorization": f"Bot {bot_token}",
}

response = requests.delete(api_url, headers=headers)

print(response.status_code)
