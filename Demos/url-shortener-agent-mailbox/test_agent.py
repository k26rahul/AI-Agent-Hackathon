from uagents import Agent, Context
from ai_engine import UAgentResponse
from protocols.models import UrlShortenRequest
from uagents.setup import fund_agent_if_low


AGENT_NAME = 'test_agent'
AGENT_PORT = 8002
test_agent = Agent(name=AGENT_NAME, seed=AGENT_NAME, port=AGENT_PORT,
                   endpoint=[f'http://127.0.0.1:{AGENT_PORT}/submit'])
fund_agent_if_low(test_agent.wallet.address())

request_data = UrlShortenRequest(
    url="https://www.linkedin.com/in/k26rahul/",
    # alias="linkedin",
    # password="Abc@123x"
)
URL_SHORTENER_AGENT_ADDRESS = 'agent1qt466elnw8pu2f4k2gfuc2j9gk5zzspp0pg67u0wz5r2h8j8r40n7nn5d4g'


@test_agent.on_event("startup")
async def startup(ctx: Context):
  ctx.logger.info(f"🤖 Agent Address: {ctx.address}")
  await ctx.send(URL_SHORTENER_AGENT_ADDRESS, request_data)


@test_agent.on_message(model=UAgentResponse, replies=set())
async def receive_shortening_reply(ctx: Context, sender: str, msg: UAgentResponse):
  ctx.logger.info(f"📩 Received response from {sender}:")
  ctx.logger.info(f"👉 Message: {msg.message}")

if __name__ == "__main__":
  test_agent.run()
