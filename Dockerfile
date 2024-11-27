FROM python:3.9-slim
EXPOSE 8088
WORKDIR /app
COPY /build/memes.py .
ENTRYPOINT ["python", "-u", "memes.py"]