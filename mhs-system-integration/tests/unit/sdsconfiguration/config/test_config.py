import unittest
import os
from sdsconfiguration import config

defaultHostname = 'localhost'
defaultPort = '389'
defaultEnableTLS = False

ldapHostnameKey = 'LDAP_HOSTNAME'
ldapHostname = "another.domain.com"

ldapPortKey = 'LDAP_PORT'
ldapPort = '686'

ldapEnableTLSKey = 'LDAP_ENABLE_TLS'
ldapEnableTLS = True


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

    def test_default_hostname_config(self):
        self.assertEqual(config.getLdapHostname(), defaultHostname)

    def test_environment_var_overrides_hostname_config(self):
        os.environ[ldapHostnameKey] = ldapHostname
        self.assertEqual(config.getLdapHostname(), ldapHostname)

    def test_default_port_config(self):
        self.assertEqual(config.getLdapPort(), defaultPort)

    def test_environment_var_overrides_port_config(self):
        os.environ[ldapPortKey] = ldapPort
        self.assertEqual(config.getLdapPort(), ldapPort)

    def test_default_enable_tls_flag(self):
        self.assertFalse(config.isTLSEnabled())

    def test_environment_var_overrides_enable_tls_flag(self):
        os.environ[ldapEnableTLSKey] = str(ldapEnableTLS)
        self.assertTrue(config.isTLSEnabled())


if __name__ == '__main__':
    unittest.main()
