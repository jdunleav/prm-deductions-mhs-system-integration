DEFAULT_ENDPOINT = "ldap://localhost:389"


class LdapService:

    def __init__(self, ldap_endpoint: str = DEFAULT_ENDPOINT):
        self.endpoint = ldap_endpoint
