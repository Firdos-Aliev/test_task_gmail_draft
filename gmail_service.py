import base64
import os
import re
from email.message import EmailMessage

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials



class GmailAPIService:

    def __init__(self, token=""):
        # path to token file
        if token != "":
            self._TOKEN_FILE_PATH = token
        else:    
            self._TOKEN_FILE_PATH = os.environ.get("GMAIL_OAUTH_TOKEN", "token.json")
        self._SCOPES = [
            "https://mail.google.com/",
            "https://www.googleapis.com/auth/gmail.modify",
            "https://www.googleapis.com/auth/gmail.compose"
        ]
        # authorize user form OAUTH2 cred
        self.credentials = Credentials.from_authorized_user_file(self._TOKEN_FILE_PATH, self._SCOPES)
        self.service = build("gmail", "v1", credentials=self.credentials)


    def gmail_create_draft(self, to, subject, content):
        # message object
        message = EmailMessage()
        
        if self.check_email(to):
            message["To"] = to
        else:
            return None
        
        message["Subject"] = subject
        message.set_content(content)

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"message": {"raw": encoded_message}}
        draft = self.service.users().drafts().create(userId="me", body=create_message).execute()

        return draft
    
    # email validation
    def check_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        
        if(re.fullmatch(regex, email)):
            return True
        return False


if __name__ == "__main__":
    service = GmailAPIService()
    draft_mail = service.gmail_create_draft(
        "google@gmail.com",
        "test subject",
        "test content"
    )
    print(draft_mail)
