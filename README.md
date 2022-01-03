# Overview

This is second project for Udacity Azure DevOps course: Building a CI/CD Pipeline. 

## Project Plan

* A link to a Trello board for the project
 [a link](https://trello.com/b/ChL89FXI/udacity-2nd)
* A link to a spreadsheet that includes the original and final project plan>
 [a relative link](project-management-udacity-2nd.xlsx)

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

## Enhancements

* Do not push on main branch
* Push on separate branches
* Create PRs
* Start pipeline only on PRs

## Demo 

<TODO: Add link Screencast on YouTube>

