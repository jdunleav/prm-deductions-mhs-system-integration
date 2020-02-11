import unittest
import os
from sdsconfiguration.config import LdapConfig

defaultHostname = 'localhost'
defaultPort = '389'
defaultEnableTLS = False

ldapHostnameKey = 'LDAP_HOSTNAME'
ldapHostname = "another.domain.com"

ldapPortKey = 'LDAP_PORT'
ldapPort = '686'

ldapEnableTLSKey = 'LDAP_ENABLE_TLS'
ldapEnableTLS = True

ldapClientCertKey = 'LDAP_CLIENT_CERT'
ldapClientCert = './path/to/client_cert.crt'

ldapClientPrivateKey = 'LDAP_CLIENT_KEY'
ldapClientPrivate = './path/to/client_key.pem'

ldapCACertKey = 'LDAP_CA_CERT'
ldapCACert = './path/to/ca_cert.crt'


class TestConfig(unittest.TestCase):
    """
    Unit level tests for the sdsconfiguration config
    """

    def tearDown(self) -> None:
        if ldapHostnameKey in os.environ:
            del os.environ[ldapHostnameKey]

        if ldapPortKey in os.environ:
            del os.environ[ldapPortKey]

        if ldapEnableTLSKey in os.environ:
            del os.environ[ldapEnableTLSKey]

        if ldapClientCertKey in os.environ:
            del os.environ[ldapClientCertKey]

        if ldapClientPrivateKey in os.environ:
            del os.environ[ldapClientPrivateKey]

        if ldapCACertKey in os.environ:
            del os.environ[ldapCACertKey]

    def test_default_hostname_config(self):
        self.assertEqual(LdapConfig().getHostname(), defaultHostname)

    def test_environment_var_overrides_hostname_config(self):
        os.environ[ldapHostnameKey] = ldapHostname
        self.assertEqual(LdapConfig().getHostname(), ldapHostname)

    def test_default_port_config(self):
        self.assertEqual(LdapConfig().getPort(), defaultPort)

    def test_environment_var_overrides_port_config(self):
        os.environ[ldapPortKey] = ldapPort
        self.assertEqual(LdapConfig().getPort(), ldapPort)

    def test_default_enable_tls_flag(self):
        self.assertTrue(type(LdapConfig().isTLSEnabled()) is bool)
        self.assertFalse(LdapConfig().isTLSEnabled())

    def test_environment_var_overrides_enable_tls_flag(self):
        os.environ[ldapEnableTLSKey] = str(ldapEnableTLS)
        self.assertTrue(type(LdapConfig().isTLSEnabled()) is bool)
        self.assertTrue(LdapConfig().isTLSEnabled())

    def test_default_client_cert_config(self):
        self.assertEqual(LdapConfig().getClientCert(), "")

    def test_environment_var_override_client_cert(self):
        os.environ[ldapClientCertKey] = ldapClientCert
        self.assertEqual(LdapConfig().getClientCert(), ldapClientCert)

    def test_default_client_key_config(self):
        self.assertEqual(LdapConfig().getClientKey(), "")

    def test_environment_var_override_client_key(self):
        os.environ[ldapClientPrivateKey] = ldapClientPrivate
        self.assertEqual(LdapConfig().getClientKey(), ldapClientPrivate)

    def test_default_ca_cert_config(self):
        self.assertEqual(LdapConfig().getCACert(), "")

    def test_environment_var_override_ca_cert(self):
        os.environ[ldapCACertKey] = ldapCACert
        self.assertEqual(LdapConfig().getCACert(), ldapCACert)


if __name__ == '__main__':
    unittest.main()
