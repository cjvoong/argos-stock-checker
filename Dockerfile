FROM python:3

ADD check_argos_stock.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD ["python","./check_argos_stock_v2.py"]

