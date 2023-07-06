# Question-Answering-over-PDF-using-Langchain-and-Large-Language-Models
I have implemented/demonstrated the sales research use case using Langchain, LLM and vector DB.


In this assignment, our model will summarize the PDF and will be able to answer any relevant questions. Copying and pasting text from pdf or reading it manually and summarizing is not an efficient solution for long pdfs (50-100 pages). Hence using Langchain and LLMs will benefit here.

For example, I have used Pfizer's sales report to get an estimate of the sales figures projected by Pfizer. Also, how much are the sales (exact number), and whether they exceeded their previous earnings based on the report. 

Bonus#1: There are some cases when Langchain cannot find an answer. In such cases, I have added a feature such that our model will leverage LLM to answer such queries (Bonus #1) For example, how is pfizer associated with moderna?, etc. Normal langchain model cannot answer if 'Moderna' is not present in pdf

Bonus#2: I have also implemented an UI which will take input in the form of a UI (asking the user to upload PDF instead of command line) and then paste a query in the text box. The output will then be displayed in the text box.

I have attached 2 scripts, pdf file used and a readme file with all the instructions. Also there are 4 different output files (Outputs 1,2, bonus_1 from command line where you can see query in cmd line or in the code passed as a parameter)  and Output (3 showing UI usecase).





Getting Started:

1. Open anaconda/conda and create a new virtual conda environment (with the Python version) using the below command
   conda create --name env_name python==3.10.9

2. Activate the created conda environment using conda activate {env_name}

3. After step 2, you have entered the new virtual environment. Now, install all the required dependencies for langchain

    pip install langchain
    pip install OpenAI
    pip install chromadb      # this is for vector DB 
    pip install tiktoken      # this is a tokenizer for OpenAI
    pip install pypdf         # this is to use and read pdf through UI (eg upload button to upload pdf)
    pip install panel         # panel will be used to display output in the form of UI (easier for user)

4. Now we need key API key from OpenAI which will be used to make call to OpenAI . 
   1. Go to https://platform.openai.com/account/api-keys
   2. Click Create new secret key (if not created) and save the key
   

 Now, we are all set.


 How to run?

 There are 2 python scripts: Langchain.py and llm_app.py

1. Langchain.py
 Langchain.py will just display the output on the terminal. The query and filepath will be provided by the user in the below way:
 result = qa("C:/Users/asus/Desktop/ABC.pdf", "Summarize X?","stuff",3)  # Passing the path to pdf file
 print (result['result'])


2. llm_app.py
   In order to run the UI python script (llm_app.py), it is recommended to use interactive py environment
   Running it in interactive env will ask the user to upload file from PC and enter the query in textbox and the API key.
   The result will then be displayed in the textbox.


Bonus feature added: Most of the times Langchain says "I don't know" if it can find anything relevant to pdf. In such case I am passing the response to language model and it will show relevant responses.
