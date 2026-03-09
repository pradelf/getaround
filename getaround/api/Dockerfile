FROM python:3.9

ENV MLFLOW_EXPERIMENT_NAME=$MLFLOW_EXPERIMENT_NAME
ENV MLFLOW_TRACKING_URI=$MLFLOW_TRACKING_URI
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV BACKEND_STORE_URI=$BACKEND_STORE_URI
ENV ARTIFACT_ROOT=$ARTIFACT_ROOT

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . /app
EXPOSE 7860
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

#CMD ["bash","-lc","fastapi run app.py --host 0.0.0.0 --port ${PORT}"]
