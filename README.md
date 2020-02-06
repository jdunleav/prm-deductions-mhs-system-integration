# prm-deductions-mhs-system-integration

## Goals

Create system integration tests for the MHS Adapter and supporting environment, including:
* Validate that SDS is returning the expected Accredited System information
* Validate that SDS is returning the expected Message Handing System information (Endpoint)
* Verify that using the credentials (public and private keys and ca certificate) we are able to successfully make a PDS request
* Perform a PDS request using the MHS Adaptor

## Pre-requisites

* Python3
    * [virtualenv](https://docs.python.org/3/library/venv.html)
    * [kudulab/dojo](https://github.com/kudulab/dojo)

## Testing

There are three levels of testing: 
* Unit - unit level testing of the components within this project
* Integration - integration level testing of the components within this project
* System Integration (Functional) - System Integration level testing of MHS Adapter and the supporting environment

### Unit Testing

Using Python Dojo

```bash
$ ./tasks unit_tests
``` 

In terminal 

```bash

# Switch to virtual environment
$ source venv/bin/activate

# Install requirements 
(venv)$ pip install -r requirements.txt

# Runs the unit tests
(venv)$ python -m unittest discover tests/unit
```

### Integration Testing

Using Python Dojo

```bash
$ ./tasks integration_tests
``` 

In terminal 

```bash

# Switch to virtual environment
$ source venv/bin/activate

# Install requirements 
(venv)$ pip install -r requirements.txt

# Runs the integration tests
(venv)$ python -m unittest discover tests/integration
```

### System Integration Testing

Using Python Dojo

```bash
$ ./tasks functional_tests
``` 

In terminal 

```bash

# Switch to virtual environment
source venv/bin/activate

# Install requirements 
(venv)$ pip install -r requirements.txt

# Runs the functional tests
(venv)$ python -m unittest discover tests/functional
```
