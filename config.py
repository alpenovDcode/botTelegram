import openai
import os
import logging

# Настройка логгера
logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

API_TOKEN = "токен телеграм бота"
ADMINS = []# ваш id для админки

# Установка API-ключа OpenAI
api_key = "API_chatgpt"
openai.api_key = api_key

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,  # Увеличено ограничение на количество токенов
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.RateLimitError as e:
        logger.error(f"Quota exceeded: {e}")
        return "Вы превысили лимит использования API. Пожалуйста, проверьте ваш план и детали биллинга."
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "Произошла ошибка при генерации ответа."