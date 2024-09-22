# install a slim Python image
FROM python:3.11-slim

# install the requests package
RUN pip install --no-cache-dir requests

# move a Python script into the image
COPY script.py /app/

# set the working directory
WORKDIR /app

# run the script
# note the '-u' flag which will run
# the script with unbuffered output, forcing print 
# to display immediately in logs
CMD ["python", "-u", "agent.py"]
