FROM python

WORKDIR /app

COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

RUN pip install aiohttp

# Run app.py when the container launches
CMD ["python", "app.py"]