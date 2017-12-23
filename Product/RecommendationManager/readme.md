# Recommendation Manager
This is the recommendation manager

## Prerequisites
Python 3.4.3

## Running the tests
Explain how to run the tests here

## Folder structure
* docs - Put documentation here
* example - Some examples to get started
* tests - Tests here
* scripts - Scripts for creating a database here
* archive - Old files no longer in use. Kept for future reference


## lightfm determinism
lightm is not deterministic when fitting a new model. However if the model has already been
fitted and the precision@k is checked on the same model it will produce the same results.