FROM python:3.9

RUN apt-get update -y

RUN unlink /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

# set env variables
#PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
#PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV AUTOWRAPT_BOOTSTRAP autodynatrace

COPY app/ /app

WORKDIR /app


RUN pip install --upgrade pip --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
RUN pip install -r requirements.txt --trusted-host=pypi.org --trusted-host=files.pythonhosted.org

RUN apt-get install -y zip
RUN pip3 install --upgrade awscli --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
EXPOSE 8000
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

# CMD ["gunicorn","-b", "0.0.0.0:8000",  "main:app"]