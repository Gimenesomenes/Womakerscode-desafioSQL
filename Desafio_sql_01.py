# importando sqlite3
import sqlite3

# Fazendo conexão com o BD

conexao = sqlite3.connect('dados_banco')

cursor = conexao.cursor()

# 1. Criando tabela com nome alunos contendo: id, nome, idade e curso.
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Adicionando regitros na tabela alunos
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(01, "Carolina Gimenes Oliveira", 29, "Física Médica")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(02, "Lucas Bento Chaves", 28, "Administração")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(03, "Isabela Tiezzi", 26, "Astronomia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(04, "Ana Carolina Rocha", 30, "Biblioteconomia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(05, "Luis Felipe Santos", 27, "Física Biomolecular")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(06, "Victor da Silva Junqueira", 19, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(07, "Otávio Souza Oliveira", 23, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(08, "Amanda Gardillari", 29, "Cinema")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(09, "Fernanda Fonega Liza", 19, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(10, "Gisele Araujo Souza", 24, "Jornalismo")')


# 3. Consultas Básicas:
# a) Selecionar todos os registros da tabela "alunos".

tabela = cursor.execute('SELECT * FROM alunos')

for alunos in tabela:
    print(alunos)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

tabela = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

for alunos in tabela:
    print(alunos)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética

tabela = cursor.execute('SELECT * FROM alunos WHERE curso == "Engenharia" ORDER BY nome ASC')

for alunos in tabela:
    print(alunos)

# d) Contar o número total de alunos na tabela

tabela = cursor.execute('SELECT * FROM alunos')

conta_alunos = 0

for alunos in tabela:
    conta_alunos += 1
print(f"O número total de alunos na tabela é: {conta_alunos}")

# 4. Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.

cursor.execute('UPDATE alunos SET idade=20 WHERE nome="Carolina Gimenes Oliveira"')

# Mostrando a tabela com a idade atualizada:

tabela = cursor.execute('SELECT * FROM alunos')

for alunos in tabela:
    print(alunos)

# b) Remova um aluno pelo seu ID:

cursor.execute('DELETE FROM alunos WHERE id=07')

tabela = cursor.execute('SELECT * FROM alunos')

for alunos in tabela:
    print(alunos)



# As informações vão ser enviadas
conexao.commit()

# A conexão será encerrada

conexao.close