from uagents import Context, Protocol
from .models import QuickTradeChoiceMessage
from ai_engine import UAgentResponse, UAgentResponseType

choice_protocol = Protocol("QuickTradeChoice")


@choice_protocol.on_message(model=QuickTradeChoiceMessage, replies={UAgentResponse})
async def handle_choice(ctx: Context, sender: str, msg: QuickTradeChoiceMessage):
  ctx.logger.info(f"📩 Incoming request from {sender}:")
  ctx.logger.info(f"👉 Action: {msg.action}")
  ctx.logger.info(f"👉 Response: {msg.response}")

  # Directly send the response back
  message = msg.response.strip()
  ctx.logger.info(f"👉 Message: {message}")
  await ctx.send(
      sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
  )
