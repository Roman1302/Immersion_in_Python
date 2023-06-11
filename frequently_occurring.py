'''В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.'''
from collections import Counter
import string
import wikipedia

NUMBER_WORDS = 10
TITLE_ARTICLE = "Россия"

print(wikipedia.summary(TITLE_ARTICLE))

text = wikipedia.summary(TITLE_ARTICLE)
# print(f'текст{text}')
text_low = text.lower()

text_clear = text_low.translate(str.maketrans('', '', string.punctuation))
# print(f'\n{text_clear}')
text_list = text_clear.split(' ', )

text_list_dict = (Counter(text_list).items())

top_worlds = sorted(text_list_dict, key=lambda x: x[1], reverse=True)[:NUMBER_WORDS]
print(top_worlds)
out = [x for x, y in top_worlds]
print(f'\n10 самых частовстечающихся слов в wikipedia в статье "{TITLE_ARTICLE}" \n{out}')
