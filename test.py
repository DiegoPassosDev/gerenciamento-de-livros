import datetime
from views import *
import sqlite3

# Adicionar 20 usuários
print("Adicionando 20 usuários...")
usuarios = [
    ("JOÃO", "SILVA", "RUA DAS FLORES, 123", "joao.silva@email.com", "(11)9 8765-4321"),
    ("MARIA", "SANTOS", "AV PAULISTA, 456", "maria.santos@email.com", "(21)9 7654-3210"),
    ("PEDRO", "OLIVEIRA", "RUA AUGUSTA, 789", "pedro.oliveira@email.com", "(31)9 6543-2109"),
    ("ANA", "COSTA", "RUA DA CONSOLAÇÃO, 321", "ana.costa@email.com", "(41)9 5432-1098"),
    ("CARLOS", "PEREIRA", "AV BRASIL, 654", "carlos.pereira@email.com", "(51)9 4321-0987"),
    ("JULIANA", "FERREIRA", "RUA SÃO JOÃO, 987", "juliana.ferreira@email.com", "(61)9 3210-9876"),
    ("RICARDO", "ALMEIDA", "AV IPIRANGA, 147", "ricardo.almeida@email.com", "(71)9 2109-8765"),
    ("FERNANDA", "RODRIGUES", "RUA VERGUEIRO, 258", "fernanda.rodrigues@email.com", "(81)9 1098-7654"),
    ("LUCAS", "MARTINS", "AV REBOUÇAS, 369", "lucas.martins@email.com", "(85)9 0987-6543"),
    ("CAMILA", "SOUZA", "RUA OSCAR FREIRE, 741", "camila.souza@email.com", "(11)9 9876-5432"),
    ("BRUNO", "LIMA", "AV FARIA LIMA, 852", "bruno.lima@email.com", "(21)9 8765-4321"),
    ("PATRICIA", "BARBOSA", "RUA HADDOCK LOBO, 963", "patricia.barbosa@email.com", "(31)9 7654-3210"),
    ("RAFAEL", "CARDOSO", "AV NOVE DE JULHO, 159", "rafael.cardoso@email.com", "(41)9 6543-2109"),
    ("AMANDA", "GOMES", "RUA PAMPLONA, 357", "amanda.gomes@email.com", "(51)9 5432-1098"),
    ("GUSTAVO", "RIBEIRO", "AV BRIGADEIRO, 468", "gustavo.ribeiro@email.com", "(61)9 4321-0987"),
    ("LARISSA", "CARVALHO", "RUA Augusta, 579", "larissa.carvalho@email.com", "(71)9 3210-9876"),
    ("THIAGO", "TEIXEIRA", "AV IBIRAPUERA, 681", "thiago.teixeira@email.com", "(81)9 2109-8765"),
    ("VANESSA", "ARAUJO", "RUA JARDINS, 792", "vanessa.araujo@email.com", "(85)9 1098-7654"),
    ("DIEGO", "MOREIRA", "AV MORUMBI, 813", "diego.moreira@email.com", "(11)9 0987-6543"),
    ("GABRIELA", "NASCIMENTO", "RUA PINHEIROS, 924", "gabriela.nascimento@email.com", "(21)9 9876-5432")
]

for usuario in usuarios:
    create_user(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4])

print("20 usuários adicionados com sucesso!")

# Adicionar 30 livros
print("\nAdicionando 30 livros...")
livros = [
    ("DOM CASMURRO", "MACHADO DE ASSIS", "EDITORA GLOBO", "1899", "978-8525406262"),
    ("1984", "GEORGE ORWELL", "COMPANHIA DAS LETRAS", "1949", "978-8535914849"),
    ("O PEQUENO PRÍNCIPE", "ANTOINE DE SAINT-EXUPÉRY", "AGIR", "1943", "978-8522008703"),
    ("HARRY POTTER E A PEDRA FILOSOFAL", "J.K. ROWLING", "ROCCO", "1997", "978-8532530787"),
    ("O SENHOR DOS ANÉIS", "J.R.R. TOLKIEN", "MARTINS FONTES", "1954", "978-8533613379"),
    ("A REVOLUÇÃO DOS BICHOS", "GEORGE ORWELL", "COMPANHIA DAS LETRAS", "1945", "978-8535909555"),
    ("O CORTIÇO", "ALUÍSIO AZEVEDO", "ÁTICA", "1890", "978-8508040063"),
    ("MEMÓRIAS PÓSTUMAS DE BRÁS CUBAS", "MACHADO DE ASSIS", "PENGUIN", "1881", "978-8563560148"),
    ("VIDAS SECAS", "GRACILIANO RAMOS", "RECORD", "1938", "978-8501012371"),
    ("GRANDE SERTÃO VEREDAS", "GUIMARÃES ROSA", "NOVA FRONTEIRA", "1956", "978-8520923634"),
    ("CAPITÃES DA AREIA", "JORGE AMADO", "COMPANHIA DAS LETRAS", "1937", "978-8535908640"),
    ("O ALQUIMISTA", "PAULO COELHO", "ROCCO", "1988", "978-8532511010"),
    ("A MORENINHA", "JOAQUIM MANUEL DE MACEDO", "MARTIN CLARET", "1844", "978-8572327282"),
    ("IRACEMA", "JOSÉ DE ALENCAR", "MARTIN CLARET", "1865", "978-8572327169"),
    ("SENHORA", "JOSÉ DE ALENCAR", "ÁTICA", "1875", "978-8508040124"),
    ("O GUARANI", "JOSÉ DE ALENCAR", "ÁTICA", "1857", "978-8508040117"),
    ("QUINCAS BORBA", "MACHADO DE ASSIS", "PENGUIN", "1891", "978-8563560209"),
    ("A HORA DA ESTRELA", "CLARICE LISPECTOR", "ROCCO", "1977", "978-8532511256"),
    ("A PAIXÃO SEGUNDO G.H.", "CLARICE LISPECTOR", "ROCCO", "1964", "978-8532530790"),
    ("MACUNAÍMA", "MÁRIO DE ANDRADE", "AGIR", "1928", "978-8522008896"),
    ("SÃO BERNARDO", "GRACILIANO RAMOS", "RECORD", "1934", "978-8501012555"),
    ("MEMÓRIAS DE UM SARGENTO DE MILÍCIAS", "MANUEL ANTÔNIO DE ALMEIDA", "ÁTICA", "1854", "978-8508040148"),
    ("O ATENEU", "RAUL POMPEIA", "ÁTICA", "1888", "978-8508040131"),
    ("TRISTE FIM DE POLICARPO QUARESMA", "LIMA BARRETO", "PENGUIN", "1915", "978-8563560278"),
    ("O PRIMO BASÍLIO", "EÇA DE QUEIRÓS", "MARTIN CLARET", "1878", "978-8572327954"),
    ("OS MAIAS", "EÇA DE QUEIRÓS", "MARTIN CLARET", "1888", "978-8572327947"),
    ("A RELÍQUIA", "EÇA DE QUEIRÓS", "MARTIN CLARET", "1887", "978-8572328128"),
    ("FOGO MORTO", "JOSÉ LINS DO REGO", "JOSÉ OLYMPIO", "1943", "978-8503011914"),
    ("MENINO DE ENGENHO", "JOSÉ LINS DO REGO", "JOSÉ OLYMPIO", "1932", "978-8503011907"),
    ("GABRIELA CRAVO E CANELA", "JORGE AMADO", "COMPANHIA DAS LETRAS", "1958", "978-8535928396")
]

for livro in livros:
    create_book(livro[0], livro[1], livro[2], livro[3], livro[4])

print("30 livros adicionados com sucesso!")

print("\n=== OPERAÇÃO CONCLUÍDA ===")
print(f"Total de usuários no banco: {len(read_users())}")
print(f"Total de livros no banco: {len(read_books())}")