# Hands on IBM Cloud Functions
This is a hands-on workshop walking through creating and using IBM Cloud Functions to process video files stored in IBM Cloud Object Storage. This workshop was originally created for the Tweakers group in the Netherlands.

## Pre-requisites

1. You will need an IBM Cloud account, which you can get for free signing up here: https://ibm.biz/ibm-cloud-functions-account-reg
2. You will need to install the IBM Cloud CLI: https://www.ibm.com/cloud/cli

## Create a Cloud Object Storage instance

1. From the [IBM Cloud](https://cloud.ibm.com) homepage, click on the catalog and choose 'Cloud Object Storage'
![IBM Cloud homepage](_images/cos1.png)
2. Create your free instance of Object Storage.
![IBM Cloud Object Storage creation screen](_images/cos2.png)

# Creating a simple 'hello world' function via the Web Console

1. Click the Cloud Functions icon in the left menu:
![Cloud functions icon](_images/functions1.png)

2. Click on 'Start Creating' on the IBM Cloud Functions homepage
![Cloud functions homepage](_images/functions2.png)

2. Click on 'Action' form the list of entities
![Create entity page](_images/functions3.png)

3. Name your action (e.g. 'hello world') and pick a runtime, in this case `python 3.7`:
![Create an action page](_images/functions4.png)

4. You will be taken to a page in which you can edit code yourself and click 'Invoke' to run it
![Code editor for an action](_images/functions5.png)

5. Actions take a dictionary parameter in which arguments to the function are marshalled. You can change the code to take a name, e.g.:

```python
import sys

def main(dict):
    name = dict.get('name', 'Random Bob')
    return { 'message': f'Hello {name}'}
```




