from uagents import Model
from pydantic import Field


class UrlShortenRequest(Model):
  url: str = Field(description="The URL to be shortened.")
  alias: str = Field(default=None, description="Optional custom alias for the shortened URL.")
  password: str = Field(default=None, description="Optional password for the shortened URL.")
