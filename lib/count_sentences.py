#!/usr/bin/env python3

class MyString:

  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, string_value):
    if type(string_value) == str:
      self._value = string_value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    value = self.value

    for punctuation in ["!", "?"]:
      value = value.replace(punctuation, ".")
    
    sentences = [sentence for sentence in value.split(".") if sentence]

    return len(sentences)

