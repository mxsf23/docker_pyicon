FROM python:3.8.18-slim
WORKDIR /app
COPY get_favico.py .
RUN pip install favicon requests 
ENTRYPOINT [ "python", "get_favico.py","-u"]
CMD ["https://grafana.com"]