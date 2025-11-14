# 📚 Sistema de Gerenciamento de Livros

Sistema desktop desenvolvido em Python com interface gráfica moderna para gerenciamento completo de biblioteca, permitindo o controle de livros, usuários e empréstimos com validações e máscaras de entrada.

## ✨ Principais Destaques

- Interface gráfica moderna e intuitiva (900x450 pixels)
- Janelas centralizadas automaticamente na tela
- Máscara de telefone com validação em tempo real: `(XX)9 XXXX-XXXX`
- Sistema completo de edição de usuários e livros
- Tabelas expansíveis com rolagem vertical e horizontal
- Validação de integridade referencial no banco de dados

## 🚀 Funcionalidades

### **Gerenciamento de Livros**
- ✅ Cadastro de novos livros com todos os dados bibliográficos
- ✅ Listagem completa com tabela de 15 linhas visíveis
- ✅ Edição em janela modal (600x450) com campos ampliados
- ✅ Conversão automática para maiúsculas
- ✅ Campos: Título, Autor, Editora, Ano de Publicação, ISBN
- ✅ Recarregamento automático da lista após edições

### **Gerenciamento de Usuários**
- ✅ Cadastro de novos usuários com dados completos
- ✅ Máscara de telefone automática `(XX)9 XXXX-XXXX`
- ✅ Listagem com tabela expansível
- ✅ Edição em janela modal centralizada
- ✅ Validação de campos obrigatórios
- ✅ Campos: Nome, Sobrenome, Endereço, Email, Telefone
- ✅ Email convertido automaticamente para minúsculas
- ✅ Nome e sobrenome convertidos para maiúsculas

### **Gerenciamento de Empréstimos**
- ✅ Registro de empréstimos com validação de IDs
- ✅ Validação automática de existência de livros e usuários
- ✅ Data de empréstimo registrada automaticamente
- ✅ Sistema de devolução com confirmação
- ✅ Listagem completa mostrando:
  - ID do empréstimo
  - Título do livro
  - Nome completo do usuário
  - Data do empréstimo
  - Data da devolução (ou em branco se ativo)

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **Tkinter** - Interface gráfica nativa
- **SQLite3** - Banco de dados relacional
- **PIL (Pillow)** - Manipulação e exibição de imagens/ícones
- **Grid Layout** - Sistema de layout responsivo

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
pip install -r requirements.txt
```

Ou manualmente:
```bash
pip install Pillow==10.1.0
```

3. Crie o banco de dados (primeira execução):
```bash
python database.py
```

4. Execute o sistema:
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
gerenciamento_de_livros/
│
├── main.py              # Ponto de entrada (executa screen.py)
├── screen.py            # Interface gráfica principal e lógica de apresentação
├── views.py             # Funções CRUD (Create, Read, Update, Delete)
├── database.py          # Script de criação das tabelas do banco
├── database.db          # Arquivo do banco de dados SQLite
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
├── LICENSE              # Licença do projeto
├── CONTRIBUTING.md      # Guia de contribuição
│
└── img/                 # Pasta com imagens/ícones do sistema
    ├── livro.png        # Logo principal
    ├── novo-usuario.png # Ícone novo usuário
    ├── new-book.png     # Ícone novo livro
    ├── list-book.png    # Ícone listar livros
    ├── list-user.png    # Ícone listar usuários
    ├── new-loan.png     # Ícone novo empréstimo
    ├── return-loan.png  # Ícone devolver empréstimo
    ├── list-loan.png    # Ícone listar empréstimos
    ├── save.png         # Ícone salvar
    └── update.png       # Ícone editar
```


## 🗄️ Estrutura do Banco de Dados

### Tabela: livros
| Campo           | Tipo    | Descrição                    |
|-----------------|---------|------------------------------|
| id              | INTEGER | Chave primária (autoincremento) |
| titulo          | TEXT    | Título do livro (armazenado em MAIÚSCULAS) |
| autor           | TEXT    | Autor do livro (armazenado em MAIÚSCULAS) |
| editora         | TEXT    | Editora (armazenado em MAIÚSCULAS) |
| ano_publicacao  | INTEGER | Ano de publicação            |
| isbn            | TEXT    | Código ISBN único            |

### Tabela: usuarios
| Campo      | Tipo    | Descrição                    |
|------------|---------|------------------------------|
| id         | INTEGER | Chave primária (autoincremento) |
| nome       | TEXT    | Nome do usuário (armazenado em MAIÚSCULAS) |
| sobrenome  | TEXT    | Sobrenome (armazenado em MAIÚSCULAS) |
| endereco   | TEXT    | Endereço completo (armazenado em MAIÚSCULAS) |
| email      | TEXT    | Email (armazenado em minúsculas) |
| telefone   | TEXT    | Telefone formato `(XX)9 XXXX-XXXX` |

### Tabela: emprestimos
| Campo            | Tipo    | Descrição                         |
|------------------|---------|-----------------------------------|
| id               | INTEGER | Chave primária (autoincremento)   |
| livro_id         | INTEGER | FK - Referência ao livro          |
| usuario_id       | INTEGER | FK - Referência ao usuário        |
| data_emprestimo  | TEXT    | Data do empréstimo (YYYY-MM-DD)   |
| data_devolucao   | TEXT    | Data da devolução (NULL se ativo) |

**Relacionamentos:**
- `emprestimos.livro_id` → `livros.id`
- `emprestimos.usuario_id` → `usuarios.id`

## 🎯 Como Usar

### Cadastrar um Novo Livro
1. Clique no botão **"Novo Livro"** no menu lateral esquerdo
2. Preencha todos os campos obrigatórios:
   - **Título**: Nome do livro
   - **Autor**: Nome do autor
   - **Editora**: Nome da editora
   - **Ano de Publicação**: Ano em formato numérico
   - **ISBN**: Código ISBN do livro
3. Clique em **"Salvar Livro"**
4. O cursor retorna automaticamente ao campo Título para novo cadastro

### Cadastrar um Novo Usuário
1. Clique no botão **"Novo Usuário"** no menu lateral
2. Preencha todos os campos:
   - **Nome**: Primeiro nome
   - **Sobrenome**: Sobrenome do usuário
   - **Endereço**: Endereço completo
   - **Email**: Email válido
   - **Telefone**: Digite apenas números, a máscara é aplicada automaticamente
3. Clique em **"Salvar Usuário"**
4. O cursor retorna ao campo Nome

> 💡 **Dica**: No campo telefone, digite apenas os números (ex: 79999999999) e a máscara `(79)9 9999-9999` será aplicada automaticamente!

### Editar um Usuário
1. Clique em **"Listar Usuários"**
2. Clique em um usuário na tabela para selecioná-lo
3. Clique no botão **"Editar Usuário"** abaixo da tabela
4. Uma janela modal será aberta com todos os dados
5. Edite os campos desejados (ID não pode ser alterado)
6. Clique em **"Salvar Alterações"** ou **"Cancelar"**
7. A lista será recarregada automaticamente

### Editar um Livro
1. Clique em **"Listar Livros"**
2. Clique em um livro na tabela para selecioná-lo
3. Clique no botão **"Editar Livro"** abaixo da tabela
4. Uma janela maior (600x450) será aberta com campos ampliados
5. Edite os dados necessários
6. Clique em **"Salvar Alterações"** ou **"Cancelar"**

### Registrar um Empréstimo
1. Clique no botão **"Novo Empréstimo"**
2. Informe o **ID do Usuário** (consulte em "Listar Usuários")
3. Informe o **ID do Livro** (consulte em "Listar Livros")
4. Clique em **"Salvar Empréstimo"**
5. A data atual será registrada automaticamente

> ⚠️ **Importante**: O sistema valida se os IDs existem. Se não existirem, uma mensagem de erro será exibida e o cursor retornará ao campo incorreto.

### Devolver um Empréstimo
1. Clique em **"Devolver Empréstimo"**
2. Informe o **ID do Empréstimo** (consulte em "Listar Empréstimos")
3. Clique em **"Salvar Devolução"**
4. Confirme a operação na janela de confirmação
5. A data de devolução será registrada automaticamente

### Visualizar Listas
- **Listar Livros**: Tabela com ID, Título, Autor, Editora, Ano e ISBN
- **Listar Usuários**: Tabela com ID, Nome, Sobrenome, Endereço, Email e Telefone
- **Listar Empréstimos**: Tabela com ID, Livro, Usuário, Data Empréstimo e Data Devolução

Todas as tabelas possuem:
- Scrollbar vertical e horizontal
- 15 linhas visíveis por padrão
- Colunas redimensionáveis
- Seleção de itens para edição

## 🔒 Validações Implementadas

### Validações de Entrada
- ✅ Verificação de campos obrigatórios (não permite campos vazios)
- ✅ Máscara de telefone aceita apenas números
- ✅ Conversão automática de email para minúsculas
- ✅ Conversão automática de nomes para maiúsculas
- ✅ Limite de 11 dígitos no telefone

### Validações de Banco de Dados
- ✅ Verificação de existência de ID de livro antes de criar empréstimo
- ✅ Verificação de existência de ID de usuário antes de criar empréstimo
- ✅ Verificação de existência de ID de empréstimo antes de registrar devolução
- ✅ Relacionamentos com FOREIGN KEY
- ✅ Consultas com INNER JOIN para garantir integridade

### Validações de Interface
- ✅ Mensagens de erro claras e específicas
- ✅ Retorno automático do cursor ao campo com erro
- ✅ Confirmação antes de operações críticas (devolução)
- ✅ Bloqueio de edição do campo ID
- ✅ Janelas modais que bloqueiam interação com janela principal

## 🎨 Interface

### Layout Principal (900x450 pixels)
- **Menu Lateral Esquerdo** (150px):
  - 7 botões distribuídos uniformemente
  - Ícones + texto descritivo
  - Cores: fundo cinza escuro (#403d3d), texto branco
  
- **Área de Conteúdo** (750x400 pixels):
  - Formulários de cadastro
  - Tabelas de visualização
  - Área dinâmica que muda conforme seleção do menu

### Paleta de Cores
```python
cor0 = "#2e2d2b"  # Preto
cor1 = "#feffff"  # Branco
cor2 = "#4fa882"  # Verde (botão salvar)
cor3 = "#38576b"  # Azul escuro (linhas)
cor4 = "#403d3d"  # Cinza escuro (menu)
cor5 = "#e06636"  # Laranja (botão cancelar)
cor6 = "#cf6c38"  # Laranja escuro (header)
cor9 = "#e9edf5"  # Cinza claro (fundo)
cor11 = "#f2f4f2" # Cinza muito claro (campos readonly)
```

### Componentes Visuais
- Campos de entrada com bordas sólidas
- Botões com efeito hover (overrelief=RIDGE)
- Scrollbars automáticas nas tabelas
- Janelas centralizadas na tela
- Fonte padrão: Ivy (11-16pt)

## 📊 Script de Teste (test.py)

O arquivo `test.py` popula o banco com dados de exemplo:

**20 Usuários incluindo:**
- João Silva, Maria Santos, Pedro Oliveira, Ana Costa, etc.
- Endereços fictícios em diferentes cidades
- Emails únicos
- Telefones com diferentes DDDs

**30 Livros incluindo:**
- Clássicos brasileiros: Dom Casmurro, Macunaíma, Vidas Secas, etc.
- Clássicos internacionais: 1984, O Pequeno Príncipe, Harry Potter, etc.
- Autores: Machado de Assis, Jorge Amado, George Orwell, J.K. Rowling, etc.
- ISBNs válidos e anos de publicação reais

Execute com:
```bash
python test.py
```

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'PIL'"
**Solução:**
```bash
pip install Pillow==10.1.0
```

### Erro: "no such table: livros"
**Solução:** Execute o script de criação do banco:
```bash
python database.py
```

### Banco de dados fica travado
**Solução:** Feche todas as instâncias do programa e verifique se não há conexões abertas.

### Empréstimos não aparecem na lista
**Possíveis causas:**
- IDs de livros ou usuários não existem
- Empréstimos criados com IDs inválidos antes das validações
- Execute `test.py` para popular com dados válidos

### Janelas aparecem em posição errada
**Solução:** O sistema calcula automaticamente a posição central. Certifique-se que está executando em um monitor com resolução mínima de 1024x768.

### Máscara de telefone não funciona
**Causa:** O evento KeyRelease está vinculado corretamente. Se não funcionar:
- Verifique se está digitando no campo correto
- Digite apenas números (0-9)
- A máscara aceita apenas 11 dígitos

## 📈 Melhorias Futuras

- [ ] Sistema de busca e filtros nas tabelas
- [ ] Exportação de relatórios em PDF
- [ ] Gráficos de estatísticas (livros mais emprestados, etc.)
- [ ] Sistema de multas por atraso
- [ ] Backup automático do banco de dados
- [ ] Modo escuro/claro
- [ ] Impressão de comprovantes de empréstimo
- [ ] Campo de observações nos empréstimos
- [ ] Histórico de alterações
- [ ] Sistema de reservas
- [ ] Categorização de livros por gênero

## 👨‍💻 Autor

Desenvolvido por **FluixIT Solutions**

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaNovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade X'`)
4. Push para a branch (`git push origin feature/MinhaNovaFuncionalidade`)
5. Abra um Pull Request

Leia o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes sobre nosso código de conduta e processo de contribuição.

## 📞 Suporte

- 🐛 Para reportar bugs, abra uma [issue](https://github.com/seu-usuario/gerenciamento_de_livros/issues)
- 💡 Para sugerir melhorias, abra uma [issue](https://github.com/seu-usuario/gerenciamento_de_livros/issues) com a tag `enhancement`
- 📧 Para contato direto: seu-email@example.com

## 🙏 Agradecimentos

- Biblioteca Tkinter pela interface gráfica nativa
- Pillow pela manipulação de imagens
- SQLite pela simplicidade e eficiência do banco de dados
- Comunidade Python pelo suporte

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no repositório!**

📚 **Desenvolvido com ❤️ para facilitar o gerenciamento de bibliotecas**
