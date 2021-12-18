FROM python:3-windowsservercore
WORKDIR /app

COPY requirements.txt aw64.dll /app/
RUN pip install -r requirements.txt
COPY greeter/ /app/greeter

ENTRYPOINT [ "python /app/greeter" ]