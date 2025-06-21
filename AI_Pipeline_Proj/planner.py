# planner.py

from function_library import *
from model_inference import simulate_model_response

def execute_plan(query: str):
    plan = simulate_model_response(query)
    context = {}

    for step in plan:
        func = globals()[step['function']]
        args = {k: context.get(v, v) for k, v in step['args'].items()}
        result = func(**args)
        context[step['assign']] = result

    return context
