#!/bin/bash

curl https://www.kroger.com/product/images/large/front/000000000406 > cucumber.jpg
aws s3 cp cucumber.jpg s3://ds2002-acv7qc/
aws s3 presign --expires-in 604800 s3://ds2002-acv7qc/cucumber.jpg
