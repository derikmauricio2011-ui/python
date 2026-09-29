# Exemplos de Conjuntos (sets) em Python

# 1. Criando conjuntos
frutas = {"maçã", "banana", "laranja"}
outras_frutas = {"banana", "uva", "laranja"}

print("Frutas:", frutas)

# 2. União: elementos dos dois conjuntos
uniao = frutas | outras_frutas
print("União:", uniao)

# 3. Intersecção: elementos que aparecem nos dois conjuntos
interseccao = frutas & outras_frutas
print("Intersecção:", interseccao)

# 4. Diferença: elementos que estão no primeiro conjunto,
# mas não estão no segundo
diferenca = frutas - outras_frutas
print("Diferença:", diferenca)

# 5. Diferença simétrica: elementos que estão em apenas um dos conjuntos
diferenca_simetrica = frutas ^ outras_frutas
print("Diferença simétrica:", diferenca_simetrica)

# 6. Adicionando um elemento
frutas.add("manga")
print("Depois de adicionar manga:", frutas)

# 7. Removendo um elemento
frutas.remove("manga")
print("Depois de remover manga:", frutas)

# 8. Verificando se um elemento pertence ao conjunto
print("banana" in frutas)  # True
print("uva" in frutas)     # False
