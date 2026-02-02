
# ---- base ----
FROM python:3.13-slim

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential curl &&     rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./api/getaround_api.py .
COPY ../models/getaroundmodel.pkl ./model.pkl

# HF Spaces usually expose 7860; Streamlit default is 8501, we map to 7860
ENV PORT=7860
ENV STREAMLIT_SERVER_PORT=7860
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Expose Streamlit and FastAPI ports
EXPOSE 7860
EXPOSE 8000

# Launch both Streamlit and FastAPI
# Note: On HF Spaces, only the first service (Streamlit) will be publicly exposed.
CMD bash -lc "uvicorn app.getaround_api:app --host 0.0.0.0 --port 8000 &               streamlit run app/streamlit_app.py"