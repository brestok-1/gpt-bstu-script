from environs import Env

env = Env()
env.read_env()

PATH = 'No.docx'
WORD_COUNT = 237

GPT_KEY = env('API_KEY')
