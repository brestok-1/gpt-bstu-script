from environs import Env

env = Env()
env.read_env()

PATH = 'ДАНЯ.docx'
WORD_COUNT = 205

GPT_KEY = env('API_KEY')
