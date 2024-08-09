# Type Annotations:
  # Examples of Type Annotation:


def sum(num1: int| float, num2: int| float) -> int | float:   # Or just float, because float is part of Int Class, i do prefer using int | float to be more expressive.
  return num1 + num2

def text_return(text1: str = '', text2: str = '', text3: str ='') -> str:
    return ',\n'.join([text1, text2, text3])


  
# Just examples about type annotations!
