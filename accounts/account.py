from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID, uuid4


@dataclass
class Account:
    id_: UUID
    currency: str
    balance: Decimal

    @classmethod
    def random_kzt(cls) -> "Account":
        return cls(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(0),
        )

    @classmethod
    def random_usd(cls) -> "Account":
        return cls(
            id_=uuid4(),
            currency="USD",
            balance=Decimal(0),
        )

    @classmethod
    def random_eur(cls) -> "Account":
        return cls(
            id_=uuid4(),
            currency="EUR",
            balance=Decimal(0),
        )

