FROM node:current-alpine

WORKDIR /app

COPY . /app

RUN npm install

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["npm", "start"]