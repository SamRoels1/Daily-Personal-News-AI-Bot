import config
from newsFetcher import NewsFetcher
from newsSummarizer import NewsSummarizer
from discordDelivery import DiscordSender
from emailDelivery import EmailSender

def main():
    print("Starting the Daily News Curator...\n")

    # 1. Create the objects (instantiation)
    fetcher = NewsFetcher(config.NEWSAPI_QUERIES, config.THENEWSAPI_QUERIES, config.ARTICLE_COUNT)
    ai_editor = NewsSummarizer(config.GEMINI_API_KEY)
    discord = DiscordSender(config.DISCORD_WEBHOOK_URL)

    # 2. Create the Email object
    email_bot = EmailSender(config.SENDER_EMAIL, config.SENDER_PASSWORD, config.RECEIVER_EMAIL)

    # Run the workflow
    raw_data = fetcher.get_all_news()
    final_newsletter = ai_editor.summarize(raw_data)

    print("\n" + "=" * 40)
    print("📰 YOUR DAILY NEWSLETTER 📰")
    print("=" * 40 + "\n")
    print(final_newsletter)

    # Deliver the news!
    discord.send_newsletter(final_newsletter)

    # 3. Send the email!
    email_bot.send_email("Your Daily AI News Briefing 🗞️", final_newsletter)


if __name__ == "__main__":
    main()