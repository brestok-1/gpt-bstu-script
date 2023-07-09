from environs import Env

env = Env()
env.read_env()

PATH = 'chehov.docx'
WORD_COUNT = 205

GPT_API = env('API_KEY')
