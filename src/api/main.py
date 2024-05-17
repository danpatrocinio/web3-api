from fastapi import FastAPI, HTTPException
from scripts import test_conn

app = FastAPI()

@app.get("/")
def healthCHeck():
    return { "Connection with local ethereum netowrk is": test_conn.check_connection() }

