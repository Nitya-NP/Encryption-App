""" Encryption App """

class Encryption:
    #Symbol Ciper mapping 
    symbolKey={
        'a':'@','b':'#','c':'$','d':'%','e':'&','f':'*','g':'!','h':'?',
        'i':'^','j':'~','k':'<','l':'>','m':'/','n':'+','o':'=','p':'-',
        'q':';','r':':','s':'|','t':'`','u':'_','v':'[','w':']','x':'{',
        'y':'}','z':'('}
    
    reverseSymbolKey= {v:k for k,v in symbolKey.items()}
    
    #Caesar Cipher
    def caesarEncrypt(msg,shift):
        result=""
        for i in msg:
            if i.isalpha():
                base= ord('A') if i.isupper() else ord('a')
                result+=chr((ord(i)-base+shift)%26 +base)
            else:
                result+=i
        return result
    
    def caesarDecrypt(msg,shift):
        return Encryption.caesarEncrypt(msg, -shift)
    
    
    #Symbol Cipher
    def symbolEncrypt(msg):
        return "".join(Encryption.symbolKey.get(i.lower(),i) for i in msg)
    
    def symbolDecrypt(msg):
        return "".join(Encryption.reverseSymbolKey.get(i,i) for i in msg)
    
    #Password based Cipher
    def passwordEncrypt(msg,password):
        result=""
        for i, c in enumerate(msg):
              if c.isalpha():
                  shift=ord(password[i%len(password)])%26
                  base=ord('A') if c.isupper() else ord('a')
                  result+=chr((ord(c)-base+shift) %26+base)
              else:
                  result+=c
        return result
    
    def passwordDecrypt(msg,password):
        result=""
        for i, c in enumerate(msg):
              if c.isalpha():
                  shift=ord(password[i%len(password)])%26
                  base=ord('A') if c.isupper() else ord('a')
                  result+=chr((ord(c)-base-shift) %26+base)
              else:
                  result+=c
        return result
          
