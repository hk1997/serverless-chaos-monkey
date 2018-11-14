import json
import boto3
import random
from config import *

#randomly stops any container in given ecs cluster
def stop_container():
    client=boto3.client('ecs')

    if(cluster_arn=='' or cluster_arn==None):
        return "No Cluster Arn Specified"

    #retrieving ist of active containers
    containers = client.list_container_instances(
    cluster=cluster_arn,
    status='ACTIVE',
    maxResults=100)['containerInstanceArns']

    print("number of containers initially",len(containers))


    if(len(containers)==0):
        return "No container running"

    #randomly selecting a container
    container_down = random.randint(0,len(containers)-1)
    print(container_down, "down arn=", containers[container_down] )


    #degregistering a container at random
    res= client.deregister_container_instance(cluster=cluster_arn,
    containerInstance=str(containers[container_down]),
    force=True)

    #listing remaining containers
    containers = client.list_container_instances(
    cluster=cluster_arn,
    status='ACTIVE',
    maxResults=100)['containerInstanceArns']

    print("number of containers now",len(containers))

    return {"remaining containers":len(containers)}


#randomly stops ec2 instances in given autoscaling group
def stop_ec2_instances():
    asg_client = boto3.client('autoscaling')

    if(autoscaling_group_name=='' or autoscaling_group_name==None):
        return "No Autoscaling group provided"

    asg_response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[autoscaling_group_name])

    instance_ids = [] # List to hold the instance-ids

    for i in asg_response['AutoScalingGroups']:
        for k in i['Instances']:
            instance_ids.append(k['InstanceId'])

    instance_down = random.randint(0,len(instance_ids)-1)

    ec2_client = boto3.client('ec2')
    response = ec2_client.terminate_instances(InstanceIds=[instance_ids[instance_down]],DryRun=False)

    return {'terminating instances':response['TerminatingInstances']}
