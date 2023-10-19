# Crie um programa que verifique se os delimitadores de uma expressão matemática estão corretamente dispostos.

def verifica_delimitadores(expressao):
    stack = Stack()
    delimitadores_abertos = "([{"
    delimitadores_fechados = ")]}"

    for char in expressao:
        if char in delimitadores_abertos:
            stack.push(char)
        elif char in delimitadores_fechados:
            if stack.isEmpty():
                return False
            topo = stack.pop()
            if not delimitadores_compativeis(topo, char):
                return False

    return stack.isEmpty()

def delimitadores_compativeis(op, end):
    return (op == "(" and end == ")") or \
           (op == "[" and end == "]") or \
           (op == "{" and end == "}")

# Exemplo de uso
expressao1 = "({[1 + 2] * 3})"
expressao2 = "({[1 + 2] * 3)}"

#print(verifica_delimitadores(expressao1))  # Deve retornar True
#print(verifica_delimitadores(expressao2))  # Deve retornar False