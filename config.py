from environs import Env

env = Env()
env.read_env()

PATH = 'LESHYA.docx'
WORD_COUNT = 210

GPT_KEY = env('API_KEY')
