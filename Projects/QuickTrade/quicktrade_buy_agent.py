"""
Buy Agent

This agent handles buy requests and responds accordingly.

Prompt the user for buy details.
"""

from uagents import Agent, Context
from protocols.buy_protocol import buy_protocol
from uagents.setup import fund_agent_if_low

AGENT_NAME = 'buy_agent'
AGENT_PORT = 8003
buy_agent = Agent(name=AGENT_NAME, seed=AGENT_NAME, port=AGENT_PORT,
                  endpoint=[f'http://127.0.0.1:{AGENT_PORT}/submit'])
fund_agent_if_low(buy_agent.wallet.address())
buy_agent.include(buy_protocol, publish_manifest=True)


@buy_agent.on_event("startup")
async def startup(ctx: Context):
  ctx.logger.info(f"🤖 Agent Address: {ctx.address}")


if __name__ == "__main__":
  buy_agent.run()
