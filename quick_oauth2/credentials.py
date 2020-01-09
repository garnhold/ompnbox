# import quick_oauth2

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

import json
import os.path


def fetch_credentials(client_id_filename, credential_filename, scopes):
    if credential_filename and os.path.isfile(credential_filename):
        return load_credentials(credential_filename, scopes)

    credentials = request_credentials(client_id_filename, scopes)
    save_credentials(credentials, credential_filename)
    return credentials


def load_credentials(credential_filename, scopes):
    return Credentials.from_authorized_user_file(credential_filename, scopes)


def save_credentials(credentials, filename):
    with open(filename, 'w') as f:
        print(json.dumps({
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'id_token': credentials.id_token,
            'scopes': credentials.scopes,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret
        }), file=f)


def request_credentials(client_id_filename, scopes):
    flow = InstalledAppFlow.from_client_secrets_file(client_id_filename, scopes=scopes)

    return flow.run_local_server(
        host='localhost',
        port=8080,
        authorization_prompt_message="",
        success_message='The auth flow is complete; you may close this window.',
        open_browser=True
    )