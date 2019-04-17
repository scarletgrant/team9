FROM python

WORKDIR /app

COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 9000

RUN pip install numpy
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install aiohttp

# Run app.py when the container launches
CMD ["python", "app.py"]