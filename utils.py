import re
import nltk
nltk.download('punkt') 

def clean_text(text):
    text = remove_code_text(text)
    paragraphs = text.split('\n')
    cleaned_paragraphs = []

    for paragraph in paragraphs:
        cleaned_paragraph= ' '.join(paragraph.split())
        if cleaned_paragraph!= "" and cleaned_paragraph is not None:
            cleaned_paragraphs.append(cleaned_paragraph)
            

    return cleaned_paragraphs

def remove_code_text(text):

    return re.sub(r'```.*?```', '', text, flags=re.DOTALL)

if __name__ == "__main__":
    text = '''
    This is a paragraph with some `inline code`.
    
    Here is some code:

    ```python
    def greet(name):
        print("Hello, " + name + "!")

    greet("World")
    ```
    That was some code.
    '''

    print(clean_text(text))