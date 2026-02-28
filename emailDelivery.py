import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import markdown

class EmailSender:
    def __init__(self, sender_email, sender_password, receiver_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

    def send_email(self, subject, text_content):
        print("\nFormatting and sending email to your inbox...")

        # 1. Convert Gemini's Markdown into HTML
        html_content = markdown.markdown(text_content)

        # 2. Wrap it in beautiful CSS styling
        # This gives it a white card look on a soft gray background, with clean fonts!
        styled_html = f"""
        <html>
            <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f3f4f6; padding: 20px; color: #333333;">
                <div style="max-width: 650px; margin: 0 auto; background-color: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                    <h1 style="color: #2563eb; text-align: center; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">📰 Your Daily Briefing</h1>
                    <div style="line-height: 1.6; font-size: 16px;">
                        {html_content}
                    </div>
                    <p style="text-align: center; font-size: 12px; color: #9ca3af; margin-top: 40px;">
                        Generated automatically by your Python AI Bot 🤖
                    </p>
                </div>
            </body>
        </html>
        """

        # 3. Package the email
        msg = MIMEMultipart()
        # This tells Gmail to display the custom name instead of your raw email address
        msg['From'] = f"Daily News Bot <{self.sender_email}>"
        msg['To'] = self.receiver_email
        msg['Subject'] = subject

        # NOTE: We changed 'plain' to 'html' right here!
        msg.attach(MIMEText(styled_html, 'html'))

        # 4. Connect to Gmail and send
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(msg)
            server.quit()

            print("Email delivered successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")