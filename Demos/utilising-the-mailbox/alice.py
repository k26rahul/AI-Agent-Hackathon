from uagents import Agent, Context, Model, Protocol
from uagents.setup import fund_agent_if_low


class Message(Model):
  message: str


# First generate a secure seed phrase (e.g. https://pypi.org/project/mnemonic/)
SEED_PHRASE = "YXZQPQZAGGP1JBW9"

# Copy the address shown below
print(f"Your agent's address is: {Agent(seed=SEED_PHRASE).address}")

# Then go to https://agentverse.ai, register your agent in the Mailroom
# and copy the agent's mailbox key
AGENT_MAILBOX_KEY = "58cbedb9-8ed9-460c-b4c0-7d05ad2bc1a8"

# Now your agent is ready to join the agentverse!
PORT = 8001
IP = 'localhost'
agent = Agent(
    name="alice",
    seed=SEED_PHRASE,
    port=PORT,
    endpoint=[f'http://{IP}:{PORT}/submit'],
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)
fund_agent_if_low(agent.wallet.address())


@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
  ctx.logger.info(f"Received message from {sender}: {msg.message}")

  # send the response
  ctx.logger.info("Sending message to bob")
  await ctx.send(sender, Message(message="hello there bob"))

protocol = Protocol()
agent.include(protocol, publish_manifest=True)

if __name__ == "__main__":
  agent.run()
