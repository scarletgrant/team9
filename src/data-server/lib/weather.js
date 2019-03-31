/**
 * This module provides weather APIs for external service
 * It has three functions.
 * search - A generic function which returns all weather information
 * currently - A function returns current weather
 * forecast - A function returns forecast weather
 */

const process = require('process')
const geo = require('./geo')
const https = require('https')
const queryString = require('querystring')

/**
 * Return generic weather information
 * @param {number} lat
 * @param {number} lon
 * @param {Object} [opts]
 * @type {string[]} [opts.exclude]
 * @type {string[]} [opts.lang]
 * @type {string} [opts.units]
 * @returns {Object}
 */

const search = (lat, lon, opts) => {
  const query = {
    ...(opts.exclude && { exclude: opts.exclude.join(',') }),
    ...(opts.lang && { lang: opts.lang.join(',') }),
    ...(opts.units && { units: opts.units.join(',') })
  }

  const options = {
    hostname: 'api.darksky.net',
    path: `/forecast/${
      process.env.WEATHER_TOKEN
    }/${lat},${lon}?${queryString.stringify(query)}`,
    method: 'GET',
    headers: {
      Accept: 'application/json'
    }
  }

  console.info(options.path)

  return new Promise((resolve, reject) => {
    const req = https.request(options, res => {
      if (res.statusCode !== 200) {
        reject({
          code: res.statusCode,
          message: res.statusMessage
        })
      }

      let data = ''

      res.on('data', chunk => {
        data += chunk
      })

      res.on('end', () => {
        resolve(JSON.parse(data))
      })
    })

    req.on('error', err => {
      reject({
        code: 400,
        message: err
      })
    })

    req.end()
  })
}

/**
 * Return current weather
 * @param {string} city
 * @param {string} country
 * @returns {Object}
 */

const currently = (city, country) => {
  return new Promise((resolve, reject) => {
    geo
      .coordinate(city, country)
      .then(data => {
        const options = {
          exclude: ['minutely', 'hourly', 'daily', 'alerts', 'flags']
        }
        search(data.lat, data.lon, options)
          .then(data => {
            return data
          })
          .catch(err => {
            reject(err)
          })
      })
      .then(data => {
        resolve(data.currently)
      })
      .catch(err => {
        reject(err)
      })
  })
}

/**
 * Return weather forecast
 * @param {string} city
 * @param {string} country
 * @returns {Promise<Object>}
 */

const forecast = (city, country) => {
  return new Promise((resolve, reject) => {
    geo
      .coordinate(city, country)
      .then(data => {
        const options = {
          exclude: ['currently', 'minutely', 'daily', 'alerts', 'flags']
        }

        const tasks = data.map(location => {
          return search(location.lat, location.lon, options)
        })

        Promise.all(tasks)
          .then(data => {
            resolve(data)
          })
          .catch(err => console.error(err))
      })
      .catch(err => {
        reject(err)
      })
  })
}

module.exports = {
  search: search,
  currently: currently,
  forecast: forecast
}
