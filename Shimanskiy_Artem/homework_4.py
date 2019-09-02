'''
Task 4 Text Analyzer

Implement Text Analyzer program.
Features:

Calculate words quantity;
Extract text dictionary - unique words;
Find keywords - top 3 most frequent words;
Calculate frequency for each word - word quantity / all words quantity * 100.
Do not analyze such words as a, an, to, is, are, was, were, will, would, could, and, or, if, he, she, it, this, my, etc.

Example:
input: This is my favourite text. Let's try to analyze it. I love this text. I love Python.
output:

words quantity: 9
text dictionary: favourite, text, let's, try, analyze, love, python
keywords: text - 2, love - 2, favourite - 1
frequency: favourite - 11%, text - 22%, let's - 11%, try - 11%, analyze - 11%, love - 22%, python - 11%
'''


text = 'This is my favourite text. Let’s try to analyze it. I love this text. I love Python!'
exclude_symbol = [',', '.', '!', '?', '’']
exclude_words = ['is', 'my', 'is', 'to', 'it', 'i']


def clear_text(text):
    """ This function exclude words and symbols
        :param text: text for clean
        :type text: str
        :return: list words with out exclude words and symbols
        :rtype: list
    """
    for i in exclude_symbol:
        text = text.replace(i, '')

    text = text.lower().split()
    for j in text:
        while j in text:
            text.remove(j)
    return text


def words_count(text_1):
    """ This function counts a number of words in text
        :param text_1: text for count
        :type text_1: str
        :return: len()
        :rtype: int
    """
    return len(text_1)


def frequent_words(text_1):
    """ TThis function counts appearance word in text and sort 3 the most common
        :param text_1: list words
        :type text_1: list
        :return: 3 the most common words in text
        :rtype: str
    """
    frequent_words = [text.count(text_1[x]) for x in range(len(text_1))]
    frequent_words = dict(zip(text_1, frequent_words))
    frequent_words = sorted(frequent_words.items(), key=lambda i: i[1], reverse=True)
    frequent_words = frequent_words[0:3]
    return frequent_words


def calculate_freq(text_1):
    """
        This function calculate the percentage of each word in text
        :param text_1: list words
        :type text_1: list
        :return: dict with words and they percentage of each word in text
        :rtype: dict
    """
    calculate_list = []
    for i in text_1:
        calc = int(text_1.count(i) / len(text_1) * 100)
        calculate_list.append(calc)
    calculate_list = [str(x) + '%' for x in calculate_list]
    frequency = dict(zip(text_1, calculate_list))
    # Calculate frequency for each word - word quantity / all words quantity * 100.
    return frequency


text_1 = clear_text(text)
print(f'words quantity : {words_count(text_1)} ')
print(f'text dictionary : {set(text_1)} ')
print(f'frequent words : {frequent_words(text_1)} ')
print(f'calculate frequent words : {calculate_freq()} ')
