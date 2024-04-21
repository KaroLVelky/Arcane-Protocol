from typing import List
from pydantic import BaseModel, Field, validator

class Block(BaseModel):
    """Defines the schema of a block on the Arcane Chain."""

    # Transaction data
    transactions: List[dict]

    # Blockheader data
    parent_slot: int
    previous_blockhash: str
    timestamp: int
    validator_address: str
    poh_information: List[dict]

    # Transaction metadata (not directly included in block, but relevant)
    @Field.validator('transactions', pre=True)
    def validate_transactions(cls, value):
        """Ensures transactions are a list of dictionaries."""
        if not isinstance(value, list):
            raise ValueError("transactions must be a list")
        for item in value:
            if not isinstance(item, dict):
                raise ValueError("Transactions must be dictionaries")
        return value
class Transaction(BaseModel):
    """ Defines the schema of a transaction on the Arcane Chain."""
    # Transaction data
    sender: str
    recipient: str
    amount: int
    signature: str
    timestamp: int
    memo: str = ""

    # Transaction metadata
    @Field.validator('sender')
    def validate_sender(cls, value):
        """Ensures the sender is a valid address."""
        if not isinstance(value, str) or len(value) != 64:
            raise ValueError("Sender must be a 64-character hex string")
        return value

    @Field.validator('recipient')
    def validate_recipient(cls, value):
        """Ensures the recipient is a valid address."""
        if not isinstance(value, str) or len(value) != 64:
            raise ValueError("Recipient must be a 64-character hex string")
        return value

    @Field.validator('amount')
    def validate_amount(cls, value):
        """Ensures the amount is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Amount must be a positive integer")
        return value

    @Field.validator('signature')
    def validate_signature(cls, value):
        """Ensures the signature is a valid signature."""
        if not isinstance(value, str) or len(value) != 128:
            raise ValueError("Signature must be a 128-character hex string")
        return value

    @Field.validator('timestamp')
    def validate_timestamp(cls, value):
        """Ensures the timestamp is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Timestamp must be a positive integer")
        return value

    @Field.validator('memo')
    @validator('memo')
    def validate_memo(cls, value):
        """Ensures the memo is a string."""
        if not isinstance(value, str):
            raise ValueError("Memo must be a string")
        return value

