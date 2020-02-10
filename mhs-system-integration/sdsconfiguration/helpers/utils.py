from sdsconfiguration.config import LdapConfig


def buildLdapEndpoint(ldap_config: LdapConfig = LdapConfig()):
    """
    Builds the endpoint (i.e. ldaps://some.url:689) for the LdapService from the LdapConfig

    If isTLSEnabled then it will prefix with 'ldaps' instead of 'ldap'.

    :returns: URL starting with either 'ldap' or 'ldaps'
    """
    endpoint = "ldap"

    if ldap_config.isTLSEnabled():
        endpoint += "s"

    endpoint += "://"
    endpoint += ldap_config.getHostname()
    endpoint += ":"
    endpoint += ldap_config.getPort()

    return endpoint
