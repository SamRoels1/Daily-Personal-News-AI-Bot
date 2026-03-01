import requests
from datetime import datetime

class NewsFetcher:
    def __init__(self, newsapi_queries, thenewsapi_queries, article_count=10):
        # We now accept both dictionaries
        self.newsapi_queries = newsapi_queries
        self.thenewsapi_queries = thenewsapi_queries
        self.article_count = article_count

    def format_date(self, raw_date):
        # A quick helper to keep the code clean
        if not raw_date:
            return "Unknown Date"
        try:
            parsed_date = datetime.fromisoformat(raw_date.replace('Z', '+00:00'))
            return parsed_date.strftime("%B %d, %Y")
        except ValueError:
            return raw_date

    def get_all_news(self):
        all_news_items = []
        categories = self.newsapi_queries.keys()

        for category in categories:
            all_news_items.append(f"\n--- {category} News ---")
            print(f"Aggregating {category} news...")

            # --- 1. Fetch from NewsAPI ---
            try:
                response1 = requests.get(self.newsapi_queries[category])
                data1 = response1.json()
                if data1.get("status") == "ok":
                    for article in data1.get('articles', [])[:self.article_count]:
                        title = article.get('title', 'No Title')
                        description = article.get('description', 'No Description')
                        url = article.get('url', 'No URL')
                        date = self.format_date(article.get('publishedAt', ''))
                        all_news_items.append(f"Title: {title}\nDate: {date}\nURL: {url}\nSummary: {description}\n")
            except Exception as e:
                print(f"NewsAPI Error for {category}: {e}")

            # --- 2. Fetch from TheNewsAPI ---
            try:
                response2 = requests.get(self.thenewsapi_queries[category])
                data2 = response2.json()
                if "data" in data2:
                    for article in data2.get('data', [])[:self.article_count]:
                        title = article.get('title', 'No Title')
                        description = article.get('snippet', 'No Description') # uses 'snippet'
                        url = article.get('url', 'No URL')
                        date = self.format_date(article.get('published_at', '')) # uses 'published_at'
                        all_news_items.append(f"Title: {title}\nDate: {date}\nURL: {url}\nSummary: {description}\n")
            except Exception as e:
                print(f"TheNewsAPI Error for {category}: {e}")

        # Join the massive aggregated list into one text block for Gemini
        return "\n".join(all_news_items)