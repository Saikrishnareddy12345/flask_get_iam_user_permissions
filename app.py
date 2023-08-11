# from flask import Flask, render_template, request
# import boto3

# app=Flask(__name__)
# @app.route('/',methods=['GET','POST'])
# def index():
#     aws_username = request.form['username']
#     client = boto3.client('iam')

#     response = client.list_attached_user_policies(
#     UserName=aws_username)
#     try:
#         ##Get User Information
#         user_info=client.get_user(UserName=aws_username)
#         ##get attached policies
#         user_policies = client.list_attached_user_policies(UserName=aws_username)
#         return render_template('result.html', user_info=user_info, user_policies=user_policies)
#     except Exception as e:
#         error_message = str(e)
#         return render_template('index.html', error=error_message)

#     return render_template('index.html')
# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0',port=80)






# # print(response['AttachedPolicies'])
# # for i in response['AttachedPolicies']:
# #     a=i['PolicyName']
# #     b=i['PolicyArn']
# #     print(f"PolicyName: {a} | PolicyARN: {b}")

from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Replace these values with your AWS credentials
AWS_ACCESS_KEY = 'your_access_key'
AWS_SECRET_KEY = 'your_secret_key'
AWS_REGION = 'us-east-1'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        
        # Connect to AWS using the provided credentials
        session = boto3.Session()
        
        iam_client = session.client('iam')
        
        try:
            user_policies = iam_client.list_attached_user_policies(UserName=username)
            user_permissions = []
            
            for policy in user_policies['AttachedPolicies']:
                user_permissions.append(policy['PolicyName'])
            
            return render_template('index.html', username=username, permissions=user_permissions)
        
        except Exception as e:
            error_message = str(e)
            return render_template('index.html', error=error_message)
    
    return render_template('index.html', username=None, permissions=None)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
