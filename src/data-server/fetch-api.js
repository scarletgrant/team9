/* 
  This is an API to provide the internal server-data to the clients. It serves the following server-data:
    1. Bike-data from bike.js
    2. Weather-data from weather.js
    3. Geo location from geo.js
    4. Distance of the bike stations in relation to the (dynamic) user's location
*/

/**
 * This module provides external APIs for front-end service
 * @module fetch
 */

const geo = require('./geo')
const weather = require('./weather')
const bike = require('./bike')
const distance = require('./distance')

module.exports = {
  coordinate: geo.coordinate,
  weather: weather,
  bike: {
    search: bike.search,
    cache: bike.cache
  },
  distance: {
    coordsInRange: distance.coordsInRange
  }
}
