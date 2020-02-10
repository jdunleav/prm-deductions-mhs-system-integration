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

## Environment Variables

| Environment Variable | Description                                                              | Default Value |
|----------------------|--------------------------------------------------------------------------|---------------|
| LDAP_HOSTNAME        | Defines the hostname of the target LDAP server                           | 'localhost'   |
| LDAP_PORT            | Defines the port of the target LDAP server                               | '389'         |
| LDAP_ENABLE_TLS      | True: will use 'ldaps://' (requires public, private and ca certificates) | False         |
| LDAP_CLIENT_CERT     | Path to client certificate for TLS enabled connections                   | ''            | 
| LDAP_CLIENT_KEY      | Path to client private key for TLS enabled connections                   | ''            |
| LDAP_CA_CERT         | Path to CA Certificate for TLS enabled connection                        | ''            |

`LDAP_CLIENT_CERT`, `LDAP_CLIENT_KEY`, and `LDAP_CA_CERT` are paths to the resource. If they start with `/`, it is assumed that 
an absolute path is provided. Otherwise, it will prepend the resources root folder and expects a relative path such 
as `certs/ca.crt`.

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

# Docker LDAP

docker-compose-itest.yml

| Service         | Description                                   | Ports       |
|:---------------:|:----------------------------------------------|-------------|
| mhs-python-dojo | Python dojo environment containing ldap-utils |             |
| phpldapadmin    | Admin console for openldap server             | 8080        |
| openldap        | OpenLDAP server                               | 389 (ldap)  |
|                 |                                               | 636 (ldaps) | 
## Admin Console

The phpldapadmin console is running on port `8080`:

Username: `cn=admin,dc=nhs,dc=uk`
Password: `admin`

## Command line (ldapsearch)

The scripts [example_ldap_search](docker/ldap/example_ldap_search.sh) and 
[example_ldaps_search_tls](docker/ldap/example_ldaps_search_tls.sh) demonstrate how we can
connect to the openldap docker instance using `ldap` and `ldaps` (using TLS). 

The volume for the certificates have been mounted to stop them being re-generated.

To run these and see the response:
```bash
$ dojo -c Dojofile-itest

# LDAPS (ldapsearch)
# You need to be in the docker/ldap folder to run this
# You will get 'ldap_sasl_bind(SIMPLE): Can't contact LDAP server (-1)' if you are not
(mhs-python-dojo)$ ./example_ldaps_search_tls.sh

# LDAP (ldapsearch)
# From the docker/ldap folder
(mhs-python-dojo)$ ./example_ldap_search.sh 
```