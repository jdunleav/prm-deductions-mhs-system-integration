import unittest
from sdsconfiguration.config import LdapConfig
from sdsconfiguration.helpers.ldap_connection_factory import LdapConnectionFactory


class TestLdapService(unittest.TestCase):
    """
    Unit level tests for the ldap_connection_builder helper
    """

    def test_default_builder(self):
        self.assertEqual(LdapConnectionFactory.builder().name, "LdapConnectionBuilder")

    def test_default_builder_create(self):
        self.assertEqual(LdapConnectionFactory.builder().create().name, "LdapConnection")

    def test_with_tls_enabled_false(self):
        self.assertEqual(LdapConnectionFactory
                         .builder()
                         .create().isTlsEnabled(), False)

    def test_with_tls_enabled_true(self):
        self.assertEqual(LdapConnectionFactory
                         .builder()
                         .enableTls()
                         .create().isTlsEnabled(), True)

    def test_with_default_ldap_config(self):
        connection_factory = LdapConnectionFactory\
            .builder()\
            .withLdapConfig(LdapConfig())\
            .create()

        self.assertEqual(connection_factory.getEndpoint(), 'ldap://localhost:389')
        self.assertFalse(connection_factory.isTlsEnabled())
        self.assertEqual(connection_factory.getClientCert(), '')
        self.assertEqual(connection_factory.getClientKey(), '')
        self.assertEqual(connection_factory.getCACert(), '')


if __name__ == '__main__':
    unittest.main()
