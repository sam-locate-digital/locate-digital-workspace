"""One-off OAuth flow to get a refresh token for GA4 + Google Ads.

Usage: python get_refresh_token.py <path-to-client-env>

Opens a browser, you sign in with the test user's Google account, grant
permissions, and the refresh token is printed at the end.
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/adwords",
]

if len(sys.argv) < 2:
    print("Usage: python get_refresh_token.py <path-to-client-env>")
    sys.exit(1)

env_path = Path(sys.argv[1])
load_dotenv(env_path)

client_id = os.getenv("GOOGLE_ADS_CLIENT_ID")
client_secret = os.getenv("GOOGLE_ADS_CLIENT_SECRET")

if not client_id or not client_secret:
    print("ERROR: GOOGLE_ADS_CLIENT_ID or GOOGLE_ADS_CLIENT_SECRET missing in .env")
    sys.exit(1)

client_config = {
    "installed": {
        "client_id": client_id,
        "client_secret": client_secret,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost"],
    }
}

flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
credentials = flow.run_local_server(
    port=0,
    prompt="consent",
    access_type="offline",
    authorization_prompt_message="\nA browser window will open. Sign in with the test user account, then grant permissions.\n",
    success_message="Done. You can close this browser tab.",
    open_browser=True,
)

print("\n" + "=" * 60)
print("REFRESH TOKEN (paste this into .env as GOOGLE_ADS_REFRESH_TOKEN):")
print("=" * 60)
print(credentials.refresh_token)
print("=" * 60)
print("\nAlso paste the same value into GA4_REFRESH_TOKEN if you want")
print("to keep it explicit, or reuse GOOGLE_ADS_REFRESH_TOKEN for both.")
