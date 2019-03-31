const { describe, it } = require('mocha')
const expect = require('chai').expect
const geo = require('../lib/geo')

describe('Geo Location OK Testing', () => {
  it('should get the correct coordinates information', () => {
    geo.coordinate('dublin', 'ie').catch(err => expect(err).to.null)
  })
})
