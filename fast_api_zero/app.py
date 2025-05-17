from fastapi import FastAPI

app = FastAPI()


# System Under Test - SUT
@app.get('/')
def read_root():
    return {'message': 'Olá, mundo!'}
