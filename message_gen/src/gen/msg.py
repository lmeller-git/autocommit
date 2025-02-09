from parse.diff import Diff
from huggingface_hub import InferenceClient

client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct")

def summarize(diffs: list[Diff], original: str) -> str:
	messages = [
		{
			"role": "system",
			"content": "You are a llm model, which summarizes git diffs and condenses these into short commit messages.\
						You will work with the original commit messages and a simplified git diff to generate the new message.\
						The commit messages should follow this template:\
						[<type>]<changes>\
						where type is bugfix | fix | optimization | chore | docs | feature and should reflect the changes which were done.\
						changes should be one sentence summarizing the most important changes\
						ex: [docs] added docs in file x for function y\
						this should be encased in {<commit msg>}\
						ex: {[docs] added docs in file x for function y}"
		},
		{
			"role": "user",
			"content": "\n".join([str(diff) for diff in diffs])
		}
	]
	stream = client.chat.completions.create(
		messages = messages,
		max_tokens = 20,
		stream = True
	)
	msg = "".join([chunk.choices[0].delta.content for chunk in stream])
	msg = msg.split("{")[1].split("}")[0]
	return msg

def gen_msg(diffs: list[Diff], original: str) -> str:
	summ = summarize(diffs, original)
	msg = summ + " (generated)" + "\noriginal: " + original
	return msg
	
	
