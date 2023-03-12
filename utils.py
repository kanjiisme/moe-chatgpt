import re
import nltk
nltk.download('punkt') 

def clean_text(text):
    text = remove_code_text(text)
    paragraphs = text.split('\n')
    cleaned_sentences = []

    for paragraph in paragraphs:
        sentences = nltk.sent_tokenize(paragraph)

        for sentence in sentences:
            cleaned_sentence = ' '.join(sentence.split())
            if cleaned_sentence != "" and cleaned_sentence is not None:
                cleaned_sentences.append(cleaned_sentence)

    return cleaned_sentences

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