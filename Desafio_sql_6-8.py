import sqlite3

# Fazendo conexão com o BD

conexao = sqlite3.connect('dados_clientes')

cursor = conexao.cursor()

# 5. Criando tabela com nome clientes contendo: id (PRIMARY KEY), nome, idade e saldo.

cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

# Criando registros na tabela clientes

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(01, "Carolina Gimenes Oliveira", 29, 1999.99)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(02, "Lucas Bento Chaves", 28, 3000.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(03, "Isabela Tiezzi", 26, 3948.09)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(04, "Ana Carolina Rocha", 30, 1500.94)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(05, "Luis Felipe Santos", 35, 1000.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(06, "Victor da Silva Junqueira", 40, 998.32)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(07, "Otávio Souza Oliveira", 23, 375.67)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(08, "Amanda Gardillari", 29, 587.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(09, "Fernanda Fonega Liza", 62, 2500.45)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(10, "Gisele Araujo Souza", 24, 7834.98)')

# 6. Consulta e Funções Agregadas

# a) Seleciona o nome e a idade dos clientes com idade superior a 30 anos.

tabela = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

for clientes in tabela:
    print(clientes)

# b. Calcule o saldo médio dos clientes

tabela = cursor.execute('SELECT saldo FROM clientes')

soma = 0
contador = 0

for clientes in tabela:
    soma += clientes[0]
    contador += 1

saldo_medio = soma / contador

print(f"O saldo médio dos clientes é: {saldo_medio}")


# c. Encontre o clientes com o saldo máximo.

# Podemos ordenar do maior para o menor e pegar somente o primeiro id
tabela = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')

for cliente in tabela:
    print(f"O cliente com o maior saldo (máximo) é: {cliente}")

# d. Conte quantos clientes têm saldo acima de 1000.

tabela = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')

# Retornando apenas as linhas
resultado = tabela.fetchone()

print(f"O número de clientes com saldo acima de R$ 1000 é {resultado[0]}")


# 7. Atualização e Remoção com Condições

# a) Atualize o saldo de um cliente específico

cursor.execute('UPDATE clientes SET saldo=2000.00 WHERE nome="Carolina Gimenes Oliveira"')

# Mostrando a tabela com a idade atualizada:

tabela = cursor.execute('SELECT * FROM clientes')

for clientes in tabela:
    print(clientes)

# b) Remova um cliente pelo seu ID:

cursor.execute('DELETE FROM clientes WHERE id=07')

tabela = cursor.execute('SELECT * FROM clientes')

for alunos in tabela:
    print(alunos)

# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra.

cursor.execute('CREATE TABLE compras( id INTEGER PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 1, 'Notebook', 3800.99)")
cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 2, 'Camiseta', 89.90)")
cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 3, 'Sapato', 150.00)")

tabela = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes JOIN compras ON clientes.id = compras.cliente_id')

for clientes in tabela:

    print(clientes)


# As informações vão ser enviadas
conexao.commit()

# A conexão será encerrada

conexao.close