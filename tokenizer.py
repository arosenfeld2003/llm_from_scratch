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
        # sort and remove duplicates
        all_tokens = sorted(set(preprocessed))
        # add unknown token and end of text token
        all_tokens.extend(["<|endoftext|>", "<|unk|>"])
        vocab = {token:integer for integer,token in enumerate(all_tokens)}
        return vocab


class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [token.strip() for token in preprocessed if token.strip()]
        # replace unknown tokens with <|unk|> token
        preprocessed = [
            item if item in self.str_to_int 
            else "<|unk|>" for item in preprocessed
        ]
        return [self.str_to_int[token] for token in preprocessed]
    
    def decode(self, tokens):
        text = " ".join([self.int_to_str[token] for token in tokens])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text


# Testing

# vocab = create_vocab('the-verdict.txt')
# tokenizer = SimpleTokenizerV2(vocab)

# tokenizer = SimpleTokenizerV2(vocab)

# text1 = "Hello, do you like tea?"
# text2 = "In the sunlit terraces of the palace."

# text = " <|endoftext|> ".join((text1, text2))
# print(text)

# print(tokenizer.encode(text))

# print(tokenizer.decode(tokenizer.encode(text)))
