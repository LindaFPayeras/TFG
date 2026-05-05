import ollama
import os


def call_ollama(prompt):
    response = ollama.generate(model='llama3', prompt=prompt)
    return response['response']

