FROM python:3.12-slim

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

# use root account
USER root

#Install the gears
RUN apt-get update -y
RUN apt-get install nano unzip curl -y
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# create user account
RUN useradd -m -u 1000 user
# RUN useradd -ms /bin/bash user
RUN mkdir /app 
RUN chown -R user /app

# use user account
USER user

ENV HOME=/app\
    PATH=/app/.local/bin:$PATH

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt


COPY --chown=user . /app
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
EXPOSE $PORT

CMD fastapi run app.py --port $PORT --reload
