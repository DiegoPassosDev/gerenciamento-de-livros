# 📚 Sistema de Gerenciamento de Livros

Sistema desktop desenvolvido em Python para gerenciamento de biblioteca, permitindo o controle de livros, usuários e empréstimos.

## 🚀 Funcionalidades

- **Gerenciamento de Livros**
  - Cadastro de novos livros
  - Listagem de todos os livros cadastrados
  - Edição de informações dos livros
  - Exclusão de livros

- **Gerenciamento de Usuários**
  - Cadastro de novos usuários
  - Listagem de todos os usuários
  - Informações completas (nome, sobrenome, endereço, email, telefone)

- **Gerenciamento de Empréstimos**
  - Registro de novos empréstimos
  - Validação de IDs de livros e usuários
  - Listagem de todos os empréstimos (ativos e devolvidos)
  - Controle de datas de empréstimo e devolução
  - Visualização com ID do empréstimo

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter** - Interface gráfica
- **SQLite3** - Banco de dados
- **PIL (Pillow)** - Manipulação de imagens

## 📋 Pré-requisitos

```bash
Python 3.x instalado
pip (gerenciador de pacotes Python)
```

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/gerenciamento_de_livros.git
cd gerenciamento_de_livros
```

2. Instale as dependências:
```bash
pip install pillow
```

3. Execute o sistema:
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
gerenciamento_de_livros/
│
├── main.py              # Arquivo principal para executar o sistema
├── screen.py            # Interface gráfica e lógica de apresentação
├── views.py             # Funções de acesso ao banco de dados (CRUD)
├── database.py          # Criação das tabelas do banco de dados
├── database.db          # Arquivo do banco de dados SQLite
├── check_db.py          # Scripts de verificação do banco
├── verify_db.py         # Scripts auxiliares de verificação
│
└── img/                 # Pasta com imagens/ícones do sistema
    ├── livro.png
    ├── novo-usuario.png
    ├── new-book.png
    ├── list-book.png
    ├── list-user.png
    ├── new-loan.png
    ├── return-loan.png
    ├── list-loan.png
    └── save.png
```

## 🗄️ Estrutura do Banco de Dados

### Tabela: livros
| Campo           | Tipo    | Descrição                    |
|-----------------|---------|------------------------------|
| id              | INTEGER | Chave primária (auto)        |
| titulo          | TEXT    | Título do livro              |
| autor           | TEXT    | Autor do livro               |
| editora         | TEXT    | Editora                      |
| ano_publicacao  | INTEGER | Ano de publicação            |
| isbn            | TEXT    | Código ISBN                  |

### Tabela: usuarios
| Campo      | Tipo    | Descrição                    |
|------------|---------|------------------------------|
| id         | INTEGER | Chave primária (auto)        |
| nome       | TEXT    | Nome do usuário              |
| sobrenome  | TEXT    | Sobrenome do usuário         |
| endereco   | TEXT    | Endereço completo            |
| email      | TEXT    | Email do usuário             |
| telefone   | TEXT    | Telefone de contato          |

### Tabela: emprestimos
| Campo            | Tipo    | Descrição                         |
|------------------|---------|-----------------------------------|
| id               | INTEGER | Chave primária (auto)             |
| livro_id         | INTEGER | FK - Referência ao livro          |
| usuario_id       | INTEGER | FK - Referência ao usuário        |
| data_emprestimo  | TEXT    | Data do empréstimo                |
| data_devolucao   | TEXT    | Data da devolução (NULL se ativo) |

## 🎯 Como Usar

### Cadastrar um Novo Livro
1. Clique no botão **"Novo Livro"** no menu lateral
2. Preencha todos os campos (Título, Autor, Editora, Ano de Publicação, ISBN)
3. Clique em **"Salvar Livro"**

### Cadastrar um Novo Usuário
1. Clique no botão **"Novo Usuário"** no menu lateral
2. Preencha todos os campos (Nome, Sobrenome, Endereço, Email, Telefone)
3. Clique em **"Salvar Usuário"**

### Registrar um Empréstimo
1. Clique no botão **"Novo Empréstimo"** no menu lateral
2. Informe o **ID do Usuário** (consulte na lista de usuários)
3. Informe o **ID do Livro** (consulte na lista de livros)
4. Clique em **"Salvar Empréstimo"**

> ⚠️ **Importante**: O sistema valida automaticamente se os IDs informados existem no banco de dados. Caso um ID não exista, será exibida uma mensagem de erro e o cursor retornará ao campo correspondente.

### Visualizar Listas
- **Listar Livros**: Exibe todos os livros cadastrados
- **Listar Usuários**: Exibe todos os usuários cadastrados
- **Listar Empréstimos**: Exibe todos os empréstimos (ativos e devolvidos) com ID, título do livro, nome do usuário e datas

## 🔒 Validações Implementadas

- Verificação de campos obrigatórios (não permite campos vazios)
- Validação de existência de IDs de livros antes de criar empréstimo
- Validação de existência de IDs de usuários antes de criar empréstimo
- Relacionamentos via INNER JOIN garantindo integridade referencial

## 🎨 Interface

O sistema utiliza uma paleta de cores profissional e interface intuitiva:
- Menu lateral com ícones para fácil navegação
- Tabelas com scroll para visualização de muitos registros
- Mensagens de confirmação e erro claras
- Design responsivo e organizado

## 🐛 Solução de Problemas

### Erro ao executar: "ModuleNotFoundError: No module named 'PIL'"
Instale o Pillow:
```bash
pip install pillow
```

### Banco de dados não é criado
Execute primeiro o arquivo `database.py`:
```bash
python database.py
```

### Empréstimos não aparecem na lista
- Verifique se os IDs de livros e usuários existem no banco de dados
- O sistema usa INNER JOIN, então apenas empréstimos com livros e usuários válidos são exibidos
- Use os scripts `verify_db.py` ou `check_db.py` para verificar o conteúdo do banco

## 👨‍💻 Autor

Desenvolvido por FluixIT Solutions

## 📄 Licença

Este projeto é de código aberto e está disponível para uso educacional e comercial.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📞 Suporte

Para reportar bugs ou sugerir melhorias, abra uma [issue](https://github.com/seu-usuario/gerenciamento_de_livros/issues) no GitHub.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
