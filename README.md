# Overview

This is second project for Udacity Azure DevOps course: Building a CI/CD Pipeline. 

## Project Plan

* A link to a Trello board for the project
* [a link](https://trello.com/b/ChL89FXI/udacity-2nd)
* A link to a spreadsheet that includes the original and final project plan>
* [a relative link](project-management-udacity-2nd.xlsx)

## Instructions

Architectural Diagram
[a link](https://classroom.udacity.com/nanodegrees/nd082/parts/42614ad1-72a7-4cdf-8119-cbfacad88d57/modules/53c5d9eb-3795-4066-af43-68379c2c2650/lessons/f5d7c13a-0cea-4cc3-981e-3d0aa9d1b73d/concepts/c84a9d8b-89b0-4668-a014-f72ef73fcc0f)

Steps:
1.  Launch an Azure Cloud Shell environment, create ssh-key and upload it to your GitHub account.
2.  Create project scaffolding from files provided in this repository.
3.  Make local test
4.  Clone project to Cloud Shell
5.  Configure GitHub Actions
6.  Create continous delivery in Azure
7.  Enable continous deployment iz Azure Pipelines
8.  Enable GitHub actions to worth with Azure Piplens
9.  Make a final test and stream logs

For more info about each step, take a look at the screenshots below and the demo section.

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>



## This was edited in Cloud Shell

![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/lint%20and%20test%20in%20GIT%20UI.JPG?raw=true)
