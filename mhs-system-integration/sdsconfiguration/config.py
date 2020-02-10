import os


def getLdapHostname():
    """
    Gets the Hostname information for the target LDAP server

    :returns: Value of LDAP_HOSTNAME env variable or localhost
    """
    return os.getenv('LDAP_HOSTNAME', "localhost")


def getLdapPort():
    """
    Gets the Port information for the target LDAP server

    :returns: Value of LDAP_PORT env variable or 389 (ldap)
    """
    return os.getenv('LDAP_PORT', '389')


def isTLSEnabled():
    """
    Gets the enable TLS flag information to see whether to select 'ldap' or 'ldaps' and if the
    public, private and CA certificates are required.

    :returns: true if isTLSEnabled is set, false otherwise (default)
    """
    return os.getenv('LDAP_ENABLE_TLS', False)


def getClientCert():
    """
    Gets the public certificate location to be able to provide it to the Ldap service for TLS enabled connections.

    This value is required when isTLSEnabled is set to True.

    :returns: path to client certificate if defined, default is empty string
    """
    return os.getenv('LDAP_CLIENT_CERT', "")


def getClientKey():
    """
    Gets the client private key location to be able to provide it to the Ldap service for TLS enabled connections.

    This value is required when isTLSEnabled is set to True.

    :returns: path to client private key if defined, default is empty string
    """
    return os.getenv('LDAP_CLIENT_KEY', "")


def getCACert():
    """
    Gets the CA certificate location to be able to provide it to the Ldap service for TLS enabled connections.

    This value is required when isTLSEnabled is set to True.

    :returns: path to ca certificate if defined, default is empty string
    """
    return os.getenv('LDAP_CA_CERT', "")
