import json
import boto3
import random
from chaos import *

def lambda_handler(event, context):
    if(mode_of_operation='autoscaling'):
        return stop_ec2_instances()
    elif(mode_of_operation=='ecs'):
        return stop_container()
    else:
        return "invalid mode of operation"
