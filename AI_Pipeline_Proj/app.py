# app.py

from planner import execute_plan

if __name__ == "__main__":
    query = "Retrieve all invoices for March, summarize, and email me."
    output = execute_plan(query)
    print("Execution Output:")
    for key, value in output.items():
        print(f"{key} => {value}")
