# cross-account-sqs
Enable SNS topics in account-a to publish to SQS queues in account-b

- Account A will contain an SNS topic called 'orders-incoming'
- Account B will contain an SQS queue called 'orders-incoming'

Publishing a message to the 'orders-incoming' topic will result in a message being 
enqueued into the orders-incoming queue in Account B.

## Create the orders-incoming SNS topic
<code>aws sns create-topic --name "orders-incoming"</code>


