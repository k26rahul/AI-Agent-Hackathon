from uagents import Model
from pydantic import Field
from enum import Enum


class ConditionEnum(str, Enum):
  NEW = "new"
  LIKE_NEW = "like new"
  USED_GOOD = "used - good"
  USED_FAIR = "used - fair"


class QuickTradeChoiceMessage(Model):
  action: str = Field(description="The choice of action, either 'buy' or 'sell'.")
  response: str = Field(
      description="The final response. Do not ask for this value from the user but use a subtask agent to fulfill it.")


class QuickTradeBuyMessage(Model):
  product_name: str = Field(description="The name of the product to buy. For example, 'laptop', 'smartphone', etc.")
  quantity: int = Field(description="The quantity of the product to buy. For example, 1, 2, 5, etc.")
  price_range: str = Field(description="The acceptable price range for the product. For example, '$500-$1000'.")
  delivery_timeframe: str = Field(
      description="The preferred delivery timeframe. For example, 'within 5 days', 'next week', etc.")
  payment_method: str = Field(description="The preferred payment method. For example, 'credit card', 'PayPal', etc.")


class QuickTradeSellMessage(Model):
  product_name: str = Field(description="The name of the product to sell. For example, 'laptop', 'smartphone', etc.")
  quantity: int = Field(description="The quantity of the product to sell. For example, 1, 2, 5, etc.")
  price: float = Field(description="The selling price of the product. For example, 500.0, 750.0, etc.")
  condition: ConditionEnum = Field(
      description="The condition of the product. Possible values are 'new', 'like new', 'used - good', 'used - fair'.")
  shipping_options: str = Field(
      description="The available shipping options. For example, 'standard', 'express', 'pickup', etc.")
