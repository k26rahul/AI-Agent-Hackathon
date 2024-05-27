from uagents import Context, Protocol
from ai_engine import UAgentResponse, UAgentResponseType
from .models import UrlShortenRequest
import requests

url_shortener_protocol = Protocol("UrlShortener")


@url_shortener_protocol.on_message(model=UrlShortenRequest, replies={UAgentResponse})
async def shorten_url(ctx: Context, sender: str, msg: UrlShortenRequest):
  ctx.logger.info(f"📩 Incoming request from {sender}:")
  ctx.logger.info(f"👉 Data: URL={msg.url}, Alias={msg.alias}, Password={msg.password}")

  url = "https://spoo.me"
  payload = {
      "url": msg.url,
      "alias": msg.alias if msg.alias else "",
      "password": msg.password if msg.password else ""
  }
  headers = {
      "Accept": "application/json"
  }
  response = requests.post(url, data=payload, headers=headers)

  if response.status_code == 200:
    data = response.json()
    message = f"🎉 Shortened URL generated: {data['short_url']}"
  else:
    message = f"❌ Request failed with status code {response.status_code}. {response.text}"

  message = message.strip()
  ctx.logger.info(f"👉 Message: {message}")
  await ctx.send(
      sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
  )
