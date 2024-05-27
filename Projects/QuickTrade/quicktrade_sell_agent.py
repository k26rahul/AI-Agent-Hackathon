"""
Sell Agent

This agent handles sell requests and responds accordingly.

Prompt the user for sell details.
"""

from uagents import Agent, Context
from protocols.sell_protocol import sell_protocol
from uagents.setup import fund_agent_if_low

AGENT_NAME = 'sell_agent'
AGENT_PORT = 8004
sell_agent = Agent(name=AGENT_NAME, seed=AGENT_NAME, port=AGENT_PORT,
                   endpoint=[f'http://127.0.0.1:{AGENT_PORT}/submit'])
fund_agent_if_low(sell_agent.wallet.address())
sell_agent.include(sell_protocol, publish_manifest=True)


@sell_agent.on_event("startup")
async def startup(ctx: Context):
  ctx.logger.info(f"🤖 Agent Address: {ctx.address}")


if __name__ == "__main__":
  sell_agent.run()
