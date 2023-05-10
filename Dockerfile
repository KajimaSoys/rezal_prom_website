FROM python:3.8

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt


COPY blocks/ /app/blocks/
COPY core/ /app/core/
COPY log/ /app/log/
COPY media/ /app/media/
COPY requests/ /app/requests/
COPY rezal_prom_website/ /app/rezal_prom_website/
COPY static/ /app/static/
COPY templates/ /app/templates/
COPY manage.py /app/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]