def save_requests(question_dict: dict):
    with open('data/LESHA/gpt_requests.txt', 'w') as file:
        for value in question_dict.values():
            file.write(f"{value}\n\n")


def save_gpt_response(gpt_answers: list[str]) -> None:
    with open('data/LESHA/gpt_output.txt', 'w') as file:
        for i, answer in enumerate(gpt_answers):
            file.write(f"№{i+1}: {answer}\n\n")


def save_gpt_answer(i: int, gpt_answers: str) -> None:
    with open('data/LESHA/gpt_answers.txt', 'a') as file:
        file.write(f"№{i + 1}: {gpt_answers}\n\n")
