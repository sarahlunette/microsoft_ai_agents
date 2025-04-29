FROM python:3.11-slim

# Install system dependencies for Java and jnius
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    gcc \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    cython3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install jnius manually after Cython and Java are ready
RUN pip install pyjnius

COPY . .

EXPOSE 9000 8501

CMD ["bash", "-c", "if [ \"$APP\" = 'streamlit' ]; then streamlit run demo.py --server.port=8501 --server.enableCORS=false; else uvicorn llm_app_generate_on_colab_completed:app --host 0.0.0.0 --port 9000; fi"]
