import time

import openai

from config import GPT_KEY
from files import save_gpt_answer
from parse import get_q_dict


def get_gpt_answers(text) -> list[str]:
    question_dict = get_q_dict(text)
    openai.api_key = GPT_KEY
    gpt_answers = []
    for i, prompt in enumerate(question_dict.values()):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=600,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        answer = response['choices'][0]['text']
        if answer == '' or answer is None:
            raise '''Something was wrong'''
        print(answer)
        save_gpt_answer(i=i, gpt_answers=answer)
        gpt_answers.append(answer)
        time.sleep(20)
    return gpt_answers
