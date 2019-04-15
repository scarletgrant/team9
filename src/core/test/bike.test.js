const fetch = require('../lib/fetch')
const expect = require('chai').expect

const { describe, it } = require('mocha')

describe('Contract List OK Testing', () => {
  it('should not report error', () => {
    fetch.bike.search('ie').catch(err => {
      expect(err).to.null
    })
  })
})
