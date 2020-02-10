import unittest
import os

from unittest.mock import patch
from sdsconfiguration.helpers.utils import buildLdapEndpoint, getResourcesRoot, validateLdapConfig

ldapEndpoint = "ldap://some.host:123"
ldapsEndpoint = "ldaps://some.host:123"

ldapHostname = 'some.host'
ldapPort = '123'

CLIENT_CERT_PATH = "certs/ldap.crt"
CLIENT_KEY_PATH = "certs/ldap.key"
CA_CERT_PATH = "certs/ca.crt"
NOT_A_FILE = 'test/not_a_file'
EMPTY_FILE = 'test/empty_file.txt'


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
        self.ldap_config.getClientCert.return_value = CLIENT_CERT_PATH
        self.ldap_config.getClientKey.return_value = CLIENT_KEY_PATH
        self.ldap_config.getCACert.return_value = CA_CERT_PATH

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

    def test_get_resources_root_returns_valid_path(self):
        resourcesRoot = getResourcesRoot()
        self.assertTrue(os.path.exists(resourcesRoot))
        self.assertTrue(os.path.isdir(resourcesRoot))

    def test_validation_fails_when_ca_cert_not_specified(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getCACert.return_value = 'does_not_exist'

        with self.assertRaises(FileNotFoundError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The file \'does_not_exist\' cannot be found', str(context.exception))

    def test_validation_fails_when_ca_cert_is_not_a_file(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getCACert.return_value = NOT_A_FILE

        with self.assertRaises(FileNotFoundError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The defined value \'test/not_a_file\' is not of type File', str(context.exception))

    def test_validation_fails_when_ca_cert_empty(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getCACert.return_value = EMPTY_FILE

        with self.assertRaises(ValueError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The file \'test/empty_file.txt\' cannot be empty', str(context.exception))

    def test_validation_fails_when_client_cert_not_specified(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getClientCert.return_value = 'does_not_exist'

        with self.assertRaises(FileNotFoundError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The file \'does_not_exist\' cannot be found', str(context.exception))

    def test_validation_fails_when_client_cert_is_not_a_file(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getClientCert.return_value = NOT_A_FILE

        with self.assertRaises(FileNotFoundError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The defined value \'test/not_a_file\' is not of type File', str(context.exception))

    def test_validation_fails_when_client_cert_empty(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getClientCert.return_value = EMPTY_FILE

        with self.assertRaises(ValueError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The file \'test/empty_file.txt\' cannot be empty', str(context.exception))

    def test_validation_fails_when_client_key_not_specified(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getClientKey.return_value = 'does_not_exist'

        with self.assertRaises(FileNotFoundError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The file \'does_not_exist\' cannot be found', str(context.exception))

    def test_validation_fails_when_client_key_is_not_a_file(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getClientKey.return_value = NOT_A_FILE

        with self.assertRaises(FileNotFoundError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The defined value \'test/not_a_file\' is not of type File', str(context.exception))

    def test_validation_fails_when_client_key_empty(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getClientKey.return_value = EMPTY_FILE

        with self.assertRaises(ValueError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The file \'test/empty_file.txt\' cannot be empty', str(context.exception))

    def test_absolute_path_is_working(self):
        self.ldap_config.isTLSEnabled.return_value = True
        self.ldap_config.getCACert.return_value = "/" + CA_CERT_PATH  # Chosen file that we know exists

        with self.assertRaises(FileNotFoundError) as context:
            validateLdapConfig(self.ldap_config)

        self.assertEqual('The file \'/certs/ca.crt\' cannot be found', str(context.exception))

    def test_validation_passes_when_all_certs_and_keys_are_valid(self):
        self.ldap_config.isTLSEnabled.return_value = True
        validateLdapConfig(self.ldap_config)


if __name__ == '__main__':
    unittest.main()
