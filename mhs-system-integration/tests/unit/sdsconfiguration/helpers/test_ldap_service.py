import unittest
from sdsconfiguration.helpers.ldap_service import LdapService


class TestLdapService(unittest.TestCase):
    """
    Unit level tests for the ldap_service helper
    """

    def test_should_be_true(self):
        self.assertTrue(True)

    def test_should_take_ldap_endpoint(self):
        ldap_service = LdapService()
        self.assertIsNotNone(ldap_service)


if __name__ == '__main__':
    unittest.main()
