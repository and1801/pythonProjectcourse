import re

text = "Hello world! How are you? I'm fine. Thank you!"
sentences = re.split(r'[.!?]', text)
sentences = [s.strip() for s in sentences if s]
print("Список предложений:", sentences)
