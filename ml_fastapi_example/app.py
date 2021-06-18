
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    '''
        Index page of the application.
        Returns a Hello World message
    '''
    return {'message', 'Hello, world!'}


@app.get('/{name}')
def get_name(name: str):
    '''
        This is the get_name endpoint
        where a greeting message is returned
    '''
    return {'message': f'Hello, {name}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
