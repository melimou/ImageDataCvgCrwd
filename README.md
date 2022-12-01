# ImageDataCvgCrwd
Image data coverage identification using crowdsourcing

This repo is built to implement our algorithms to identify the coverage in an image dataset using Amazon Mechanical Turk. In order to use this code, you need to have:
- An AWS account,
- A dataset of images.

You can replace your aws "access_key" and "secret_access_key" in hit_builder.py and the route of your dataset (which contains the URL of the images you have previously uploaded on cloud space, such as s3) in coverage.py.
Here you can specify the settings of the task as well (subset size, coverage threshold). Please note that if you run this code on AMT Prouction environment, you will be charged by the number of HITs workers accept and finish. After the task is complete, a log of all the generated HITs and the responses will be stored as "log.txt".
