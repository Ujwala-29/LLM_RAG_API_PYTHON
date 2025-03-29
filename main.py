from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from retriever import retrieve_function
from automation_functions import FUNCTIONS

app = FastAPI()

# Define request body model
class FunctionRequest(BaseModel):
    prompt: str

@app.post("/execute/")
async def execute_function(request: FunctionRequest):
    """Executes a function dynamically based on a natural language prompt."""
    function_name = retrieve_function(request.prompt)

    if function_name is None or function_name not in FUNCTIONS:
        raise HTTPException(status_code=404, detail="No matching function found")

    # Execute the function
    function_output = FUNCTIONS[function_name]()

    # Generate function invocation code
    generated_code = f'{{ "function": "{function_name}", "code": "{function_name}()" }}'

    return {"function": function_name, "code": generated_code, "result": function_output}
