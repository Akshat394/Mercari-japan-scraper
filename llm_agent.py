import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Translate text between English and Japanese using OpenAI
def translate_text(text, dest_lang):
    prompt = f"Translate the following text to {'Japanese' if dest_lang == 'ja' else 'English'}:\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=256,
    )
    return response.choices[0].message.content.strip()

# Use OpenAI to extract search intent and filters from a user query
def extract_search_intent(user_query, language="en"):
    system_prompt = (
        "You are a shopping assistant for Mercari Japan. "
        "Given a user's request, extract the following as JSON: "
        "- keywords (list of strings)\n"
        "- category (string, optional)\n"
        "- min_price (float, optional)\n"
        "- max_price (float, optional)\n"
        "- tags (list of strings, optional)\n"
        "If the query is in Japanese, return keywords in Japanese. If in English, return in English. "
        "If the user specifies a language, respect it."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        temperature=0.2,
        max_tokens=256,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

# Use OpenAI to generate reasoned recommendations for top products
def recommend_products(products, user_query, language="en"):
    system_prompt = (
        "You are a helpful shopping assistant for Mercari Japan. "
        "Given a user's request and a list of products (as JSON), select the top 3 that best match the user's needs. "
        "For each, provide a short reason for your recommendation. "
        "Output as a JSON list: [{title, price, reason, url}]."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"User request: {user_query}\nProducts: {products}"}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        temperature=0.3,
        max_tokens=512,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content 