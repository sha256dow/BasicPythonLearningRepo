# [INIT]
# Do you know the Walrus Operator?
# Here is a very simple example about Walrus Operator (:=):

# It assigns values to variables as part of a larger expression:

# If you try to:
# print(happy = True) -> It will not work and raise a TypeError... BUT with Walrus Operator it can be done just like that:

print(happy := True) # And the code will sucessfully run without errors.

# ========================================================================================================================================== #
# Português (PT-BR):

# O operador Walrus (:=) foi introduzido no Python 3.8 e é conhecido oficialmente como o operador de atribuição de expressão. 
#Ele permite atribuir um valor a uma variável como parte de uma expressão maior. 
#Isso pode ser útil em situações onde você deseja usar o valor da variável imediatamente após a atribuição, evitando a necessidade de linhas de 
#código adicionais.

# ========================================================================================================================================== #
# Example (Português)

# Antes do Walrus Operator:
value = len(some_list)
if value > 5:
    print(f"A lista é grande, tem {value} elementos")

# Com o Walrus Operator:
if (value := len(some_list)) > 5:
    print(f"A lista é grande, tem {value} elementos")

# [END]

