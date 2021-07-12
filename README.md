# fastapi-mangum-lambda

## Run

```
uvicorn main:app --reload
```


## Deploy to AWS Lambda

### Install serverless framework

```
npm install -g serverless
```

### Install serverless plugins

```
npm install
```

### Deploy it

```
serverless deploy \
    --region 'ap-southeast-1' \
    --stage 'dev' \
    --aws-profile 'default' \
    --iamrole 'paste-your-lambda-arn-role-here'
```

Change the options value with your own:

- region: the AWS region that you wanna used
- aws-profile: the AWS CLI Profile (default will be used if it's not provided)
- stage: the default is dev, but you could change it with do you want (ex: staging)
- iamrole: using the ARN Role that you are copied on the previous step


----------
More explanation about this project is on this story https://dwisulfahnur.medium.com/fastapi-deployment-to-aws-lambda-with-serverless-framework-b637b455142c
