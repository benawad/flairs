#!/bin/bash

source .env
aws s3 cp --profile $PROFILE flairs.txt s3://$BUCKET_NAME
aws s3 cp --profile $PROFILE resized s3://$BUCKET_NAME --recursive