import re

# create a tokenizer from scratch
# Goal: tokenize entire text from 'the verdict' (20479 chars)
# Note: super small dataset, so we can use simple character-level tokenization
# SIMPLE, BUT NOT IDEAL

def create_vocab(text):
    with open(text, 'r', encoding='utf-8') as f:
        raw_text = f.read()
        # add punctuation to the regex
        preprocessed  = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
        # remove whitespace - THIS IS AN IMPORTANT DISCUSSION
        preprocessed = [token.strip() for token in preprocessed if token.strip()]
        print(f"length of preprocessed: {len(preprocessed)}")
        all_tokens = sorted(set(preprocessed))

        vocab = {token:integer for integer,token in enumerate(all_tokens)}
        return vocab


class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [token.strip() for token in preprocessed if token.strip()]
        return [self.str_to_int[token] for token in preprocessed]
    
    def decode(self, tokens):
        text = "".join([self.int_to_str[token] for token in tokens])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
vocab = create_vocab('the-verdict.txt')
tokenizer = SimpleTokenizerV1(vocab)

text = """
        "It's the last he painted, you know,"
        Mrs. Gisburn said with pardonable pride.
    """

ids = tokenizer.encode(text)
print(ids)

decoded = tokenizer.decode(ids)
print(decoded)