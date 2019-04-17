const http = require('http')
const fetch = require('../lib/fetch')
const url = require('url')
const fs = require('fs')
const axios = require('axios')

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

  addBikeStationRoutine(10 * 1000)
  // addWeatherRoutine(10 * 1000)
}

/**
 * Handle the HTTP GET request
 * @param {IncomingMessage} req - The http request sent from user
 * @param {ServerResponse} res - The response message sent to user
 */

const get = (req, res) => {
  if (url.parse(req.url).pathname === '/api/v1/coordinates') {
    getCoords(req, res)
  }

  if (url.parse(req.url).pathname === '/api/v1/forecast') {
    getWeatherForecast(req, res)
  }

  if (url.parse(req.url).pathname === '/api/v1/weather') {
    getWeatherCurrent(req, res)
  }

  if (url.parse(req.url).pathname === '/api/v1/bikes') {
    getBikes(req, res)
  }

  if (url.parse(req.url).pathname === '/api/v1/pred') {
    getForecastPred(req, res)
  }

  if (url.parse(req.url).pathname === '/map') {
    returnHomePage(req, res)
  }
}

/**
 * Return home page(index.html)
 * @param {InComingMessage} req - The incmoning request
 * @param {ServerResponse} res - The response
 */

const returnHomePage = (req, res) => {
  const home = fs.readFileSync('./index.html')

  res.writeHead(200, {
    'Content-Type': 'text/html'
  })
  res.write(home)
  res.end()
}

/**
 * Handle the weather forecast request
 * @param {IncomingMessage} req
 * @param {ServerReponse} res
 */

const getForecastPred = (req, res) => {
  const city = url.parse(req.url, true).query.city
  const country = url.parse(req.url, true).query.country
  const number = url.parse(req.url, true).query.number

  const options = {
    params: {
      city: city,
      country: country,
      number: number
    }
  }

  axios
    .get(
      `http://${fetch.env().ml.host}:${fetch.env().ml.port}/api/v1/pred`,
      options
    )
    .then(data => {
      res.setHeader('Content-Type', 'application/json')
      res.write(JSON.stringify(data.data))
      res.end()
    })
}

/**
 * Handle the weather forecast request
 * @param {IncomingMessage} req
 * @param {ServerReponse} res
 */

const getWeatherForecast = (req, res) => {
  const city = url.parse(req.url, true).query.city
  const country = url.parse(req.url, true).query.country

  fetch.weather
    .forecast(city, country)
    .then(data => {
      res.setHeader('Content-Type', 'application/json')

      res.write(JSON.stringify(data))
      res.end()
    })
    .catch(err => {
      throw new Error(err)
    })
}

/**
 * Return current weather
 * @param {IncomingMessage} req
 * @param {ServerResponse} res
 */
const getWeatherCurrent = (req, res) => {
  const city = url.parse(req.url, true).query.city
  const country = url.parse(req.url, true).query.country

  fetch.weather
    .currently(city, country)
    .then(data => {
      res.setHeader('Content-Type', 'application/json')

      res.write(JSON.stringify(data))
      res.end()
    })
    .catch(err => {
      throw new Error(err)
    })
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

/**
 * Return current information about of bike station
 * @param {IncomingMessage} req
 * @param {ServerResponse} res
 */
const getBikes = (req, res) => {
  const country = url.parse(req.url, true).query.country

  fetch.bike
    .search(country)
    .then(data => {
      res.setHeader('Content-Type', 'application/json')
      res.write(JSON.stringify(data))
      res.end()
    })
    .catch(err => {
      throw new Error(err)
    })
}

/**
 * Create a new doc in the database
 * @param {Any} dbInstance
 * @param {Object} options
 */
const createDoc = (dbInstance, options) => {
  dbInstance.put(`/${options.db}/${options.id}`, options.data).then(res => {
    return {
      status: res.status,
      id: res.data.id,
      ok: res.data.ok,
      rev: res.data.rev
    }
  })
}

/**
 * Update an existing doc in the database
 * @param {Any} dbInstance
 * @param {Object} options
 */
const updateDoc = (dbInstance, options) => {
  dbInstance
    .head(`/${options.db}/${options.id}`)
    .then(res => {
      if (res.status === 404) {
        createDoc(dbInstance, options)
      } else {
        dbInstance.put(`/${options.db}/${options.id}`, options.data, {
          params: {
            rev: res.headers.ETag
          }
        })
      }
    })
    .catch(err => {
      throw new Error(err)
    })
}

/**
 * Run every interval milesecond
 * Add bike station data to the database
 * @param {Integer} interval
 */
const addBikeStationRoutine = interval => {
  setInterval(() => {
    fetch.bike
      .search('ie')
      .then(data => {
        const features = data.features

        const env = fetch.env()
        const db = axios.create({
          baseURL: `http://${env.db.host}:${env.db.port}`,
          validateStatus: function(status) {
            return true
          }
        })

        for (const feature of features) {
          const options = {
            db: 'station',
            id: feature.properties.last_update,
            data: {
              number: feature.properties.number,
              banking: feature.properties.banking,
              bonus: feature.properties.bonus,
              bike_stands: feature.properties.bike_stands,
              available_bike_stands: feature.properties.available_bike_stands,
              status: feature.properties.status,
              lat: feature.geometry.coordinates[0],
              lon: feature.geometry.coordinates[1]
            }
          }

          updateDoc(db, options)
        }
      })
      .catch(err => {
        throw new Error(err)
      })
  }, interval)
}

/**
 * Add weather forecast every interval milesecond
 * @param {Integer} interval
 */
const addWeatherRoutine = interval => {
  setInterval(() => {
    fetch.weather
      .forecast('dublin', 'ie')
      .then(data => {
        const env = fetch.env()
        const db = axios.create({
          baseURL: `http://${env.db.host}:${env.db.port}`,
          validateStatus: function(status) {
            return true
          }
        })

        for (const [key, value] of Object.entries(data[0].hourly.data)) {
          const options = {
            db: 'forecast',
            id: value.time,
            data: value
          }
          updateDoc(db, options)
        }
      })
      .catch(err => {
        throw new Error(err)
      })
  }, interval)
}

module.exports = {
  start: start
}
