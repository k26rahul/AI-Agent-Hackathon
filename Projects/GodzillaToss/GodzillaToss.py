# Here we demonstrate how we can create a magical Godzilla-themed coin toss agent that is compatible with DeltaV.
# After running this agent, it can be registered to DeltaV on Agentverse's Services tab. For registration, you will have to use the agent's address.

from uagents import Agent, Context, Model, Protocol
from pydantic import Field
from ai_engine import UAgentResponse, UAgentResponseType
import random

AGENT_NAME = 'godzilla_coin_toss_agent'
AGENT_PORT = 8001
AGENT_SEED = ''
AGENT_ENDPOINT = [f'http://localhost:{AGENT_PORT}/submit']
AGENT_MAILBOX_KEY = ""

agent = Agent(name=AGENT_NAME, seed=AGENT_SEED,
              port=AGENT_PORT, endpoint=AGENT_ENDPOINT,
              #  mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai"
              )


class GodzillaToss(Model):
  choice: str = Field(description="Your magical choice. Must be 'heads' or 'tails'.")


godzilla_toss_protocol = Protocol("GodzillaToss")


@godzilla_toss_protocol.on_message(model=GodzillaToss, replies={UAgentResponse})
async def magical_toss(ctx: Context, sender: str, msg: GodzillaToss):
  # Generate a random number to simulate a magical coin toss
  random_number = random.randint(0, 1)
  coin_tossed = "heads" if random_number == 0 else "tails"

  # Determine if the sender's magical choice matches the coin toss result
  if coin_tossed == msg.choice:
    message = "Your magical vibes prevailed! You won!"
  else:
    message = "The mighty Godzilla roars! You lost!"

  # Send the result back to the sender
  await ctx.send(
      sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
  )

# Include the protocol in the agent and publish the manifest
agent.include(godzilla_toss_protocol, publish_manifest=True)


@agent.on_event("startup")
async def startup(ctx: Context):
  ctx.logger.info(f"🤖 Agent Address: {ctx.address}")

# Run the agent if this script is executed as the main module
if __name__ == "__main__":
  agent.run()
