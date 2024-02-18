import os
import sys

sys.path.append(os.path.abspath("src"))

from models import llm, llm1

model = llm1

def summarise(user_query,text):
    prompt_template = f"Provide a detailed response to the following question based on the context provided.\nQuestion: {user_query}\nContext:\n{text}"
    
    result = model.invoke(prompt_template)

    if model == llm:
        return result.content
    else:
        return result
