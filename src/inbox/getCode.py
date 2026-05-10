from mailtm import Email
import httpx

class GetCode:
    message_ids = []

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        self.client = self.__client_build()

    def __client_build(self) -> httpx.Client:
        return httpx.Client(
            http2=True,
            follow_redirects=True
        )

    def __extract_code(self, message: dict) -> str:
        subject = message['subject']

        if " is your 6-digit code" in subject:
            return subject.split(" is your 6-digit code")[0]

        return "No TikTok code found"
    def get_token(self):
        url = "https://api.mail.tm/token"
        payload = {
            "address": self.email,
            "password": self.password
        }
        print(payload)
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(url, headers=headers, json=payload)
       
        response.raise_for_status()
        try:
            token = response.json()['token']
            return token
        except:
            raise Exception("Failed to get token")
    def get(self) -> str:
        try:

            url = "https://api.mail.tm/messages"

            token = self.get_token()
            print(token)

            headers = {
                'Authorization': f'Bearer {token}'
            }

            response = self.client.get(
                url,
                headers=headers
            )

            data = response.json()

            inbox = [
                msg for msg in data['hydra:member']
                if msg['id'] not in self.message_ids
            ]

            if not inbox:
                return "No new messages"

         
            for message in inbox:
                print(inbox)

                subject = message.get("subject", "")

                if " is your 6-digit code" in subject:

                    self.message_ids.append(
                        message['id']
                    )

                    return self.__extract_code(
                        message
                    )

            return "No TikTok code found"

        except Exception as e:
            return str(e)


print(
    GetCode(
        input("Email: "),
        input("Password: ")
    ).get()
)

