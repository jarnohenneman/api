# Deloitte - Cloud engineer assignment

Build an API that will use a string as input and does a find and replace for certain
words and outputs the result.

## Deliverables
- Access to the version control system the sources are hosted (preferably Github or GitLab)  
  https://github.com/jarnohenneman/api  
- The endpoint of the API;  
  Api keys: None  
  Endpoints: POST - https://01lmjziadh.execute-api.eu-central-1.amazonaws.com/dev/validate  
- Postman file, including testcase;  
  [deloitte-api.assignment.json](./deloitte-api.assignment.json)

## List of word that need to be replaced:
- Oracle -&gt; Oracle©
- Google -&gt; Google©
- Microsoft -&gt; Microsoft©
- Amazon -&gt; Amazon©
- Deloitte -&gt; Deloitte©

## Prerequisite
- AWS account  
- Phyton3.8
- AWS CLI 2 (and configured)

## Deployment steps
Download/Install serverless framework, find your distribution steps here;
https://www.serverless.com/framework/docs/getting-started/

When deploying for the first time, or updating run the command

```bash
  cd api/
  sls deploy
```

This will generate a cloudformation template and deploy this to your region.

## Cloudformation resources
- AWS::ApiGateway
- AWS::IAM
- AWS::S3
- AWS::Lambda
- AWS::Logs