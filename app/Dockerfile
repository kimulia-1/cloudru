FROM python:3.9

WORKDIR /home
ARG AUTHOR=Max
ENV AUTHOR="${AUTHOR}"
ARG UUID="123e4567-e89b-12d3-a456-426655440000"
ENV UUID="${UUID}"


COPY ./conditions.txt /home/conditions.txt
COPY ./main.py /home/main.py

RUN pip install --no-cache-dir --upgrade -r /home/conditions.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]