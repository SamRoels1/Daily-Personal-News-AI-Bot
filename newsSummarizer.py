from google import genai


class NewsSummarizer:
    def __init__(self, api_key):
        # Set up the Gemini client when the class is created
        self.client = genai.Client(api_key=api_key)

    def summarize(self, raw_news):
        print("\nHanding data to Gemini to write your newsletter...")

        prompt = f"""You are an objective news intelligence analyst and Editor-in-Chief. I am providing you with a large batch of raw news articles across Global, Technology, Science, and European news.

        Your primary task is to FILTER this data. You must evaluate the articles and SELECT ONLY the top 3 to 5 most critical, globally significant, and impactful stories from each category. Prioritize major geopolitical conflicts, groundbreaking tech/science, and massive economic shifts. Ignore minor, local, or trivial news.

        For the highly significant stories you select, provide a comprehensive, strictly factual, and unbiased briefing. 
        Do not use conversational filler, introductions, or attempt to be "entertaining." Include all vital facts, numbers, quotes, and context provided in the raw data. 

        Format requirements:
        - Group the selected news by category with clear headings.
        - For EVERY selected story, the title MUST be a clickable Markdown link. You MUST use the exact "URL:" provided for that specific article in the raw data. Do NOT make up or hallucinate URLs. Format it exactly like this: [Insert Story Title Here](Insert Exact URL Here)
        - Below the title, provide a detailed, multi-bullet summary of all the facts.

        Here is the raw data:
        {raw_news}"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text