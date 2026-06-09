from decimal import Decimal

from app.services.fibonacci import fibonacci
from app.services.factorial import factorial
from app.services.loan_repayment import loan_repayment
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Calculation Service"}

@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    try:
        return {"result": fibonacci(n)}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=(str(e))
        )
    
@app.get("/factorial/{n}")
def get_factorial(n: int):
    try:
        return {"result": factorial(n)}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=(str(e))
        )

@app.get("/loan_repayment")
def get_loan(
    principal: Decimal,
    annual_rate: Decimal,
    months: int
):
    try:
        return {
            "monthly_payment": loan_repayment(
                principal,
                annual_rate,
                months
            )
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=(str(e))
        )