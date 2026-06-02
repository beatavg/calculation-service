from app.services.loan_repayment import loan_repayment
import pytest
from decimal import Decimal

# Valid input
def test_zero_interest():
    assert loan_repayment(
        Decimal("12000"),
        Decimal("0"),
        12
    ) == Decimal("1000.00")

def test_standard_loan():
    assert loan_repayment(
        Decimal("100000"),
        Decimal("5"),
        360
    ) == Decimal("536.82")

# Invalid input
def test_negative_principal():
    with pytest.raises(ValueError):
        loan_repayment(
            Decimal("-1000"),
            Decimal("5"),
            12
        )

def test_negative_interest():
    with pytest.raises(ValueError):
        loan_repayment(
            Decimal("1000"),
            Decimal("-5"),
            12
        )

def test_zero_months():
    with pytest.raises(ValueError):
        loan_repayment(
            Decimal("1000"),
            Decimal("5"),
            0
        )

def test_negative_months():
    with pytest.raises(ValueError):
        loan_repayment(
            Decimal("1000"),   
            Decimal("5"),
            -12
        )  