import requests


class NewsFetcher:
    def __init__(self, queries):
        # The class needs the URLs when it is created
        self.queries = queries

    def get_top_news(self):
        news_items = []

        for category, url in self.queries.items():
            print(f"Fetching {category} news...")
            response = requests.get(url)
            data = response.json()

            if data.get("status") == "ok":
                news_items.append(f"\n--- {category} News ---")

                articles = data.get("articles", [])
                for article in articles:
                    title = article.get("title")
                    description = article.get("description") or "No description available."
                    news_items.append(f"Title: {title}\nSummary: {description}\n")
            else:
                print(f"Error fetching {category}: {data.get('message')}")

        return "\n".join(news_items)