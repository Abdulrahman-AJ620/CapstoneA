# ids_app/utils/openai_utils.py

from openai import OpenAI

client = OpenAI(
    api_key="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"
)


def analyze_log_entry(log_entry):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system",
             "content": "You are the core of an Intrusion Detection engine designed to detect SQL Injection attacks"},
            {"role": "user",
             "content": f"An IDS received the following log entry:\n\"{log_entry}\"\n\nIs this log entry considered an attack? Answer only with Yes it is an attack or No it is legitmate?: "}
        ],
        # stream=True
    )
    return response.choices[0].message.content
