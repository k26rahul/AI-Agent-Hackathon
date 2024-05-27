from uagents import Context, Protocol
from .models import QuickTradeBuyMessage
from ai_engine import UAgentResponse, UAgentResponseType

buy_protocol = Protocol("QuickTradeBuy")


@buy_protocol.on_message(model=QuickTradeBuyMessage, replies={UAgentResponse})
async def handle_buy(ctx: Context, sender: str, msg: QuickTradeBuyMessage):
  ctx.logger.info(f"📩 Incoming buy request from {sender}:")
  ctx.logger.info(f"👉 Product Name: {msg.product_name}")
  ctx.logger.info(f"👉 Quantity: {msg.quantity}")
  ctx.logger.info(f"👉 Price Range: {msg.price_range}")
  ctx.logger.info(f"👉 Delivery Timeframe: {msg.delivery_timeframe}")
  ctx.logger.info(f"👉 Payment Method: {msg.payment_method}")

  # Directly send a confirmation response back
  message = f"Received buy request for {msg.quantity} x {msg.product_name}."
  ctx.logger.info(f"👉 Message: {message}")
  await ctx.send(
      sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
  )
