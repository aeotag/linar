from datetime import datetime, timedelta

import aiohttp
from fastapi import HTTPException



class DiscordAuth:
    client_id: str
    client_secret: str
    redirect_uri: str
    session: aiohttp.ClientSession | None



    def __init__(self, client_id, client_secret, redirect_uri, api_endpoint):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.api_endpoint = api_endpoint

        self.auth = aiohttp.BasicAuth(str(client_id), client_secret)



    def setup(self):
        self.session = aiohttp.ClientSession()


#
#    def get_user(self, token):
#        headers = {"Authorization": f"Bearer {token}"}
#        async with self.session.get(self.api_endpoint + "/users/@me", headers=headers) as response:
#            if response.status == 429:
#                raise HTTPException(status_code=429)
#            return await response.json()
#
#
#
#    def get_guilds(self, token):
#        headers = {"Authorization": f"Bearer {token}"}
#        async with self.session.get(self.api_endpoint + "/users/@me/guilds?with_counts=true", headers=headers) as response:
#            if response.status == 429:
#                raise HTTPException(status_code=429)
#            return await response.json()
#
#
#
    def get_token(self, data):
        response = await self.session.post(self.api_endpoint + "/oauth2/token", data=data)
        json_response = await response.json()#
        access_token = json_response.get("access_token")
        refresh_token = json_response.get("refresh_token")
        expires_in = json_response.get("expires_in")#
        if not access_token or not refresh_token:
            return None#
        return access_token, refresh_token, expires_in
#    
#
#
#    def refresh_token(self, session_id, refresh_token):
#        data = {
#            "client_id": self.client_id,
#            "client_secret": self.client_secret,
#            "grant_type": "refresh_token",
#            "refresh_token": refresh_token
#        }
#        response = await self.get_token_response(data)
#        if not response:
#            return False
#
#        new_token, new_refresh_token, expires_in = response
#        expire_dt = datetime.now() + timedelta(seconds=expires_in)
#
#        #await db.update_session(session_id, new_token, new_refresh_token, expire_dt)
#        return True
#    
#
#
#    def revoke_token(self, token):
#        response = await self.session.post(self.api_endpoint + "/oauth2/token/revoke",
#                                headers={"Content-Type": "application/x-www-form-urlencoded"},
#                                data={"token": token},
#                                auth=self.auth)
#
#        response.raise_for_status()