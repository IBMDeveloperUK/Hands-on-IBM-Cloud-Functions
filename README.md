# Hands on IBM Cloud Functions
This is a hands-on workshop walking through creating and using IBM Cloud Functions to process video files stored in IBM Cloud Object Storage. This workshop was originally created for the Tweakers group in the Netherlands.

## Pre-requisites

1. You will need an IBM Cloud account, which you can get for free signing up here: https://ibm.biz/ibm-cloud-functions-account-reg
2. You will need to install the IBM Cloud CLI: https://www.ibm.com/cloud/cli
3. log into IBM Cloud via the CLI and target the default group:

```bash
$ ibmcloud login --sso
$ ibmcloud target -g Default
```

4. Install the cloud functions and object storage plugins

```bash
$ ibmcloud plugin install cloud-functions
$ ibmcloud plugin install cloud-object-storage
```

## Create a Cloud Object Storage instance

1. From the [IBM Cloud](https://cloud.ibm.com) homepage, click on the catalog and choose 'Cloud Object Storage'
  ![IBM Cloud homepage](_images/cos1.png)

2. Create your free instance of Object Storage.
  ![IBM Cloud Object Storage creation screen](_images/cos2.png)

3. Create a bucket that we will need for this workshop, give each bucket a name, and ensure that the resilience is
set to *regional* and set `eu-gb` as the region..
  ![Creating a bucket in COS](_images/cos3.png)
  ![Naming the bucket](_images/cos4.png)

4. Repeat the step above again to create a second bucket.

5. We should have two buckets now:
  ![List of our two buckets](_images/cos5.png)

# Creating a simple 'hello world' function via the Web Console

1. Click the Cloud Functions icon in the left menu: \
  ![Cloud functions icon](_images/functions1.png)

2. IMPORTANT: Create a new namespace for our functions:
  ![Create namespace drop down](_images/namespaces1.png)

3. Give your namespace the name `tweakers` and choose the location, in this case we will use `London` to match our Object Storage.
  ![Details of our namespace](_images/namespaces2.png)

4. Click on 'Start Creating' on the IBM Cloud Functions homepage
  ![Cloud functions homepage](_images/functions2.png)

5. Click on 'Action' form the list of entities
  ![Create entity page](_images/functions3.png)

6. Name your action `hello_world` and pick a runtime, in this case `python 3.7`:
  ![Create an action page](_images/functions4.png)

7. You will be taken to a page in which you can edit code yourself and click 'Invoke' to run it
  ![Code editor for an action](_images/functions5.png)

8. Actions take a dictionary parameter in which arguments to the function are marshalled. You can change the code to take a name, e.g.:

    ```python
    import sys

    def main(dict):
        name = dict.get('name', 'Random Bob')
        return { 'message': f'Hello {name}'}
    ```

9. Click on 'Invoke with parameters' to set the parameters for the call
  ![Change Action inputs screen](_images/functions6.png)

10. Click 'Invoke' to now run the action with the parameters
  ![Action output with parameters](_images/functions7.png)



## Calling our function from the CLI

1. First we need to target the `tweakers` namespace
    ```bash
    % ibmcloud fn namespace target tweakers
    ok: whisk namespace set to tweakers
    ```

2. We can list our functions, we should see the one we just created:
    ```bash
    % ibmcloud fn action list
    actions
    /25ec8f7a-8e10-422a-94bf-7e7f8d7d8fd9/hello_world                      private python:3.7
    ```

3. We can invoke our action from the CLI:
    ```bash
    % ibmcloud fn action invoke hello_world --result
    {
        "message": "Hello Random Bob"
    }
    % ibmcloud fn action invoke hello_world --result --param name Matt
    {
        "message": "Hello Matt"
    }
   ```
   

    