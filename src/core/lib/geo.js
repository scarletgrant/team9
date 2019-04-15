/**
 * This module provides geo location serach service
 * @module geo
 */

const https = require('https')
const queryString = require('querystring')
const env = require('./env')

/**
 * The QueryOption type
 * @typedef {Object} QueryOption - The option used as the search filter
 * @property {string} endpoint - Default value mapbox.places
 * @property {string} search_text - The location you want to search
 * @property {boolean} autocomplete - Enable or disable auto complete
 * @property {Array.<number>} bbox - The boundary of a location
 * @property {string} country - The country for the location
 * @property {boolean} fuzzyMatch - Exactly or approximately when search
 * @property {string} language - The language display on the user interface
 * @property {number} limit - The number of results returned
 * @property {Array.<number>} proximity -The location where closed to the desire location
 * @property {boolean} routing - Wether provides routing information
 * @property {string} types - The type for the searched location
 */

/**
 * The GeoInfo Type
 * @typedef {Object} GeoInfo
 * @property {string} type - The feature collection
 * @property {Array.<string>} query - The query you typed
 * @property {Array.<Feature>} features
 * @property {string} attribution
 */

/**
 * The Feature type
 * @typedef {Object} Feature
 * @property {string} id - {types}.{id}
 * @property {string} type
 * @property {Array.<string>} place_type - The list of types
 * @property {number} relevance
 * @property {string} [address] - The full address for the searched location
 * @property {Object} properties - Deprecated
 * @property {string} text - The city name
 * @property {string} place_name - The full address
 * @property {Array.<number>} bbox
 * @property {Array.<number>} center
 * @property {Geometry} geometry
 * @property {Array.<Context>} context
 */

/**
 * The Geometry type
 * @typedef {Object} Geometry
 * @property {string} type
 * @property {Array.<number>} coordinates
 */

/**
 * The Context type
 * @typedef {Object} Context
 * @property {string} id - {type}.{id}
 * @property {string} short_code
 * @property {string} wikidata
 * @property {string} text
 */

/**
 * This function used to search the geo information of a city
 * To get more precise information, the user should provide both
 * the city and its country
 * @param {string} city - The city you want to search
 * @param {string} country - The country you want to search
 * @param {QueryOption} opts - The search filter
 * @returns {GeoInfo}
 */

const search = (city, country, opts) => {
  const endpoint = opts.endpoint || 'mapbox.places'
  const searchText = city

  let query = {
    /**
     * Required properties
     */
    autocomplete: opts.autocomplete || true,
    country: country,
    access_token: env.env().token.geo,
    /**
     * Optional properties
     */
    ...(opts.bbox && { bbox: opts.bbox }),
    ...(opts.fuzzyMatch && { fuzzyMatch: opts.fuzzyMatch }),
    ...(opts.language && { language: opts.language }),
    ...(opts.limit && { limit: opts.limit }),
    ...(opts.proximity && { proximity: opts.proximity }),
    ...(opts.routing && { routing: opts.routing }),
    ...(opts.types && { types: opts.types })
  }

  const options = {
    hostname: 'api.mapbox.com',
    path: `/geocoding/v5/${endpoint}/${searchText}.json?${queryString.stringify(
      query
    )}`,
    method: 'GET',
    header: {
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
 * The Coordinate type
 * @typedef {Object} Coordinate
 * @property {number} lat
 * @property {number} lon
 * @property {Array.<number>} box - The boundary of the location
 * @property {string} address - The string representation of the full address
 */

/**
 * This function returns the coordinate information
 * @param {string} city - The city
 * @param {string} country - The country
 * @returns {Promise<Coordinate>}
 */

const coordinate = (city, country) => {
  return new Promise((resolve, reject) => {
    const options = {
      fuzzyMatch: true,
      autocomplete: false,
      routing: false,
      limit: 5,
      type: 'address'
    }

    search(city, country, options)
      .then(features => {
        if (features.features.length !== 0) {
          let coords = []

          for (const coord of features.features) {
            // If the coordincate is not relevant
            if (coord.relevance <= 0.5) {
              continue
            }

            const lat = coord.center[1]
            const lon = coord.center[0]
            const box = coord.bbox
            const address = coord.place_name

            coords.push({ lat, lon, box, address })
          }
          resolve(coords)
        } else {
          reject({
            code: 404
          })
        }
      })
      .catch(err => {
        console.error(err)
      })
  })
}

module.exports = {
  search: search,
  coordinate: coordinate
}
