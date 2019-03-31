const { describe, it } = require('mocha')
const fetch = require('../lib/fetch')
const expect = require('chai').expect

describe('Weather Current Testing', () => {
  it('should return weather currently', () => {
    fetch.weather
      .currently('dublin', 'ie', { currently: true })
      .then(data => {
        expect(data.currently).to.throw
      })
      .catch(err => {
        expect(err).to.throw
      })
  })

  it('should return weather minutely', () => {
    fetch.weather
      .forecast('dublin', 'ie', { minutely: true })
      .then(data => {
        expect(data.minutely).to.throw
      })
      .catch(err => {
        expect(err).to.throw
      })
  })

  it('should return weather hourly', () => {
    fetch.weather
      .forecast('dublin', 'ie', { hourly: true })
      .then(data => {
        expect(data.hourly).to.throw
      })
      .catch(err => expect(err).to.throw)
  })

  it('should return weather daily', () => {
    fetch.weather
      .forecast('dublin', 'ie', { daily: true })
      .then(data => {
        expect(data.daily).to.throw
      })
      .catch(err => expect(err).to.throw)
  })
})
