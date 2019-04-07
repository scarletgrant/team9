const Sequelize = require('sequelize')

class Connection {
  constructor(env) {
    this.host = env.host
    this.port = env.port || 5432
    this.database = env.database
    this.dialect = env.dialect || 'postgres'
    this.username = env.username
    this.passwd = env.passwd
  }

  connect() {
    return new Sequelize(this.database, this.username, this.passwd, {
      host: this.host,
      dialect: 'postgres',
      pool: {
        max: 3
      }
    })
  }
}

module.exports = {
  Connection: Connection
}
