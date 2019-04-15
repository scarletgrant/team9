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
    db: {
      username: table.get('DB_USERNAME'),
      passwd: table.get('DB_PASSWD'),
      database: table.get('DB_NAME'),
      host: table.get('DB_HOST'),
      port: table.get('DB_PORT')
    },
    token: {
      geo: table.get('GEO_TOKEN'),
      weather: table.get('WEATHER_TOKEN'),
      bike: table.get('BIKE_TOKEN')
    },
    ml: {
      host: table.get('ML_HOST'),
      port: table.get('ML_PORT')
    }
  }
}

module.exports = {
  env: env
}
