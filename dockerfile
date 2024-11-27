FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml pyproject.toml

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev 

COPY . .
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
