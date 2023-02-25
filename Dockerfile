FROM python:3.10

WORKDIR /Tagud

COPY requirements.txt ./

RUN pip3 install -U pip && pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
