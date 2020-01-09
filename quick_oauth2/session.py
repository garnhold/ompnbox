import quick_oauth2

from google.auth.transport.requests import AuthorizedSession


def fetch_session(client_id_filename, credential_filename, scopes):
    return AuthorizedSession(quick_oauth2.fetch_credentials(client_id_filename, credential_filename, scopes))


def load_session(credential_filename, scopes):
    return AuthorizedSession(quick_oauth2.load_credentials(credential_filename, scopes))


def request_session(client_id_filename, scopes):
    return AuthorizedSession(quick_oauth2.request_credentials(client_id_filename, scopes))