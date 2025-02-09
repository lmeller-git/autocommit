from parse.diff import Diff
from huggingface_hub import InferenceClient
import re

client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct")

system_msg = "You are a llm model, which summarizes git diffs and condenses these into short commit messages.\
						You will work with the original commit messages and a simplified git diff to generate the new message.\
						The commit messages should follow this template:\
						[<type>]<changes>\
						where type is bugfix | fix | optimization | chore | docs | feature and should reflect the changes which were done.\
						changes should be one sentence summarizing the most important changes\
						ex: [docs] added docs in file x for function y\
						this should be encased in {<commit msg>}\
						ex: {[docs] added docs in file x for function y}\
						Return ONLY the commit message exactly in the format: {[<type>] <changes>}. The Curly Braces MUST be present.\
						Examples:\
Example 1:\
Git diff:\
--- a/file.py\
+++ b/file.py\
@@ -1,4 +1,4 @@\
- print('Hello World')\
+ print('Hello, LangChain')\
Commit message: {[fix] updated greeting message in file.py}\
\
Example 2:\
Git diff:\
--- a/docs.md\
+++ b/docs.md\
@@ -10,7 +10,7 @@\
- Added basic usage instructions.\
+ Expanded usage instructions for clarity.\
Commit message: {[docs] expanded usage instructions in docs.md}"


# TODO: diff parsing: remove noise from diffs and highlight important changes
#       model: look for different models, which might fit better
#       model: try chain of thought like process: model1 summarizes the diff into key changes, model2 takes this summary to generate commit msg, ...
#       model: tune hyperparameters

def summarize(diffs: list[Diff], original: str) -> str:
	messages = [
		{
			"role": "system",
			"content": system_msg
		},
		{
			"role": "user",
			"content": f"original: {original}\n" + "\n".join([str(diff) for diff in diffs])
		}
	]
	# print("input: ", "\n".join([str(diff) for diff in diffs]))
	stream = client.chat.completions.create(
		messages = messages,
		max_tokens = 200,
		temperature = 0.2,
		stream = True
	)
	msg = "".join([chunk.choices[0].delta.content for chunk in stream])
	# print("output: ", msg)
	ismatch = re.search(r'\{(\[.*?\].*?)\}', msg)
	if ismatch:
			msg = ismatch.group(1)
	else:
		msg = msg.strip()	
	return msg

def gen_msg(diffs: list[Diff], original: str) -> str:
	summ = summarize(diffs, original)
	msg = summ + " (generated)" + "\noriginal: " + original
	return msg
	
	
