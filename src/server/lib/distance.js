const coordsInRange = (center, coords, radius) => {
  let result = []

  for (const feature of coords.features) {
    const lat = feature.geometry.coordinates[0]
    const lon = feature.geometry.coordinates[1]

    const distanceToCenter = Math.sqrt(
      (center.lat - lat) * (center.lat - lat) +
        (center.lon - lon) * (center.lon - lon)
    )

    if (distanceToCenter < radius) {
      result.push({ lat, lon })
    }
  }

  return result
}

module.exports = {
  coordsInRange: coordsInRange
}
