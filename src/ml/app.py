from aiohttp import web
from aiohttp import ClientSession
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from json import loads
from json import dumps
import pandas as pd

if __name__ == '__main__':
    routes = web.RouteTableDef()
    session = ClientSession()

    @routes.get('/api/v1/forecast')
    async def forecast(request):
        tm_from = int(request.query['from'])
        tm_to = int(request.query['to'])

        query_data = {
            "selector": {
                "$and": [
                    {"time": {
                        "$gt": tm_from
                    }},
                    {"time": {
                        "$lt": tm_to
                    }}
                ]
            }
        }

        headers = {
            'Content-Type': 'application/json'
        }

        async with session.post('http://localhost:5984/forecast/_find', data=dumps(query_data), headers=headers) as res:
            res_data = await res.json()

            return web.json_response(res_data)

    @routes.get('/api/v1/pred')
    async def station(request):
        station_number = int(request.query['number'])

        query_data = {
            "selector": {
                "number": station_number
            }
        }

        headers = {
            'Content-Type': 'application/json'
        }

        async with session.post('http://localhost:5984/station/_find', data=dumps(query_data), headers=headers) as res:
            res_data = await res.text()
            res_data = loads(res_data)
            res_data = pd.DataFrame.from_records(res_data['docs'])
            y_pred = await predict(res_data)

            return web.json_response({"pred": y_pred[0]})

    async def predict(dataset):
        X = dataset.iloc[:, 4:6].values
        Y = dataset.iloc[:, 2].values

        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=1 / 4, random_state=0)

        reg = LinearRegression()
        reg.fit(X_train, Y_train)
        y_pred = reg.predict(X_test)

        return y_pred

    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=9000)
