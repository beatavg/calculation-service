from decimal import Decimal

def loan_repayment(
        principal: Decimal,
        annual_rate: Decimal,
        months: int
) -> Decimal:
    if principal <= 0:
        raise ValueError("Principal must be positive")

    if annual_rate < 0:
        raise ValueError("Interest rate must be positive")

    if months <= 0:
        raise ValueError("Months must be positive")
    
    if annual_rate == 0: # If interest rate is 0, just return the principal repayment per month
        return principal / months
    
    monthly_rate = annual_rate / Decimal("100") / Decimal("12") # Conversion annual to monthly rate
    
    factor = (Decimal("1") + monthly_rate) ** months # First part of formula

    monthly_payment = principal * monthly_rate * factor / (factor - Decimal("1")) # Formula

    return monthly_payment.quantize(Decimal("0.01"))
