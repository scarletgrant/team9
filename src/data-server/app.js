/**
This JS app is build to do three jobs: 
1. Fetch data from remote service providers JCD, OPenWeatherApp, Google GEO coding service
2. It will process the data request from request.py and sends it back to request.py
3. It provides a cache for the whole application, meaning the results are stored in the server's cache memory
 */


const http = require('http')
const fetch = require('../lib/fetch')
const url = require('url')

// Creates a remote server that listens for the requests from request.py
const start = port => {
  const server = http.createServer((req, res) => {
    if (req.method == 'GET') {
      get(req, res)
    }
  })

  // Error handling
  server.on('error', err => {
    throw new Error(err)
  })

  // Listens on the port for requests from request.py
  server.listen(port)

    //Cache is disabled for now while testing:
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

// Get's the requests from the client via the url path that we will set upt to be generated in the frond end HTML files
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

// Get's the forecast request from the client via the url path that we will set upt to be generated in the frond end HTML files
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

// Converts the location data from the request to coordinates and returns coordinates to the request.py
const getCoords = (req, res) => {
  const city = url.parse(req.url, true).query.city
  const country = url.parse(req.url, true).query.country

  fetch.coordinate(city, country).then(data => {
    res.setHeader('Content-type', 'application/json')

    res.write(JSON.stringify(data))
    res.end()
  })
}

// Get's the bike data request from the client via the url path that we will set upt to be generated in the frond end HTML files
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
 * Updates the bike cache every hour
 */

const updateBikeCache = () => {
  fetch.bike.search('ie').then(data => {
    fetch.bike.cache = data
  })
}

module.exports = {
  start: start
}
