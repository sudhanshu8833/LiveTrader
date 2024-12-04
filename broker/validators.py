from pydantic import BaseModel, Field
from typing import Optional, Literal, Dict

class CreateOrderParams(BaseModel):
    symbol: str = Field(..., description="Trading pair symbol, e.g., BTCUSDT")
    side: Literal["BUY", "SELL"] = Field(..., description="Order side")
    type: Literal["MARKET", "LIMIT", "STOP_LOSS", "STOP_LOSS_LIMIT", "TAKE_PROFIT", "TAKE_PROFIT_LIMIT"] = Field(..., description="Order type")
    quantity: Optional[float] = Field(None, description="Quantity to trade")
    price: Optional[float] = Field(None, description="Price for LIMIT orders")
    time_in_force: Optional[Literal["GTC", "IOC", "FOK"]] = Field(None, description="Time in force for LIMIT orders")
    stop_price: Optional[float] = Field(None, description="Stop price for STOP_LOSS/TAKE_PROFIT orders")
    trailing_delta: Optional[int] = Field(None, description="Trailing stop delta")
    client_order_id: Optional[str] = Field(None, description="Custom client order ID")
    broker_specific: Optional[Dict[str, str]] = Field({}, description="Extra parameters specific to a broker")