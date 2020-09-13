import math

message = input("Введите сообщение: ").lower()
key = input("Введите ключ: ")

def encrypt(key, msg):
  """key - смещение \n msg - сообщение которое шифруется \
    Каждый символ msg должен сместиться на key шагов вправо по алфавиту"""

  def ecryptIndexChar(char, startIndexChar, endIndexChar, step=0):
    charCrypt = ord(char) + step
    if charCrypt >= endIndexChar: 
      charCrypt = startIndexChar + (charCrypt - endIndexChar)
    return charCrypt
  

  def getSteps(key, lenghtMsg):
    key = (key*math.ceil(lenghtMsg/len(key)))[:lenghtMsg]
    step = list()
    for i in key:
      if ord(i) in range(1072, 1104): # номера русского алфавита в кодировке
        step.append(ecryptIndexChar(i, 1072, 1104)-1071)
      elif ord(i) in range(97, 123): # номера английского алфавита в кодировке
        step.append(ecryptIndexChar(i, 97, 123)-96)
    return step


  steps = getSteps(key, len(msg))
  cryptMsg = list()
  
  for i, step in zip(msg, steps):
    if ord(i) in range(1072, 1104): # Проверка - Это русский алфавит
      cryptMsg.append(chr(ecryptIndexChar(i, 1072, 1104, step)))
    elif ord(i) in range(97, 123): # Проверка - Это английский алфавит
      cryptMsg.append(chr(ecryptIndexChar(i, 97, 123, step)))
    else: # Если это не алфавит, то записываем символ в таком же виде, как он и был
      cryptMsg.append(i)
  return ''.join(cryptMsg) # Это просто перевод списка в строку


def decrypt(key, msg):
  def decryptIndexChar(char, startIndexChar, endIndexChar, step=0):
    charDerypt = ord(char) - step
    if charDerypt <= startIndexChar:
      charDerypt = endIndexChar - (startIndexChar - charDerypt)
    return charDerypt


  def getSteps(key, lenghtMsg):
    def ecryptIndexChar(char, startIndexChar, endIndexChar, step=0):
      charCrypt = ord(char) + step
      if charCrypt >= endIndexChar: 
        charCrypt = startIndexChar + (charCrypt - endIndexChar)
      return charCrypt

    key = (key*math.ceil(lenghtMsg/len(key)))[:lenghtMsg]
    step = list()
    for i in key:
      if ord(i) in range(1072, 1104): # номера русского алфавита в кодировке
        step.append(ecryptIndexChar(i, 1072, 1104)-1071)
      elif ord(i) in range(97, 123): # номера английского алфавита в кодировке
        step.append(ecryptIndexChar(i, 97, 123)-96)
    return step
  

  steps = getSteps(key, len(msg))
  decryptMsg = list()
  
  for i, step in zip(msg, steps):
    if ord(i) in range(1072, 1104): # Проверка - Это русский алфавит
      decryptMsg.append(chr(decryptIndexChar(i, 1072, 1104, step)))
    elif ord(i) in range(97, 123): # Проверка - Это английский алфавит
      decryptMsg.append(chr(decryptIndexChar(i, 97, 123, step)))
    else: # Если это не алфавит, то записываем символ в таком же виде, как он и был
      decryptMsg.append(i)
  return ''.join(decryptMsg) # Это просто перевод списка в строку

  
crp = encrypt(key, message)
print("Закодированно: ", crp)
print("Раскодированно: ", decrypt(key, crp))
