FROM python:3.13-slim

WORKDIR /flask-portfolio

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 6001

CMD ["gunicorn", "--bind", "0.0.0.0:6001", "--workers", "2", "api.index:app"]
