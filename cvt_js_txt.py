import os
import json
from openai import OpenAI
from transformers import GPT2Tokenizer

def get_summary(context, tot_tokens=2000):
    return context
    '''
    tokens = tokenizer.tokenize(context)
    half_tokens = tot_tP1+rOQ\P1+rOR\okens // 2

    start_tokens = tokens[1000:1000 + half_tokens]
    end_tokens = tokens[-(1000 + half_tokens):1000]

    summary_tokens = start_tokens + end_tokens
    summary = tokenizer.convert_tokens_to_string(summary_tokens)
    
    return summary
    '''


clses = ['mix']
for cls in clses:
    with open(f'../datasets/unique_contexts/{cls}_unique_contexts.json', mode='r') as f:
        unique_contexts = json.load(f)

    summaries = [get_summary(context) for context in unique_contexts]

    total_description = "\n\n".join(summaries)

    file_path = f"./exp_lightrag/input/{cls}_questions.txt"
    with open(file_path, "w") as file:
        file.write(total_description)

    print(f"{cls}_questions written to {file_path}")
