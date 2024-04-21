from typing import List, Optional
from pydantic import BaseModel, validator

class Block(BaseModel):
  """Defines the schema of a Solana block."""

  # Transaction data
  transactions: List[dict]

  # Blockheader data
  parent_slot: int
  previous_blockhash: str
  timestamp: int
  validator_address: str
  # Additional PoH information (optional)
  poh_information: Optional[dict] = None

  # Transaction metadata (not directly included in block, but relevant)
  @validator('transactions', pre=True)
  def validate_transactions(cls, value):
    """Ensures transactions are a list of dictionaries."""
    if not isinstance(value, list):
      raise ValueError("transactions must be a list")
    for item in value:
      if not isinstance(item, dict):
        raise ValueError("Transactions must be dictionaries")
    return value

class SolanaTransaction(BaseModel):
  """Defines the schema of a Solana transaction within a block."""

  # Placeholder for various transaction fields based on transaction type
  # Specific details can be added as needed (e.g., sender, receiver, amount for transfers)
  # or nested using Pydantic's data models for complex transaction types.
  data: dict

