import os


class LdapConfig:

    def __init__(self):

        # TLS Configuration
        self._initialiseIsTLSEnabled()

        # Endpoint
        self._initialiseLdapHostname()
        self._initialiseLdapPort()

        # Certificates
        self._initialiseClientCert()
        self._initialiseClientKey()
        self._initialiseCACert()

    def _initialiseLdapHostname(self):
        """
        Initiates the Hostname information for the target LDAP server

        Sets hostname to the value of LDAP_HOSTNAME env variable or localhost
        """
        self.hostname = os.getenv('LDAP_HOSTNAME', "localhost")

    def _initialiseLdapPort(self):
        """
        Initiates the Port information for the target LDAP server

        Sets port to the value of LDAP_PORT env variable or 389 (ldap)
        """
        self.port = os.getenv('LDAP_PORT', '389')

    def _initialiseIsTLSEnabled(self):
        """
        Initiates the enable TLS flag information to see whether to select 'ldap' or 'ldaps' and if the
        public, private and CA certificates are required.

        Sets isTLSEnabled to true if isTLSEnabled is set, false otherwise (default)
        """
        self.is_TLS_enabled = os.getenv('LDAP_ENABLE_TLS', False)

    def _initialiseClientCert(self):
        """
        Initiates the public certificate location to be able to provide it to the Ldap service for TLS enabled connections.

        This value is required when isTLSEnabled is set to True.

        Sets client_cert path to client certificate if defined, default is empty string
        """
        self.client_cert = os.getenv('LDAP_CLIENT_CERT', "")

    def _initialiseClientKey(self):
        """
        Initiates the client private key location to be able to provide it to the Ldap service for TLS enabled connections.

        This value is required when isTLSEnabled is set to True.

        Sets client_key path to client private key if defined, default is empty string
        """
        self.client_key = os.getenv('LDAP_CLIENT_KEY', "")

    def _initialiseCACert(self):
        """
        Initiates the CA certificate location to be able to provide it to the Ldap service for TLS enabled connections.

        This value is required when isTLSEnabled is set to True.

        Sets ca_cert path to ca certificate if defined, default is empty string
        """
        self.ca_cert = os.getenv('LDAP_CA_CERT', "")
