/**
 * This module is used to fetch real time bike data from JCD server
 * @module bike
 */

const process = require('process')
const https = require('https')
const queryString = require('querystring')
const env = require('./env')

const cache = {}

/**
 * The coordinate object
 * @typedef {Object} Coordinate
 * @property {number} lat
 * @property {number} lon
 */

/**
 * The JSON object return from JCD server
 * @typedef {Object} Station
 * @property {number} number
 * @property {string} contract_name
 * @property {string} name
 * @property {string} address
 * @property {Coordinate} position
 * @property {boolean} banking
 * @property {boolean} bonus
 * @property {string} status
 * @property {number} bike_stands
 * @property {number} available_bike_stands
 * @property {number} available_bike
 * @property {number} last_update
 */

/**
 * This function returns the current stations information
 * in the specified country
 * @function
 * @param {string} country
 * @returns {Promise.<Station>}
 */

const search = country => {
  const query = {
    contract: '',
    apiKey: env.env().bikeToken
  }

  const options = {
    hostname: 'api.jcdecaux.com',
    path: '/vls/v1/stations?',
    method: 'GET',
    headers: {
      Accept: 'application/json'
    }
  }

  return new Promise((resolve, reject) => {
    contracts().then(contracts => {
      let name = ''

      for (const contract of contracts) {
        if (
          contract.country_code !== null &&
          contract.country_code.toLowerCase() === country
        ) {
          name = contract.name
        }
      }

      query.contract = name
      options.path += queryString.stringify(query)

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
          resolve(geoJSON(JSON.parse(data)))
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
  })
}

/**
 * The Contract type
 * @typedef {Object} Contract
 * @property {string} name
 * @property {string} commerical_name
 * @property {string} country_code
 * @property {Array.<string>} cities
 */

/**
 * This function returns a list of contracts
 * @return {Contract}
 */

const contracts = () => {
  const query = {
    apiKey: env.env().bikeToken
  }

  const options = {
    hostname: 'api.jcdecaux.com',
    path: '/vls/v1/contracts?' + queryString.stringify(query),
    method: 'GET',
    headers: {
      Accept: 'application/json'
    }
  }

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
 * The GeoJSON data type
 * @typedef {Object} GeoJSON
 * @property {string} type
 * @property {Feature} features
 */

/**
 * The Feature data type
 * @typedef {Object} Feature
 * @property {string} type
 * @property {number[]} bbox
 * @property {Object} geometry
 * @property {string} geometry.type
 * @property {number[]} geometry.coordinates
 */

/**
 * Generate GeoJSON
 * @param {Station[]} stations - The data return from JCD
 * @returns {GeoJSON}
 */

const geoJSON = stations => {
  let data = {
    type: 'FeatureCollection',
    features: []
  }

  for (const station of stations) {
    data.features.push({
      type: 'feature',
      geometry: {
        type: 'Point',
        coordinates: [station.position.lat, station.position.lng]
      },
      properties: {
        banking: station.banking,
        bonus: station.bonus,
        bike_stands: station.bike_stands,
        available_bike_stands: station.available_bike_stands,
        available_bikes: station.available_bikes,
        status: station.status
      }
    })
  }

  return data
}

module.exports = {
  search: search,
  geoJSON: geoJSON,
  cache: cache
}
