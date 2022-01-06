# Overview

![example workflow](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/actions/workflows/pythonapp.yml/badge.svg)

This is second project for Udacity Azure DevOps course: Building a CI/CD Pipeline. 

## Project Plan

* A link to a Trello board for the project
 [link](https://trello.com/b/ChL89FXI/udacity-2nd)
* A link to a spreadsheet that includes the original and final project plan
 [link](project-management-udacity-2nd.xlsx)

## Instructions

![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/diagram-2nd.jpg)
###### *Screenshot taken from Udacity page in Cloud DevOps using Microsoft Azure course*

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
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/create%20an%20app%20service%20and%20deploy%20app.JPG)

* Project cloned into Azure Cloud Shell
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/project%20cloned%20into%20ACS.JPG)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/local%20test%20passed.JPG)

* Output of a test run
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/lint%20and%20test%20in%20GIT%20UI.JPG?raw=true)

* Successful deploy of the project in Azure Pipelines.
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/successful%20deploy%20of%20the%20project%20in%20azure%20pipelines.JPG)

* Running Azure App Service from Azure Pipelines automatic deployment
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/running%20azure%20app%20service%20from%20pipelines.JPG)

* Successful prediction from deployed flask app in Azure Cloud Shell.
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/perform%20prediction.JPG)

* Output of streamed log files from deployed application
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/logs1.JPG)
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/logs2.JPG)
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/logs3.JPG)
 ![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/logs4.JPG)

[Locust report](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/locust-report.pdf)
![Screenshot](https://github.com/TMagdalena/udacity-azuredevops-2nd-project/blob/main/locust-success.jpg)

## Enhancements

* Do not push on main branch
* Push on separate branches
* Create PRs
* Start pipeline only on PRs

## Demo 

[YouTube video](https://youtu.be/F-6iMsZTBRA)
[Better quality video](https://kapwi.ng/c/YbUUChToAz)

This is edited in Azure CLI.
