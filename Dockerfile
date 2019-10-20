FROM python:3.6.5

# Install requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade -r /tmp/requirements.txt

# Copy code
WORKDIR /app
COPY app /app

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
