FROM moditamam/selenium:python3
RUN pip install flask
WORKDIR /app
# Copy the current directory contents into the container as /app
COPY *.py /app/
COPY Score.txt /app/

# Make port 80 available to the world outside this container
EXPOSE 5001

# Run app.py when the container launches
CMD python3 MainScores.py