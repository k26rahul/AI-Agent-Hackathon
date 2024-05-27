"""
Choice Agent

This agent handles user choices and responds accordingly.

Prompt the user to choose between 'buy' or 'sell'.
"""

from uagents import Agent, Context
from protocols.choice_protocol import choice_protocol
from uagents.setup import fund_agent_if_low

AGENT_NAME = 'choice_agent'
AGENT_PORT = 8002
AGENT_MAILBOX_KEY = "9e2d8862-0407-4e08-903a-eb1fb6df6246"
choice_agent = Agent(name=AGENT_NAME, seed='FA8PPFK4TCSNXJ9W', port=AGENT_PORT,
                     endpoint=[f'localhost:{AGENT_PORT}/submit'],
                     mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai")
fund_agent_if_low(choice_agent.wallet.address())
choice_agent.include(choice_protocol, publish_manifest=True)


@choice_agent.on_event("startup")
async def startup(ctx: Context):
  ctx.logger.info(f"🤖 Agent Address: {ctx.address}")


if __name__ == "__main__":
  choice_agent.run()
