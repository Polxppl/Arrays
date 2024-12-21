def words_num(text):
  return len(text.split(' '))

def ordered(text):
  words = text.split(' ')
  return sorted(words, key=lambda a: len(a), reverse=True)

def alphabetically(text):
  return sorted(text.split(' '))
