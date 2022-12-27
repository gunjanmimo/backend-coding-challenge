FROM python:3.9


RUN mkdir /app
WORKDIR /app
COPY . .

RUN echo "$PWD"
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
RUN python db_populate.py
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]