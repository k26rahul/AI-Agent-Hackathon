"""
URL Shortener Agent

Shorten URLs with optional alias and password using spoo.me service.

Shorten the following URL using the spoo.me service: https://www.linkedin.com/in/k26rahul/
Set the alias to 'linkedin' and the password to 'Abc@123x'.
"""

from uagents import Agent, Context
from protocols.url_shortener_protocol import url_shortener_protocol
from uagents.setup import fund_agent_if_low

AGENT_NAME = 'url_shortener_agent'
AGENT_PORT = 8001
url_shortener_agent = Agent(name=AGENT_NAME, seed=AGENT_NAME, port=AGENT_PORT,
                            endpoint=[f'http://127.0.0.1:{AGENT_PORT}/submit'])
fund_agent_if_low(url_shortener_agent.wallet.address())
url_shortener_agent.include(url_shortener_protocol, publish_manifest=True)


@url_shortener_agent.on_event("startup")
async def startup(ctx: Context):
  ctx.logger.info(f"🤖 Agent Address: {ctx.address}")

if __name__ == "__main__":
  url_shortener_agent.run()
