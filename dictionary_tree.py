from typing import List, Optional

class DictTreeNode:
    """
    Dictionary tree node.
    """

    def __init__(self):
        self._is_word = False
        self._dictionary = {}
        self.word = ""

    def __repr__(self):
        return (
            f"\nword: {self.word}"
            f"\nIs it a banned word: {self._is_word}"
            f"\ndictionary: {self._dictionary}"
        )

    def _add_child_node(self, char) -> "DictTreeNode":
        """
        Add a new child node with key char.

        :param char:
        :return: Child node
        """
        child_node = DictTreeNode()
        child_node.word = self.word + char
        self._dictionary[char] = child_node
        return child_node

    def get_child_node(self, char) -> "DictTreeNode":
        """
        Get the child node.

        :param char:
        :return:
        """
        if char in self._dictionary:
            return self._dictionary[char]
        else:
            sub_dictionary = self._add_child_node(char)
            return sub_dictionary

    def search_child_node(self, char) -> Optional["DictTreeNode"]:
        """
        Search the child node.

        :param char:
        :return: Return None if not found.
        """
        if char in self._dictionary:
            return self._dictionary[char]
        else:
            return None

    def is_this_a_word(self) -> bool:
        return self._is_word

    def mark_as_a_word(self) -> bool:
        """
        Marks this node as a word.

        :return: False if already is marked before.
        """
        if self.is_this_a_word():
            return False
        else:
            self._is_word = True
            return True


class DictionaryTree:
    """
    Dictionary tree that stores banned words efficiently.
    """

    def __init__(self):
        self.dictionary = DictTreeNode()

    def add_words(self, words: List[str]) -> List[bool]:
        """
        Add words to the dictionary
        :param words:
        :return: List[bool],
            True if the corresponding word is added
            False if it existed before
        """
        # Future Possible improvement
        # 1- Sort words alphabetically
        # 2- Follow similarity from the start index, decrease the search time in the dictionary tree

        # Primitive word addition
        response = []
        for word in words:
            return_value = self.add_word(word)
            response.append(return_value)
        return response

    def add_word(self, word: str) -> bool:
        """
        Adds a single word.

        :param word:
        :return: False if the word is added previously, ow True
        """
        word_length = len(word)
        if word_length == 0:
            return False

        word = word.lower()
        current_dict = self.dictionary

        for index, char in enumerate(word):
            current_dict = current_dict.get_child_node(char)

        return current_dict.mark_as_a_word()

    def _search_for_a_word(self, string: str) -> Optional[str]:
        """
        Returns the first found word which is a substring of the given string.

        Substrings are left positioned, their first index are same as the string's first index.

        :param string:
        :return: Found substring if found, ow None
        """
        word_length = len(string)
        if word_length == 0:
            return None

        string = string.lower()
        current_dict = self.dictionary

        for index, char in enumerate(string):
            current_dict = current_dict.get_child_node(char)
            if current_dict is None:
                return None
            elif current_dict.is_this_a_word():
                return current_dict.word

        return None

    def search_for_banned_words(self, sentence: str) -> Optional[str]:
        """
        Returns the first found word from the DictionaryTree

        :param sentence:
        :return:
        """
        sentence_length = len(sentence)
        if sentence_length == 0:
            return None

        sentence = sentence.lower()
        # Remove spaces from the string
        sentence = sentence.replace(" ", "")

        for index in range(sentence_length):
            sub_string = sentence[index:]
            found_word = self._search_for_a_word(sub_string)
            if found_word is not None:
                return found_word

        return None


if __name__ == "__main__":
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
