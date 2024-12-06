# Rupan

Rupan is a tool that helps you to extract information from your AWS account.

## Starting

These instructions will help you start the project.

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

### Installing

```
pip install -r requirements.txt
```

### Configuration

With the AWS CLI installed, we can proceed with the configuration.

In this step, it is necessary to configure the IAM user that will be used by the application.
Make sure you have the AWS ACCESS KEY and AWS SECRET KEY of the user.

#### Add the profile

You can add the profile with the command below.

```
aws configure
```

### Executing

### Unused Lambda Functions

To list all unused Lambda functions, run the command below.

```
python3 rupan.py unused-lambda-functions
```

### Need Help?

If you want to see the command help, just run:

```
python3 rupan.py --help
```
