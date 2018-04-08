import json


def jsonify(content):
	return json.dumps(content)


def responsify(status_code, body):
	return {
		'statusCode': status_code,
		'body': jsonify(body),
		'headers': {
            "Access-Control-Allow-Origin": "*"
        }
	}