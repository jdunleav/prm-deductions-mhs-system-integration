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
