import unittest
from unittest.mock import patch
from sdsconfiguration.helpers.utils import buildLdapEndpoint

ldapEndpoint = "ldap://some.host:123"
ldapsEndpoint = "ldaps://some.host:123"

ldapHostname = 'some.host'
ldapPort = '123'


class TestHelperUtils(unittest.TestCase):
    """
    Unit level tests for the ldap_service helper utility functions
    """

    @patch('sdsconfiguration.config.LdapConfig')
    def setUp(self, ldap_config) -> None:
        self.ldap_config = ldap_config
        self.ldap_config.getHostname.return_value = ldapHostname
        self.ldap_config.getPort.return_value = ldapPort
        self.ldap_config.isTLSEnabled.return_value = False

    def test_each_config_is_called_once(self):
        buildLdapEndpoint(self.ldap_config)
        self.ldap_config.getHostname.assert_called_once()
        self.ldap_config.getPort.assert_called_once()
        self.ldap_config.isTLSEnabled.assert_called_once()

    def test_default_parameters(self):
        endpoint = buildLdapEndpoint()
        self.assertEqual("ldap://localhost:389", endpoint)

    def test_returns_ldap_when_not_isTLSEnabled(self):
        endpoint = buildLdapEndpoint(self.ldap_config)
        self.assertEqual(ldapEndpoint, endpoint)

    def test_returns_ldaps_when_isTLSEnabled(self):
        self.ldap_config.isTLSEnabled.return_value = True
        endpoint = buildLdapEndpoint(self.ldap_config)
        self.assertEqual(ldapsEndpoint, endpoint)


if __name__ == '__main__':
    unittest.main()
