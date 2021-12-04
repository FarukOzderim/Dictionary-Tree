# Dictionary-Tree
An efficient dictionary tree to store banned words and search for banned words for a given string.

It returns the first found banned word in the string.


_By FarukOzderim_

## Usage
```python3
from dictionary_tree import DictionaryTree

tree = DictionaryTree()
tree.add_words(["kill", "dead", "suicide"])

sentence = "I will kill you."
found_word = tree.search_for_banned_words(sentence)
print(f"Sentence 1 first banned word: {found_word}")

sentence = "He is dead, he made a suicide."
found_word = tree.search_for_banned_words(sentence)
print(f"Sentence 2 first banned word: {found_word}")

sentence = "I killed him, he is dead."
found_word = tree.search_for_banned_words(sentence)
print(f"Sentence 3 first banned word: {found_word}")
```
## Result
```
Sentence 1 first banned word: kill
Sentence 2 first banned word: dead
Sentence 3 first banned word: kill
```

## Structure Of The Dictionary Tree
```
Added word, "lol"

Resulting Tree:

word:
Is it a banned word: False
dictionary: {
	'l': 
		word: l
		Is it a banned word: False
		dictionary: {
			'o': 
				word: lo
				Is it a banned word: False
				dictionary: {
					'l': 
						word: lol
						Is it a banned word: True
						dictionary: {}
							}
					}
			}
```