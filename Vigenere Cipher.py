import math

message = input("Введите сообщение: ").lower()
key = input("Введите ключ: ")

def encrypt(key, msg):
  def ecryptIndexChar(char, startIndexChar, endIndexChar, step=0):
    charCrypt = ord(char) + step
    if charCrypt >= endIndexChar: 
      charCrypt = startIndexChar + (charCrypt - endIndexChar)
    return charCrypt
  

  def getSteps(key, lenghtMsg):
    key = (key*math.ceil(lenghtMsg/len(key)))[:lenghtMsg]
    step = list()
    for i in key:
      if ord(i) in range(1072, 1104):
        step.append(ecryptIndexChar(i, 1072, 1104)-1071)
      elif ord(i) in range(97, 123):
        step.append(ecryptIndexChar(i, 97, 123)-96)
    return step


  steps = getSteps(key, len(msg))
  cryptMsg = list()
  
  for i, step in zip(msg, steps):
    if ord(i) in range(1072, 1104):
      cryptMsg.append(chr(ecryptIndexChar(i, 1072, 1104, step)))
    elif ord(i) in range(97, 123):
      cryptMsg.append(chr(ecryptIndexChar(i, 97, 123, step)))
    else:
      cryptMsg.append(i)
  return ''.join(cryptMsg)


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
      if ord(i) in range(1072, 1104):
        step.append(ecryptIndexChar(i, 1072, 1104)-1071)
      elif ord(i) in range(97, 123):
        step.append(ecryptIndexChar(i, 97, 123)-96)
    return step
  

  steps = getSteps(key, len(msg))
  decryptMsg = list()
  
  for i, step in zip(msg, steps):
    if ord(i) in range(1072, 1104):
      decryptMsg.append(chr(decryptIndexChar(i, 1072, 1104, step)))
    elif ord(i) in range(97, 123):
      decryptMsg.append(chr(decryptIndexChar(i, 97, 123, step)))
    else:
      decryptMsg.append(i)
  return ''.join(decryptMsg)

  
crp = encrypt(key, message)
print("Закодированно: ", crp)
print("Раскодированно: ", decrypt(key, crp))
