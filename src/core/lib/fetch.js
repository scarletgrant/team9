/* 
  Caution
  This api should not be used in any internal source code or testing file.
  The node will report errors such as xxx is not a function.
  Use it only as a external api
*/

/**
 * This module provides external APIs for front-end service
 * @module fetch
 */

const geo = require('./geo')
const weather = require('./weather')
const bike = require('./bike')
const environment = require('./env')

module.exports = {
  coordinate: geo.coordinate,
  weather: weather,
  bike: {
    search: bike.search,
    cache: bike.cache
  },
  env: environment.env
}
