import boto3
import argparse
import sys

sns = boto3.resource("sns")
topic = sns.Topic("arn:aws:sns:us-east-1:477157386854:orders-incoming")

parser=argparse.ArgumentParser()
parser.add_argument('subscribing_accountId')
args=parser.parse_args()

str_subscribing_accountId=args.subscribing_accountId

sys.stdout.write("Adding subscribe permissions for account " + str_subscribing_accountId + "... ")

response = topic.add_permission(
	Label="Allow external account to subscribe",
	AWSAccountId=[str_subscribing_accountId],
	ActionName=["Subscribe"]
)

print("done")



