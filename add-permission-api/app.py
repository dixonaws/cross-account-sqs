from chalice import Chalice
import json
import boto3

app = Chalice(app_name='add-permission-api')

'''
Define a GET method which just returns all of the topics that are eligible for subscription
This method could add logic to limit the list to specific topics
'''
@app.route('/')
def index():
	sns_client = boto3.client("sns")
	dict_topic_list = sns_client.list_topics()
	return (json.dumps(dict_topic_list))

'''
Define an add_permission method which takes an HTTP POST. 
POST a JSON object with keys topic_arn and account_id to create and confirm a subscription
The account_id must be a valid AWS account, or an error will be returned ("A provided account ID is not valid")
This method could add logic to limit subscriptions to specific topics
'''
@app.route("/add_permission", methods=['POST'])
def add_permission():
	json_post_body = app.current_request.json_body

	str_topic_arn = json_post_body["topic_arn"]
	str_account_id = json_post_body["account_id"]
	str_topic=str_topic_arn.split(":")[5]

	sns=boto3.resource("sns")
	topic=sns.Topic(str_topic_arn)

	dict_response = {}
	dict_response["topic_arn"] = str_topic_arn
	dict_response["topic"] = str_topic
	dict_response["account_id"] = str_account_id
	dict_response["action"] = "subscribe"

	try:
		response = topic.add_permission(
			Label="Allow account " + str_account_id + " to subscribe",
			AWSAccountId=[str_account_id],
			ActionName=["Subscribe"]
		)
	except Exception as e:
		dict_response["status"]=str(e.response["ResponseMetadata"]["HTTPStatusCode"]) + ": " + e.response["Error"]["Message"]
		return(dict_response)

	dict_response["status"]=response["ResponseMetadata"]["HTTPStatusCode"]

	return (dict_response)
