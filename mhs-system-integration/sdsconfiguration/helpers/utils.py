import os

from sdsconfiguration.config import LdapConfig

FILE_NOT_FOUND = 'The file \'{FILE}\' cannot be found'
NOT_A_FILE = 'The defined value \'{FILE}\' is not of type File'
FILE_IS_EMPTY = 'The file \'{FILE}\' cannot be empty'


def buildLdapEndpoint(ldap_config: LdapConfig = LdapConfig()):
    """
    Builds the endpoint (i.e. ldaps://some.url:689) for the LdapService from the LdapConfig

    If isTLSEnabled then it will prefix with 'ldaps' instead of 'ldap'.

    :returns: URL starting with either 'ldap' or 'ldaps'
    """
    endpoint = "ldap"

    if ldap_config.isTLSEnabled():
        endpoint += "s"

    endpoint += "://"
    endpoint += ldap_config.getHostname()
    endpoint += ":"
    endpoint += ldap_config.getPort()

    return endpoint


def _validate_file(path_to_file):
    """
    Validates files by path.

    If path starts with '/' it is assumed to be an absolute path and hence the resource root folder is not
    prepended. Otherwise it will prepend the resources root.

    :raises: FileNotFoundError when the filepath does not exist
    :raises: FileNotFoundError when the filepath points to a location that is not a file
    :raises: ValueError when the file is empty
    """
    if path_to_file.startswith('/'):
        path = path_to_file
    else:
        path = getResourcesRoot() + path_to_file

    # Checks if path exists
    if not os.path.exists(path):
        raise FileNotFoundError(FILE_NOT_FOUND.format(FILE=path_to_file))

    # Checks if path is a file
    if not os.path.isfile(path):
        raise FileNotFoundError(NOT_A_FILE.format(FILE=path_to_file))

    # Checks if file is empty or not
    if os.stat(path).st_size == 0:
        raise ValueError(FILE_IS_EMPTY.format(FILE=path_to_file))


def validateLdapConfig(ldap_config: LdapConfig = LdapConfig()):
    """
    Simple validation of the Ldap Config for the purposes of the testing.

    If TLS is enabled, check that the client cert, key and ca.crt exist.

    :raises: FileNotFoundError when the filepath does not exist
    :raises: FileNotFoundError when the filepath points to a location that is not a file
    :raises: ValueError when the file is empty
    """
    if ldap_config.isTLSEnabled():
        _validate_file(ldap_config.getCACert())
        _validate_file(ldap_config.getClientCert())
        _validate_file(ldap_config.getClientKey())


def getResourcesRoot():
    """
    Gets the relative path to the resources folder for relative paths
    """
    return os.path.dirname(os.path.abspath(__file__)) + '/../../resources/'
