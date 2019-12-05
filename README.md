# S3 Object Downloader

## Image

Find the image on [Docker Image Hub](https://hub.docker.com/r/pants1/s3-download).

## Run With Docker

The files passed in the `FILES` variable should be a comma-separated-list.

```
docker run \
 -v /<dest>/:/Downloader/Out \ 
 -e ACCESS_KEY=AAAAAAAAAA \
 -e SECRET_KEY=123-abc-dfg \
 -e FULL_BUCKET_URL=https://bucket-name.s3.nl-ams.scw.cloud \
 -e BUCKET=bucket-name \
 -e DIRECTORY=/cdn/certs/ \
 -e FILES=some-file.key,some-file.pem \
 pants1/s3-download
```