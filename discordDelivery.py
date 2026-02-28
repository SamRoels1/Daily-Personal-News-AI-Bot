import requests


class DiscordSender:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_newsletter(self, text):
        print("\nDelivering to your Discord server...")

        # Discord messages cannot exceed 2000 characters.
        # We split the text into 1900-character chunks to be safe.
        chunks = [text[i:i + 1900] for i in range(0, len(text), 1900)]

        for index, chunk in enumerate(chunks):
            data = {"content": chunk}
            response = requests.post(self.webhook_url, json=data)

            if response.status_code == 204:
                print(f"Chunk {index + 1} sent successfully!")
            else:
                print(f"Failed to send message. Error code: {response.status_code}")