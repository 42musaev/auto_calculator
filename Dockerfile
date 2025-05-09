FROM python:3.12-slim
RUN apt-get update && apt-get install -y build-essential
WORKDIR /app
COPY . .
RUN pip install .
EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
