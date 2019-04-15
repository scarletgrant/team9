FROM node:current-alpine

WORKDIR /app

COPY . /app

RUN npm install

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV GEO_TOKEN pk.eyJ1IjoiYWxnbzQiLCJhIjoiY2p0OGllOWljMDhndDQ1bzc1czh1bW9taCJ9.oisau9Bcb7BxBZfSG4vi0g
ENV WEATHER_TOKEN ae6a76d9d2a422cd7efb48155608e3e5
ENV BIKE_TOKEN 92be62130be380ad2925b05fc3b1e5b3ef1a5a55

# Run app.py when the container launches
CMD ["npm", "start"]