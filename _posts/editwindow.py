import os

full_path = os.path.realpath(__file__)
cwd = os.path.dirname(full_path)
post = "\\2021-04-16-twaw-41621.md"

with open(cwd+post, 'r') as f:
    text = f.read()

print(text)
