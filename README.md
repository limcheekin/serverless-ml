# serverless-ml
## Overview

The repository created to code along with an Udemy course [Deploy Serverless Machine Learning Models to AWS Lambda](https://www.udemy.com/course/deploy-serverless-machine-learning-models-to-aws-lambda/).

The following are the major differences:

1. I'm using Python 3.8 instead of Python 3.6 in the course and more recent version of dependencies.
2. All examples are setup with continuous deployment by using Github Actions.
3. Code of each example is located in its own branch.

## Branches

### scikit
An example of Serverless project which contains machine learning regression model from scikit-learn trained on California housing dataset.

### spacy
An example of Serverless project which uses a small English model from spaCy NLP framework to create an AWS Lambda endpoint for named entity recognition. 

NOTE: .requirements.zip file created with serverless-python-requirements is omitted due to its size.