import glob, os
import json
import zipfile
import requests
import psycopg2
import psycopg2.extras
import boto3

def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': "ok"
    }
