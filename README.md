# Calculation Service

A calculation service built with Python and FastAPI.

## Features

* Fibonacci calculation
* Factorial calculation
* Loan repayment calculation
* Input validation
* Automated tests with pytest
* REST API using FastAPI

## Requirements

* Python 3.9+
* pip

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd calculation-service
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

### Fibonacci

```http
GET /fibonacci/{n}
```

Example:

```http
GET /fibonacci/10
```

Response:

```json
{
  "result": 55
}
```

### Factorial

```http
GET /factorial/{n}
```

Example:

```http
GET /factorial/5
```

Response:

```json
{
  "result": 120
}
```

### Loan Repayment

```http
GET /loan?principal=100000&annual_rate=5&months=360
```

Response:

```json
{
  "monthly_payment": 536.82
}
```

## Running Tests

Run all tests:

```bash
pytest
```

## Validation

The service validates inputs and returns errors for invalid values.

Examples:

* Fibonacci input must be a non-negative integer
* Factorial input must be a non-negative integer
* Principal must be positive
* Interest rate cannot be negative
* Loan duration must be positive

## Assumptions

* Interest is compounded monthly.
* Loan repayments are rounded to two decimal places.
* The loan repayment formula provided in the assignment is used.

## Limitations

* No authentication.
* No database or persistence layer.
* Intended as a demonstration service rather than a production banking system.

```
```
