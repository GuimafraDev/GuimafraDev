FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "src.backend.app:app", "--bind", "0.0.0.0:5000"]