FROM python:2.7

WORKDIR /Downloader

COPY download.py .

CMD ["python", "download.py"]