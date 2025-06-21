# AI Function Planner (Take-home Assignment)

## Objective
Convert natural language queries into structured function calls using an open-source model.

## Project Structure

- `app.py`: Entry point.
- `planner.py`: Executes function call plan.
- `model_inference.py`: Simulated model parser.
- `function_library.py`: Custom function library (~50 functions).

## Example

**Query**:
"Retrieve all invoices for March, summarize them, and email me."

**Output Plan**:
1. `get_invoices("March")`
2. `summarize_invoices(invoices)`
3. `send_email(summary, "user@example.com")`

## Instructions

1. Install Python 3.8+
2. Run with: `python app.py`
3. Modify `simulate_model_response()` to test different flows.
