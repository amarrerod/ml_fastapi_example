
import uvicorn
from fastapi import FastAPI
from model import IrisModel, IrisSpecies


app = FastAPI()
classifier = IrisModel()


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


@app.post('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    pred, prob = classifier.predict(data['sepal_length'],
                                    data['sepal_width'],
                                    data['petal_length'],
                                    data['petal_width']
                                    )
    return {
        'prediction': pred,
        'probability': prob
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
