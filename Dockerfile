FROM python:3.12

WORKDIR /bot

COPY requirements.txt /bot

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]