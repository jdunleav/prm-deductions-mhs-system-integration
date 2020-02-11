from sdsconfiguration.config import LdapConfig
from sdsconfiguration.helpers.utils import validateLdapConfig, buildLdapEndpoint


class LdapConnectionFactoryBuilder:
    """
    Fluent builder for LDAP connection
    """

    def __init__(self):
        self.name = "LdapConnectionBuilder"
        self.client_cert = ''
        self.client_key = ''
        self.ca_cert = ''
        self.endpoint = ''
        self.tlsEnabled = False

    def enableTls(self):
        """
        Enables TLS when creating Connection

        :returns: this builder
        """
        self.tlsEnabled = True
        return self

    def withLdapConfig(self, config: LdapConfig):
        """
        Validates the config before continuing
        """
        validateLdapConfig(config)

        self.endpoint = buildLdapEndpoint(config)
        self.tlsEnabled = config.isTLSEnabled()
        self.client_cert = config.getClientCert()
        self.client_key = config.getClientKey()
        self.ca_cert = config.getCACert()

        return self

    def create(self):
        """
        Creates an instance of the LdapConnectionFactory

        :returns: LdapConnectionFactory
        """
        return LdapConnectionFactory(self)


class LdapConnectionFactory:
    """
    Creates an Immutable LDAP Connection Factory based on the inputs from the builder
    """

    def __init__(self, builder: LdapConnectionFactoryBuilder):
        self.name = "LdapConnection"
        self.__endpoint = builder.endpoint
        self.__tlsEnabled = builder.tlsEnabled
        self.__client_cert = builder.client_cert
        self.__client_key = builder.client_key
        self.__ca_cert = builder.ca_cert

    def isTlsEnabled(self):
        return self.__tlsEnabled

    def getEndpoint(self):
        return self.__endpoint

    def getClientCert(self):
        return self.__client_cert

    def getClientKey(self):
        return self.__client_key

    def getCACert(self):
        return self.__ca_cert

    @staticmethod
    def builder():
        return LdapConnectionFactoryBuilder()

