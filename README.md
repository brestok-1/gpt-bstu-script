# <div align="center">Text analysis script 📝</div>

## Description

In practice, I was given a task at university to divide a writer's 80-page work into blocks of approximately 200 words.
Then, I had to analyze each block and identify the two most suitable themes out of forty. I found this task very silly
for my specialization, so I wrote a script that does all of this for me. Then, I was able to sell it to my classmates
and make enough money.

You can use this script to analyze the text by changing the values of WORD_COUNT and changing the query for ChatGPT. You can also get acquainted with the result of the script by going to the data/DANYA folder

## Technologies

***Language***

![Python](https://img.shields.io/badge/-Python-1C1C1C?&style=for-the-badge)

***Libraries***

![openai](https://img.shields.io/badge/-openai-1C1C1C?&style=for-the-badge)
![python-docx](https://img.shields.io/badge/-python--docx-1C1C1C?&style=for-the-badge)
![Re](https://img.shields.io/badge/-re-1C1C1C?&style=for-the-badge)

In this project, I wrote several functions that divide text into blocks. The condition was that each block ended with a
sentence-ending symbol (?, !, ., ..., and others). I split the text into words using regular expressions and found the
last word for each block. Understanding that the text was large, I also obtained the previous and next words to ensure
that I was cutting the text in the right place. And then, finding the index of occurrence, cut the text, getting the
necessary block. Next, I created a request for ChatGPT, sent it to the OpenAI server, used a model for
text analysis (text-davinci-003), and saved the resulting responses to a file.

## Project setup

1. Create and activate a python virtual environment
2. In the terminal, enter the following command:

```
pip3 install -r requirements.txt
```

3. Create a .env file and paste the data from the .env.example file into it
4. Register on the OpenAI website and get an API key
5. Insert the API key value into the API_KEY variable in the .env file
6. In the config.py specify the path to the file .docx with text in the PATH variable
7. In the files.py specify the path to save requests and responses
8. Run the main.py and wait for the script to finish

## <div align="center">Thank you for taking the time to review my project👋</div>
