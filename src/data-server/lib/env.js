const fs = require('fs')

/**
 * @typedef {Object} Env
 * @property {string} Env.username
 * @property {string} Env.passwd
 * @property {string} Env.database
 * @property {string} Env.host
 * @property {string} Env.geoToken
 * @property {string} Env.weatherToken
 * @property {string} Env.bikeToken
 */

/**
 * Read environment variables from system
 * @returns {Env}
 */

const env = () => {
  const file = fs.readFileSync('./.env', { encoding: 'utf8' })
  const table = new Map()

  file.split('\n').forEach(line => {
    const key = line.split('=')[0]
    const value = line.split('=')[1]
    table.set(key, value)
  })

  return {
    username: table.get('DB_USERNAME'),
    passwd: table.get('DB_PASSWD'),
    database: table.get('DB_NAME'),
    host: table.get('DB_HOST'),
    geoToken: table.get('GEO_TOKEN'),
    weatherToken: table.get('WEATHER_TOKEN'),
    bikeToken: table.get('BIKE_TOKEN')
  }
}

module.exports = {
  env: env
}
