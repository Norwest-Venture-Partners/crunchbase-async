import aiohttp
import json


class CrunchbaseAsync(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_version = 'v4'
        self.base_url = 'https://api.crunchbase.com/api/{}/'.format(self.api_version)

    def build_params(self, kwargs):
        kwargs['user_key'] = self.api_key
        return kwargs

    async def api_get(self, endpoint, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url + endpoint, params=self.build_params(kwargs)) as response:
                return await response.json()

    async def get_organization(self, org_identifier, **kwargs):
        return await self.api_get(
            'entities/organizations/' + org_identifier,
            **kwargs
        )
