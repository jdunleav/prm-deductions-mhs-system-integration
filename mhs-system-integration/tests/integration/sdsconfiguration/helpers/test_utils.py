import unittest
import os

from sdsconfiguration.config import LdapConfig
from sdsconfiguration.helpers.utils import buildLdapEndpoint

ldapEndpoint = "ldap://some.host:123"
ldapsEndpoint = "ldaps://some.host:123"

ldapHostnameKey = 'LDAP_HOSTNAME'
ldapHostname = 'some.host'

ldapPortKey = 'LDAP_PORT'
ldapPort = '123'

ldapEnableTLSKey = 'LDAP_ENABLE_TLS'
ldapEnableTLS = True


class TestHelperUtils(unittest.TestCase):
    """
    Unit level tests for the ldap_service helper utility functions
    """

    def setUp(self) -> None:
        os.environ[ldapHostnameKey] = ldapHostname
        os.environ[ldapPortKey] = ldapPort
        os.environ[ldapEnableTLSKey] = str(ldapEnableTLS)

    def tearDown(self) -> None:
        del os.environ[ldapHostnameKey]
        del os.environ[ldapPortKey]
        del os.environ[ldapEnableTLSKey]

    def test_default_parameters(self):
        endpoint = buildLdapEndpoint()
        self.assertEqual("ldap://localhost:389", endpoint)

    def test_tls_true_should_use_ldaps(self):
        endpoint = buildLdapEndpoint(LdapConfig())
        self.assertEqual(ldapsEndpoint, endpoint)

    def test_tls_false_should_use_ldap(self):
        os.environ[ldapEnableTLSKey] = str(False)
        endpoint = buildLdapEndpoint(LdapConfig())
        self.assertEqual(ldapEndpoint, endpoint)


if __name__ == '__main__':
    unittest.main()
