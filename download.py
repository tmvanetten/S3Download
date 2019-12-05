#!/usr/local/bin/python2.7

import base64
import hashlib
import hmac
import subprocess
import sys
import os
from email.utils import formatdate

s3_access_key = os.environ["ACCESS_KEY"]
s3_secret_key = os.environ["SECRET_KEY"]
s3_bucket_url = os.environ["FULL_BUCKET_URL"]
s3_bucket_name = os.environ["BUCKET"]
directory_path = os.environ["DIRECTORY"]
files = os.environ["FILES"].split(",")

try:
    os.chdir("./Out")
except Exception:
    os.mkdir("./Out")
    os.chdir("./Out")
current_date = formatdate(usegmt=True)

for file_name in files:
    object_bucket_path = "/" + s3_bucket_name + directory_path + file_name

    string_to_sign = "GET" + "\n\n\n" + current_date + "\n" + object_bucket_path
    sig = base64.b64encode(hmac.new(s3_secret_key, string_to_sign, hashlib.sha1).digest())
    auth_header = "Authorization:AWS " + s3_access_key + ":" + sig
    date_header = "Date:" + current_date

    resource_url = s3_bucket_url + directory_path + file_name
    print(resource_url)

    cmd = "wget -S " + resource_url + " --header=\"" + auth_header + "\" \
      --header=\"" + date_header + "\""

    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    while True:
        outbuf = p.stderr.read(1)
        if outbuf == "" and p.poll() is not None:
            break
        if outbuf != "":
            sys.stdout.write(outbuf)
            sys.stdout.flush()
