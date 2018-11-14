# serverless-chaos-monkey
Serverless Chaos Monkey is a serverless implementation of Netflix Chaos Monkey through AWS Lambdas in Python.
Present functionality involves two modes of operation:
1) **ecs** Mode: Allows you to configure chaos monkey to check resiliency of your ecs cluster by randomly terminating any container instance in your cluster. This is highly useful for micro-services based architectures.
2) **autoscaling** Mode: This is conventional chaos monkey implementation that randomly terminate ec2 instances in your autoscaling group. 

# Configuration
Provide your configuration details in config.py file.
1) mode_of_operation: accepted values: 'autoscaling', 'ecs'.

2)autoscaling_group_name: Name of autoscaling group(**required** if mode_of_operaton= autoscaling)

3)cluster_arn: Arn of ecs cluster (**required** if mode_of_operation= ecs)

## Details of Files
**lambda.py** : Contains lambda handler function.

**config.py** : Provide Configuration details here.

**chaos.py** : Implementation of functions to introduce chaos.

# Deployment

**Iam Policies** : Define a role for lambda and attach following policies:
1) AmazonEC2FullAcess
2) AmazonECS_FullAccess


