import unittest
from sdsconfiguration.helpers.ldap_service import LdapService

ldapEndpoint = "ldap://localhost:389"
ldapsEndpoint = "ldaps://localhost:686"

class TestLdapService(unittest.TestCase):
    """
    Unit level tests for the ldap_service helper
    """

    def setUp(self) -> None:
        self.ldap_service = LdapService()

    def test_ldapservice_endpoint_should_have_default(self):
        self.assertEqual(self.ldap_service.endpoint, ldapEndpoint)

    def test_ldapservice_can_override_endpoint(self):
        self.ldap_service = LdapService(ldapsEndpoint)
        self.assertEqual(self.ldap_service.endpoint, ldapsEndpoint)


if __name__ == '__main__':
    unittest.main()
