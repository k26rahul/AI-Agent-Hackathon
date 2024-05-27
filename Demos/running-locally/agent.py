from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Protocol, Model
import random
from pydantic import Field
from ai_engine import UAgentResponse, UAgentResponseType
import sys

dungeons = Agent(
    name="dungeonsanddragonsdiceroll",
    port=6145,
    seed="RANDOM STRINGS ok127",
    endpoint=["http://2409:4089:a18e:18e8:b00c:2aea:50e8:b7ad:6145/submit"],
)

fund_agent_if_low(dungeons.wallet.address())


@dungeons.on_event("startup")
async def hi(ctx: Context):
  ctx.logger.info(dungeons.address)


class Request(Model):
  dice_sides: int = Field(description="How many sides of magic 101 does your dice need?")


dice_roll_protocol = Protocol("DungeonsAndDragonsDiceRoll_ok101")


@dice_roll_protocol.on_message(model=Request, replies={UAgentResponse})
async def roll_dice(ctx: Context, sender: str, msg: Request):
  result = str(random.randint(1, msg.dice_sides))
  message = f"Dice roll result: {result}"
  await ctx.send(
      sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
  )


dungeons.include(dice_roll_protocol, publish_manifest=True)

dungeons.run()
