# install a slim Python image
FROM python:3.11-slim

# install the requests package
RUN pip install --no-cache-dir requests

# move a Python script into the image
COPY script.py /app/

# set the working directory
WORKDIR /app

ENV PYTHONUNBUFFERED=1

# run the script
CMD ["python", "script.py"]
