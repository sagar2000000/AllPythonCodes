ask=input("enter e to encode and d to decode")


match(ask):
  case 'e':
    message=input("enter your message")
    m=""

    if(len(message)<3):
      message="".join(reversed(message))
      print(f"encoded message is {message}")
    else:
      m=message[1:]
      m=m+message[0]
      m="abc"+m
      message=m
      print(f"encoded message is {message}")
      

  case 'd':
    message=input("enter your message")
    if(len(message)<3):
      message="".join(reversed(message))
      print(f"decoded message is {message}")  
    else:
      m=message[3:-2] 
      m=message[-1]+m
      m=m+message[-2]
      message=m
      print(f"the decoded message is {message}") 
  
  case _:
    print("enter a e or d")



