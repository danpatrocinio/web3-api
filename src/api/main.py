from fastapi import FastAPI, HTTPException
from scripts import conn_testing, hardhat_hello_operations
from models import body_authenticator

app = FastAPI()

@app.get("/")
def healthCHeck():
    return { "Connection with local ethereum netowrk is": conn_testing.check_connection() }

@app.get("/message")
def getMessageFromContract():
    response = hardhat_hello_operations.getMessage()
    if response:
        return response
    else:
        raise HTTPException(500, "Internal server error")
    
@app.post("/message")
def setMessageToContract(auth: body_authenticator.Authentication, message: str):
    response = hardhat_hello_operations.setMessage(message, auth.account_caller, auth.private_key)
    if response:
        return response
    else:
        raise HTTPException(500, "Internal server error")

@app.delete("/message")
def clearMessageFromContract(auth: body_authenticator.Authentication):
    response = hardhat_hello_operations.clearMessage(auth.account_caller, auth.private_key)
    if response:
        return response
    else:
        raise HTTPException(500, "Internal server error")