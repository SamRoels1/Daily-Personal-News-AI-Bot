from google import genai


class NewsSummarizer:
    def __init__(self, api_key):
        # Set up the Gemini client when the class is created
        self.client = genai.Client(api_key=api_key)

    def summarize(self, raw_news):
        print("\nHanding data to Gemini to write your newsletter...")

        prompt = f"""
        You are an expert journalist. I have collected the top news articles of the day across Global, Technology, Science, and European news.

        Please write a cohesive, engaging morning newsletter summarizing the most important points. 
        Do not just list the articles; weave them together into a readable briefing.
        Use clear headings for each category, bullet points for readability, and maintain a professional yet friendly tone.

        Here is the raw data:
        {raw_news}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text