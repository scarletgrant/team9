from aiohttp import web
from aiohttp import ClientSession
from json import loads

routes = web.RouteTableDef()


@routes.get('/')
async def home(request):
    with open('./static/index.html', encoding='utf8') as f:
        content = f.read()

        return web.Response(content_type='text/html', text=content)


@routes.get('/api/v1/pred')
async def forecastPred(request):
    number = request.query['number']
    city = request.query['city']
    country = request.query['country']

    params = {
        'number': number,
        'city': city,
        'country': country
    }

    async with ClientSession() as session:
        async with session.get('http://localhost:8000/api/v1/pred', params=params) as res:
            res_data = await res.text()
            return web.json_response(loads(res_data))


@routes.get('/api/v1/forecast')
async def forecast(request):
    city = request.query['city']
    country = request.query['country']

    params = {
        'city': city,
        'country': country
    }

    async with ClientSession() as session:
        async with session.get('http://localhost:8000/api/v1/forecast', params=params) as res:
            res_data = await res.text()
            return web.json_response(loads(res_data))


@routes.get('/api/v1/bikes')
async def station(request):
    country = request.query['country']

    params = {
        'country': country
    }

    async with ClientSession() as session:
        async with session.get('http://localhost:8000/api/v1/bikes', params=params) as res:
            res_data = await res.text()
            return web.json_response(loads(res_data))


@routes.get('/api/v1/coordinates')
async def coords(request):
    city = request.query['city']
    country = request.query['country']

    params = {
        'city': city,
        'country': country
    }

    async with ClientSession() as session:
        async with session.get('http://localhost:8000/api/v1/coordinates', params=params) as res:
            res_data = await res.text()

            return web.json_response(loads(res_data))


def env():
    with open('.env') as f:
        env = {}

        for row in f.readlines():
            row = row.split('=')
            key = row[0].strip()
            value = row[1].strip()

            env[key] = value

        return env


app = web.Application()
app.add_routes(routes)
web.run_app(app)
