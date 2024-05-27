from uagents import Context, Protocol
from .models import QuickTradeSellMessage
from ai_engine import UAgentResponse, UAgentResponseType

sell_protocol = Protocol("QuickTradeSell")


@sell_protocol.on_message(model=QuickTradeSellMessage, replies={UAgentResponse})
async def handle_sell(ctx: Context, sender: str, msg: QuickTradeSellMessage):
  ctx.logger.info(f"📩 Incoming sell request from {sender}:")
  ctx.logger.info(f"👉 Product Name: {msg.product_name}")
  ctx.logger.info(f"👉 Quantity: {msg.quantity}")
  ctx.logger.info(f"👉 Price: {msg.price}")
  ctx.logger.info(f"👉 Condition: {msg.condition}")
  ctx.logger.info(f"👉 Shipping Options: {msg.shipping_options}")

  # Directly send a confirmation response back
  message = f"Received sell request for {msg.quantity} x {msg.product_name} at ${msg.price}."
  ctx.logger.info(f"👉 Message: {message}")
  await ctx.send(
      sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
  )
