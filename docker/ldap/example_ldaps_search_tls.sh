LDAPTLS_CERT=certs/ldap.crt \
LDAPTLS_KEY=certs/ldap.key \
LDAPTLS_CACERT=certs/ca.crt \
ldapsearch -L -v -x -D 'cn=admin,dc=nhs,dc=uk' -w admin -H ldaps://openldap:636 -b dc=nhs,dc=uk '(objectClass=*)' '+' '*'