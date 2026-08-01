FROM python:3.13-slim

WORKDIR /flask-portfolio

RUN pip install --no-cache-dir pipenv==2025.0.4

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

EXPOSE 6001

CMD ["gunicorn", "--bind", "0.0.0.0:6001", "--workers", "2", "api.index:app"]
