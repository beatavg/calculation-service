from decimal import Decimal

from app.services.fibonacci import fibonacci
from app.services.factorial import factorial
from app.services.loan_repayment import loan_repayment
from fastapi import FastAPI, HTTPException

# python -m uvicorn main:app --reload
# python3 -m pytest

# http://127.0.0.1:8000/docs
app = FastAPI()

# http://127.0.0.1:8000/
@app.get("/")
def root():
    return {"message": "Calculation Service"}

# http://127.0.0.1:8000/fibonacci/10
@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    try:
        return {"result": fibonacci(n)}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=(str(e))
        )
    

# http://127.0.0.1:8000/factorial/5
@app.get("/factorial/{n}")
def get_factorial(n: int):
    try:
        return {"result": factorial(n)}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=(str(e))
        )

# http://127.0.0.1:8000/loan_repayment?principal=12000&annual_rate=0&months=12
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