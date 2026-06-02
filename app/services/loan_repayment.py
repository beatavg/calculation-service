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

from decimal import Decimal

if __name__ == "__main__": # Do not run when executed by test
    while True:
        principal_input = input("Loan amount (or q to quit): ")

        if principal_input.lower() == "q":
            break

        annual_rate_input = input("Annual interest rate (%): ")
        months_input = input("Months: ")

        try:
            principal = Decimal(principal_input)
            annual_rate = Decimal(annual_rate_input)
            months = int(months_input)

            payment = loan_repayment(
                principal,
                annual_rate,
                months
            )

            print(f"Monthly repayment: {payment}")

        except ValueError as e:
            print(e)