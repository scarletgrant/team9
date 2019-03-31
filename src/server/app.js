const http = require('http')
const fetch = require('../lib/fetch')
const url = require('url')

const start = port => {
  const server = http.createServer((req, res) => {
    if (req.method == 'GET') {
      get(req, res)
    }
  })

  server.on('error', err => {
    throw new Error(err)
  })

  server.listen(port)

  // Update the bike cache every hour
  // setInterval(() => {
  //   updateBikeCache()
  // }, 3600000)
}

/**
 * Handle the HTTP GET request
 * @param {IncomingMessage} req - The http request sent from user
 * @param {ServerResponse} res - The response message sent to user
 */

const get = (req, res) => {
  if (url.parse(req.url).pathname === '/geo/coordinate') {
    getCoords(req, res)
  }

  if (url.parse(req.url).pathname === '/weather/forecast') {
    console.info('here')
    getWeatherForecast(req, res)
  }

  if (url.parse(req.url).pathname === '/bikes') {
    getBikes(req, res)
  }
}

/**
 * Handle the weather forecast request
 * @param {IncomingMessage} req
 * @param {ServerReponse} res
 */

const getWeatherForecast = (req, res) => {
  const city = url.parse(req.url, true).query.city
  const country = url.parse(req.url, true).query.country

  console.info(city, country)

  fetch.weather
    .forecast(city, country)
    .then(data => {
      res.setHeader('Content-Type', 'application/json')

      res.write(JSON.stringify(data))
      res.end()
    })
    .catch(err => console.error(err))
}

/**
 * Handle the Coordinate search request
 * @param {IncomingMessage} req
 * @param {ServerResponse} res
 */

const getCoords = (req, res) => {
  const city = url.parse(req.url, true).query.city
  const country = url.parse(req.url, true).query.country

  fetch.coordinate(city, country).then(data => {
    res.setHeader('Content-type', 'application/json')

    res.write(JSON.stringify(data))
    res.end()
  })
}

const getBikes = (req, res) => {
  const country = url.parse(req.url, true).query.country

  fetch.bike
    .search(country)
    .then(data => {
      res.setHeader('Content-Type', 'application/json')
      res.write(JSON.stringify(data))
      res.end()
    })
    .catch(err => console.info(err))
}

/**
 * Update the bike cache every hour
 */

const updateBikeCache = () => {
  fetch.bike.search('ie').then(data => {
    fetch.bike.cache = data
  })
}

module.exports = {
  start: start
}
