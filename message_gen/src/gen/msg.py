from parse.diff import Diff
from huggingface_hub import InferenceClient

client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.1")


def gen_msg(diffs: list[Diff]):
    r = str(diffs[0])
    r = [
        {
            "role": "system",
            "message": "you are a llm, which condenses git diffs into commit messages",
        },
        {"role": "user", "message": r},
    ]
    print(client.chat_completion(r))
    pass
