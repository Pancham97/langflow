FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
  && pip install -e .

EXPOSE 7860

CMD ["python", "-m", "langflow", "run", "--host", "0.0.0.0", "--port", "7860"]
