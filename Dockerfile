FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["flask", "run" , "--host" , "0.0.0.0" , "--port" , "5000"]