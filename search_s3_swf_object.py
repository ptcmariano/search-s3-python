"""
searching swf objects in s3

run with docker:
docker build -t search-s3-python-app .
docker run -it --rm -v ~/code/search-s3-python:/usr/src/app --name search-s3-running-app search-s3-python-app > log-all.txt
"""
from boto.s3.connection import S3Connection

aws_access_key=''
aws_secret_key=''

conn = S3Connection(aws_access_key,aws_secret_key)

bucket=''

s3 = conn.get_bucket(bucket)

suffix='.swf>'
runCount=0

all_keys = s3.list()

for key in all_keys:
    if (str(key).endswith(suffix) and not str(key).endswith('versiontest.swf>')):
        print(key)
        runCount = 1+runCount
print('total: '+str(runCount))
