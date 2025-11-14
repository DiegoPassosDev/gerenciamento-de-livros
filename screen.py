import datetime
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from views import *

# Paleta de cores
cor0 = "#2e2d2b"  # Preto
cor1 = "#feffff"  # Branco
cor2 = "#4fa882"  # Verde
cor3 = "#38576b"  # Azul escuro
cor4 = "#403d3d"  # Cinza escuro
cor5 = "#e06636"  # Laranja
cor6 = "#cf6c38"  # Laranja escuro
cor7 = "#3fbfb9"  # Ciano
cor8 = "#263238"  # Cinza muito escuro
cor9 = "#e9edf5"  # Cinza claro
cor10 = "#6e8faf"  # Azul claro
cor11 = "#c2c5c2"  # Cinza médio

# Criar janela
janela = Tk()
janela.title("FluixIT Solutions")
janela.geometry("900x450")
janela.configure(bg=cor9)
janela.resizable(width=FALSE, height=FALSE)

# Centralizar janela na tela
window_width = 900
window_height = 450
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
janela.geometry(f"{window_width}x{window_height}+{x}+{y}")

style = Style(janela)
style.theme_use("clam")

frameUp = Frame(janela, width=900, height=50, bg=cor6, relief="flat")
frameUp.grid(row=0, column=0, columnspan=2, sticky=NSEW)
frameUp.grid_propagate(False)

frameLeft = Frame(janela, width=200, height=400, bg=cor4, relief="solid")
frameLeft.grid(row=1, column=0, sticky=NSEW)
frameLeft.grid_propagate(False)

frameRight = Frame(janela, width=750, height=400, bg=cor9, relief="raised")
frameRight.grid(row=1, column=1, sticky=NSEW)
frameRight.grid_propagate(False)

app_img = Image.open("img/livro.png")
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(
    frameUp,
    image=app_img,
    width=1000,
    compound=LEFT,
    padx=5,
    anchor=NW,
    fg=cor1,
    bg=cor6,
)
app_logo.place(x=5, y=0)

app_title = Label(
    frameUp,
    text="Sistema de Gerenciamento de Livros",
    compound=LEFT,
    padx=5,
    anchor=NW,
    font=("Ivy 16 bold"),
    bg=cor6,
    fg=cor1,
)
app_title.place(x=50, y=10)

app_line = Label(
    frameUp,
    width=900,
    height=1,
    padx=5,
    anchor=NW,
    font=("Verdana 1"),
    bg=cor3,
    fg=cor1,
)
app_line.place(x=0, y=47)


# Funções dos usuários
def new_user():
    global img_save

    def save_user():
        name = input_name.get().upper()
        surname = input_surname.get().upper()
        address = input_address.get().upper()
        email = input_email.get().lower()
        phone = input_phone.get()

        list_user = [name, surname, address, email, phone]
        for i in list_user:
            if i == "":
                messagebox.showerror("Atenção", "Por favor, preencha todos os campos.")
                return
        create_user(name, surname, address, email, phone)
        input_name.delete(0, END)
        input_surname.delete(0, END)
        input_address.delete(0, END)
        input_email.delete(0, END)
        input_phone.delete(0, END)
        messagebox.showinfo("Sucesso", "Usuário salvo com sucesso!")
        # Fazer o cursos voltar para o campo nome
        input_name.focus()

    title_new_user = Label(
        frameRight,
        text="Cadastro de Novo Usuário",
        width=50,
        compound=LEFT,
        padx=5,
        pady=10,
        font=("Ivy 12 bold"),
        bg=cor9,
        fg=cor4,
        anchor=CENTER,
    )
    title_new_user.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_line = Label(
        frameRight, width=750, height=1, anchor=NW, font=("Verdana 1"), bg=cor3, fg=cor1
    )
    app_line.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    lbl_name = Label(
        frameRight,
        text="Nome:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_name.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

    input_name = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_name.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_surname = Label(
        frameRight,
        text="Sobrenome:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_surname.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)

    input_surname = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_surname.grid(row=3, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_address = Label(
        frameRight,
        text="Endereço:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_address.grid(row=4, column=0, sticky=NSEW, padx=5, pady=5)

    input_address = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_address.grid(row=4, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_email = Label(
        frameRight,
        text="Email:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_email.grid(row=5, column=0, sticky=NSEW, padx=5, pady=5)

    input_email = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_email.grid(row=5, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_phone = Label(
        frameRight,
        text="Telefone:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_phone.grid(row=6, column=0, sticky=NSEW, padx=5, pady=5)
    input_phone = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_phone.grid(row=6, column=1, sticky=NSEW, padx=5, pady=5)

    def format_phone(event):
        # Pega o conteúdo atual
        content = input_phone.get()
        # Remove tudo que não é número
        numbers = "".join(filter(str.isdigit, content))
        # Limita a 11 dígitos
        numbers = numbers[:11]

        # Aplica a máscara
        formatted = ""
        if len(numbers) > 0:
            formatted = "("
            formatted += numbers[:2]
            if len(numbers) >= 2:
                formatted += ")"
            if len(numbers) > 2:
                formatted += numbers[2:3]
            if len(numbers) > 3:
                formatted += " "
                formatted += numbers[3:7]
            if len(numbers) > 7:
                formatted += "-"
                formatted += numbers[7:11]

        # Atualiza o campo
        input_phone.delete(0, END)
        input_phone.insert(0, formatted)

    input_phone.bind("<KeyRelease>", format_phone)

    img_save = Image.open("img/save.png")
    img_save = img_save.resize((18, 18))
    img_save = ImageTk.PhotoImage(img_save)
    btn_save_user = Button(
        frameRight,
        command=save_user,
        image=img_save,
        compound=LEFT,
        width=100,
        anchor=CENTER,
        text=" Salvar Usuário",
        bg=cor11,
        fg=cor4,
        font=("Ivy 11 bold"),
        overrelief=RIDGE,
        relief=GROOVE,
    )
    btn_save_user.grid(row=7, column=1, sticky=NSEW, pady=10, padx=5)


def list_users():
    def edit_user():
        try:
            selected_item = tree.selection()[0]
            values = tree.item(selected_item, "values")

            # Criar janela de edição
            edit_window = Toplevel()
            edit_window.title("Editar Usuário")
            edit_window.geometry("400x350")
            edit_window.configure(bg=cor9)
            edit_window.resizable(width=FALSE, height=FALSE)
            edit_window.grab_set()

            # Centralizar janela de edição
            edit_window.update_idletasks()
            edit_width = 400
            edit_height = 350
            screen_width = edit_window.winfo_screenwidth()
            screen_height = edit_window.winfo_screenheight()
            x = (screen_width // 2) - (edit_width // 2)
            y = (screen_height // 2) - (edit_height // 2)
            edit_window.geometry(f"{edit_width}x{edit_height}+{x}+{y}")

            title_edit = Label(
                edit_window,
                text="Editar Usuário",
                font=("Ivy 14 bold"),
                bg=cor9,
                fg=cor4,
            )
            title_edit.grid(row=0, column=0, columnspan=2, pady=10)

            # Campo ID (somente leitura)
            lbl_id = Label(edit_window, text="ID:", font=("Ivy 12"), bg=cor9, fg=cor4)
            lbl_id.grid(row=1, column=0, sticky=W, padx=20, pady=5)
            input_id = Entry(
                edit_window,
                width=25,
                font=("Ivy 12"),
                bg=cor11,
                fg=cor4,
                relief=SOLID,
                state="readonly",
            )
            input_id.grid(row=1, column=1, sticky=W, padx=10, pady=5)
            input_id.config(state="normal")
            input_id.insert(0, values[0])
            input_id.config(state="readonly")

            # Campo Nome
            lbl_name = Label(
                edit_window, text="Nome:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_name.grid(row=2, column=0, sticky=W, padx=20, pady=5)
            input_name = Entry(
                edit_window, width=25, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_name.grid(row=2, column=1, sticky=W, padx=10, pady=5)
            input_name.insert(0, values[1])

            # Campo Sobrenome
            lbl_surname = Label(
                edit_window, text="Sobrenome:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_surname.grid(row=3, column=0, sticky=W, padx=20, pady=5)
            input_surname = Entry(
                edit_window, width=25, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_surname.grid(row=3, column=1, sticky=W, padx=10, pady=5)
            input_surname.insert(0, values[2])

            # Campo Endereço
            lbl_address = Label(
                edit_window, text="Endereço:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_address.grid(row=4, column=0, sticky=W, padx=20, pady=5)
            input_address = Entry(
                edit_window, width=25, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_address.grid(row=4, column=1, sticky=W, padx=10, pady=5)
            input_address.insert(0, values[3])

            # Campo Email
            lbl_email = Label(
                edit_window, text="Email:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_email.grid(row=5, column=0, sticky=W, padx=20, pady=5)
            input_email = Entry(
                edit_window, width=25, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_email.grid(row=5, column=1, sticky=W, padx=10, pady=5)
            input_email.insert(0, values[4])

            # Campo Telefone
            lbl_phone = Label(
                edit_window, text="Telefone:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_phone.grid(row=6, column=0, sticky=W, padx=20, pady=5)
            input_phone = Entry(
                edit_window, width=25, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_phone.grid(row=6, column=1, sticky=W, padx=10, pady=5)
            input_phone.insert(0, values[5])

            def format_phone_edit(event):
                content = input_phone.get()
                numbers = "".join(filter(str.isdigit, content))
                numbers = numbers[:11]

                formatted = ""
                if len(numbers) > 0:
                    formatted = "("
                    formatted += numbers[:2]
                    if len(numbers) >= 2:
                        formatted += ")"
                    if len(numbers) > 2:
                        formatted += numbers[2:3]
                    if len(numbers) > 3:
                        formatted += " "
                        formatted += numbers[3:7]
                    if len(numbers) > 7:
                        formatted += "-"
                        formatted += numbers[7:11]

                input_phone.delete(0, END)
                input_phone.insert(0, formatted)

            input_phone.bind("<KeyRelease>", format_phone_edit)

            def save_changes():
                user_id = input_id.get()
                name = input_name.get().upper()
                surname = input_surname.get().upper()
                address = input_address.get().upper()
                email = input_email.get().lower()
                phone = input_phone.get()

                if not all([name, surname, address, email, phone]):
                    messagebox.showerror(
                        "Atenção", "Por favor, preencha todos os campos."
                    )
                    return

                update_user(user_id, name, surname, address, email, phone)
                messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
                edit_window.destroy()
                # Recarregar a lista
                control_menu("list_users")

            # Botões
            btn_save = Button(
                edit_window,
                command=save_changes,
                text="Salvar Alterações",
                bg=cor2,
                fg=cor1,
                font=("Ivy 11 bold"),
                overrelief=RIDGE,
                relief=GROOVE,
            )
            btn_save.grid(row=7, column=0, pady=20, padx=10)

            btn_cancel = Button(
                edit_window,
                command=edit_window.destroy,
                text="Cancelar",
                bg=cor5,
                fg=cor1,
                font=("Ivy 11 bold"),
                overrelief=RIDGE,
                relief=GROOVE,
            )
            btn_cancel.grid(row=7, column=1, pady=20, padx=10)

        except IndexError:
            messagebox.showwarning(
                "Atenção", "Por favor, selecione um usuário para editar."
            )

    title_list_user = Label(
        frameRight,
        text="Lista de Usuários",
        width=50,
        compound=LEFT,
        padx=5,
        pady=10,
        font=("Ivy 12 bold"),
        bg=cor9,
        fg=cor4,
    )
    title_list_user.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_line = Label(
        frameRight, width=750, height=1, anchor=NW, font=("Verdana 1"), bg=cor3, fg=cor1
    )
    app_line.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    list_users = read_users()

    # Criando a tabela para visualizar os usuários
    list_header = ["ID", "Nome", "Sobrenome", "Endereço", "Email", "Telefone"]
    global tree
    tree = Treeview(
        frameRight,
        selectmode="extended",
        columns=list_header,
        show="headings",
        height=13,
    )

    vsb = Scrollbar(frameRight, orient="vertical", command=tree.yview)
    hsb = Scrollbar(frameRight, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=2, column=0, sticky=NSEW)
    vsb.grid(row=2, column=1, sticky=NS)
    hsb.grid(row=3, column=0, sticky=EW)

    hd = ["center", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 90, 140, 160, 180, 90, 0]
    n = 0
    for col in list_header:
        tree.heading(col, text=col, anchor=NW)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1
    for item in list_users:
        tree.insert("", "end", values=item)

    # Botão para editar usuário
    global img_edit
    img_edit = Image.open("img/update.png")
    img_edit = img_edit.resize((18, 18))
    img_edit = ImageTk.PhotoImage(img_edit)
    btn_edit = Button(
        frameRight,
        command=edit_user,
        image=img_edit,
        compound=LEFT,
        width=120,
        anchor=CENTER,
        text=" Editar Usuário",
        bg=cor11,
        fg=cor4,
        font=("Ivy 11"),
        overrelief=RIDGE,
        relief=GROOVE,
    )
    btn_edit.grid(row=4, column=0, sticky=W, pady=10, padx=5)


# Funções dos livros
def list_books():
    def edit_book():
        try:
            selected_item = tree.selection()[0]
            values = tree.item(selected_item, "values")

            # Criar janela de edição
            edit_window = Toplevel()
            edit_window.title("Editar Livro")
            edit_window.geometry("600x450")
            edit_window.configure(bg=cor9)
            edit_window.resizable(width=FALSE, height=FALSE)
            edit_window.grab_set()

            # Centralizar janela de edição
            edit_window.update_idletasks()
            edit_width = 600
            edit_height = 450
            screen_width = edit_window.winfo_screenwidth()
            screen_height = edit_window.winfo_screenheight()
            x = (screen_width // 2) - (edit_width // 2)
            y = (screen_height // 2) - (edit_height // 2)
            edit_window.geometry(f"{edit_width}x{edit_height}+{x}+{y}")

            # Configurar grid para centralizar
            edit_window.grid_rowconfigure(0, weight=1)
            edit_window.grid_rowconfigure(1, weight=0)
            edit_window.grid_rowconfigure(2, weight=0)
            edit_window.grid_rowconfigure(3, weight=0)
            edit_window.grid_rowconfigure(4, weight=0)
            edit_window.grid_rowconfigure(5, weight=0)
            edit_window.grid_rowconfigure(6, weight=0)
            edit_window.grid_rowconfigure(7, weight=0)
            edit_window.grid_rowconfigure(8, weight=1)
            edit_window.grid_columnconfigure(0, weight=1)
            edit_window.grid_columnconfigure(1, weight=1)

            title_edit = Label(
                edit_window,
                text="Editar Livro",
                font=("Ivy 16 bold"),
                bg=cor9,
                fg=cor4,
            )
            title_edit.grid(row=0, column=0, columnspan=2, pady=20)

            # Campo ID (somente leitura)
            lbl_id = Label(edit_window, text="ID:", font=("Ivy 12"), bg=cor9, fg=cor4)
            lbl_id.grid(row=1, column=0, sticky=E, padx=20, pady=10)
            input_id = Entry(
                edit_window,
                width=45,
                font=("Ivy 12"),
                bg=cor11,
                fg=cor4,
                relief=SOLID,
                state="readonly",
            )
            input_id.grid(row=1, column=1, sticky=W, padx=20, pady=10)
            input_id.config(state="normal")
            input_id.insert(0, values[0])
            input_id.config(state="readonly")

            # Campo Título
            lbl_title = Label(
                edit_window, text="Título:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_title.grid(row=2, column=0, sticky=E, padx=20, pady=10)
            input_title = Entry(
                edit_window, width=45, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_title.grid(row=2, column=1, sticky=W, padx=20, pady=10)
            input_title.insert(0, values[1])

            # Campo Autor
            lbl_author = Label(
                edit_window, text="Autor:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_author.grid(row=3, column=0, sticky=E, padx=20, pady=10)
            input_author = Entry(
                edit_window, width=45, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_author.grid(row=3, column=1, sticky=W, padx=20, pady=10)
            input_author.insert(0, values[2])

            # Campo Editora
            lbl_publisher = Label(
                edit_window, text="Editora:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_publisher.grid(row=4, column=0, sticky=E, padx=20, pady=10)
            input_publisher = Entry(
                edit_window, width=45, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_publisher.grid(row=4, column=1, sticky=W, padx=20, pady=10)
            input_publisher.insert(0, values[3])

            # Campo Ano Publicação
            lbl_year = Label(
                edit_window, text="Ano Publicação:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_year.grid(row=5, column=0, sticky=E, padx=20, pady=10)
            input_year = Entry(
                edit_window, width=45, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_year.grid(row=5, column=1, sticky=W, padx=20, pady=10)
            input_year.insert(0, values[4])

            # Campo ISBN
            lbl_isbn = Label(
                edit_window, text="ISBN:", font=("Ivy 12"), bg=cor9, fg=cor4
            )
            lbl_isbn.grid(row=6, column=0, sticky=E, padx=20, pady=10)
            input_isbn = Entry(
                edit_window, width=45, font=("Ivy 12"), bg=cor9, fg=cor4, relief=SOLID
            )
            input_isbn.grid(row=6, column=1, sticky=W, padx=20, pady=10)
            input_isbn.insert(0, values[5])

            def save_changes():
                book_id = input_id.get()
                title = input_title.get().upper()
                author = input_author.get().upper()
                publisher = input_publisher.get().upper()
                year = input_year.get()
                isbn = input_isbn.get()

                if not all([title, author, publisher, year, isbn]):
                    messagebox.showerror(
                        "Atenção", "Por favor, preencha todos os campos."
                    )
                    return

                update_book(book_id, title, author, publisher, year, isbn)
                messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
                edit_window.destroy()
                # Recarregar a lista
                control_menu("list_books")

            # Frame para os botões centralizados
            frame_buttons = Frame(edit_window, bg=cor9)
            frame_buttons.grid(row=7, column=0, columnspan=2, pady=30)

            # Botões
            btn_save = Button(
                frame_buttons,
                command=save_changes,
                text="Salvar Alterações",
                width=18,
                bg=cor2,
                fg=cor1,
                font=("Ivy 11 bold"),
                overrelief=RIDGE,
                relief=GROOVE,
            )
            btn_save.grid(row=0, column=0, padx=10)

            btn_cancel = Button(
                frame_buttons,
                command=edit_window.destroy,
                text="Cancelar",
                width=18,
                bg=cor5,
                fg=cor1,
                font=("Ivy 11 bold"),
                overrelief=RIDGE,
                relief=GROOVE,
            )
            btn_cancel.grid(row=0, column=1, padx=10)

        except IndexError:
            messagebox.showwarning(
                "Atenção", "Por favor, selecione um livro para editar."
            )

    title_list_books = Label(
        frameRight,
        text="Lista de Livros",
        width=50,
        compound=LEFT,
        padx=5,
        pady=10,
        font=("Ivy 12 bold"),
        bg=cor9,
        fg=cor4,
    )
    title_list_books.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_line = Label(
        frameRight, width=750, height=1, anchor=NW, font=("Verdana 1"), bg=cor3, fg=cor1
    )
    app_line.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    list_books = read_books()

    # Criando a tabela para visualizar os livros

    # Criando a tabela para visualizar os usuários
    list_header = ["ID", "Titulo", "Autor", "Editora", "Ano Publicação", "ISBN"]
    global tree
    tree = Treeview(
        frameRight,
        selectmode="extended",
        columns=list_header,
        show="headings",
        height=13,
    )

    vsb = Scrollbar(frameRight, orient="vertical", command=tree.yview)
    hsb = Scrollbar(frameRight, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=2, column=0, sticky=NSEW)
    vsb.grid(row=2, column=1, sticky=NS)
    hsb.grid(row=3, column=0, sticky=EW)

    hd = ["nw", "nw", "nw", "nw", "center", "nw"]
    h = [20, 220, 120, 130, 95, 90, 10]
    n = 0
    for col in list_header:
        tree.heading(col, text=col, anchor=NW)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1
    for item in list_books:
        tree.insert("", "end", values=item)

    # Botão para editar livro
    global img_edit_book
    img_edit_book = Image.open("img/update.png")
    img_edit_book = img_edit_book.resize((20, 20))
    img_edit_book = ImageTk.PhotoImage(img_edit_book)
    btn_edit_book = Button(
        frameRight,
        command=edit_book,
        image=img_edit_book,
        compound=LEFT,
        width=120,
        anchor=CENTER,
        text=" Editar Livro",
        bg=cor11,
        fg=cor4,
        font=("Ivy 11"),
        overrelief=RIDGE,
        relief=GROOVE,
    )
    btn_edit_book.grid(row=4, column=0, sticky=W, pady=10, padx=5)


def new_book():
    global img_save

    def save_book():
        title = input_title.get().upper()
        author = input_author.get().upper()
        publisher = input_publisher.get().upper()
        publication_year = input_publication_year.get()
        isbn = input_isbn.get()

        list_user = [title, author, publisher, publication_year, isbn]
        for i in list_user:
            if i == "":
                messagebox.showerror("Atenção", "Por favor, preencha todos os campos.")
                return
        create_book(title, author, publisher, publication_year, isbn)
        input_title.delete(0, END)
        input_author.delete(0, END)
        input_publisher.delete(0, END)
        input_publication_year.delete(0, END)
        input_isbn.delete(0, END)
        messagebox.showinfo("Sucesso", "Livro salvo com sucesso!")
        # Fazer o cursos voltar para o campo título
        input_title.focus()

    title_new_book = Label(
        frameRight,
        text="Cadastro de Novo Livro",
        width=50,
        compound=LEFT,
        padx=5,
        pady=10,
        font=("Ivy 12 bold"),
        bg=cor9,
        fg=cor4,
    )
    title_new_book.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_line = Label(
        frameRight, width=750, height=1, anchor=NW, font=("Verdana 1"), bg=cor3, fg=cor1
    )
    app_line.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    lbl_title = Label(
        frameRight,
        text="Título:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_title.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

    input_title = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_title.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_author = Label(
        frameRight,
        text="Autor:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_author.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)

    input_author = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_author.grid(row=3, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_publisher = Label(
        frameRight,
        text="Editora:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_publisher.grid(row=4, column=0, sticky=NSEW, padx=5, pady=5)

    input_publisher = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_publisher.grid(row=4, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_publication_year = Label(
        frameRight,
        text="Ano da Publicação:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_publication_year.grid(row=5, column=0, sticky=NSEW, padx=5, pady=5)

    input_publication_year = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_publication_year.grid(row=5, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_isbn = Label(
        frameRight,
        text="ISBN:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_isbn.grid(row=6, column=0, sticky=NSEW, padx=5, pady=5)
    input_isbn = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_isbn.grid(row=6, column=1, sticky=NSEW, padx=5, pady=5)

    img_save = Image.open("img/save.png")
    img_save = img_save.resize((18, 18))
    img_save = ImageTk.PhotoImage(img_save)
    btn_save_book = Button(
        frameRight,
        command=save_book,
        image=img_save,
        compound=LEFT,
        width=100,
        anchor=CENTER,
        text=" Salvar Livro",
        bg=cor11,
        fg=cor4,
        font=("Ivy 11 bold"),
        overrelief=RIDGE,
        relief=GROOVE,
    )
    btn_save_book.grid(row=7, column=1, sticky=NSEW, pady=10, padx=5)


# Funções dos Empréstimos
def new_loan():
    global img_save

    def save_loan():
        id_book = input_id_book.get()
        id_user = input_id_user.get()
        date_now = datetime.datetime.now().date()

        list_user = [id_user, id_book]
        for i in list_user:
            if i == "":
                messagebox.showerror("Atenção", "Por favor, preencha todos os campos.")
                return

        # Validar se o usuário existe
        if not check_user_exists(id_user):
            messagebox.showerror(
                "Erro", f"Usuário com ID {id_user} não existe no banco de dados!"
            )
            input_id_user.delete(0, END)
            input_id_user.focus()
            return

        # Validar se o livro existe
        if not check_book_exists(id_book):
            messagebox.showerror(
                "Erro", f"Livro com ID {id_book} não existe no banco de dados!"
            )
            input_id_book.delete(0, END)
            input_id_book.focus()
            return

        create_loan(id_book, id_user, date_now, None)
        input_id_user.delete(0, END)
        input_id_book.delete(0, END)
        messagebox.showinfo("Sucesso", "Empréstimo salvo com sucesso!")
        # Fazer o cursor voltar para o campo id_user
        input_id_user.focus()

    title_new_book = Label(
        frameRight,
        text="Cadastro de Novo Empréstimo",
        width=50,
        compound=LEFT,
        padx=5,
        pady=10,
        font=("Ivy 12 bold"),
        bg=cor9,
        fg=cor4,
    )
    title_new_book.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_line = Label(
        frameRight, width=750, height=1, anchor=NW, font=("Verdana 1"), bg=cor3, fg=cor1
    )
    app_line.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    lbl_id_user = Label(
        frameRight,
        text="ID do Usuário:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_id_user.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

    input_id_user = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_id_user.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

    lbl_id_book = Label(
        frameRight,
        text="ID do Livro:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_id_book.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)

    input_id_book = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_id_book.grid(row=3, column=1, sticky=NSEW, padx=5, pady=5)

    img_save = Image.open("img/save.png")
    img_save = img_save.resize((18, 18))
    img_save = ImageTk.PhotoImage(img_save)
    btn_save_book = Button(
        frameRight,
        command=save_loan,
        image=img_save,
        compound=LEFT,
        width=100,
        anchor=CENTER,
        text=" Salvar Empréstimo",
        bg=cor11,
        fg=cor4,
        font=("Ivy 11"),
        overrelief=RIDGE,
        relief=GROOVE,
    )
    btn_save_book.grid(row=7, column=1, sticky=NSEW, pady=10, padx=5)


def return_loan():
    global img_save

    def save_loan_return():
        id_loan = input_id_loan.get()
        date_now = datetime.datetime.now().date()

        list_loan = [id_loan]
        for i in list_loan:
            if i == "":
                messagebox.showerror("Atenção", "Por favor, preencha todos os campos.")
                return

        # Validar se o usuário existe
        if not check_loan_exists(id_loan):
            messagebox.showerror(
                "Erro", f"Empréstimo com ID {id_loan} não existe no banco de dados!"
            )
            input_id_loan.delete(0, END)
            input_id_loan.focus()
            return
        # Gerar uma messagebox de confirmação antes de salvar a devolução
        if not messagebox.askyesno(
            "Confirmação", "Tem certeza que deseja salvar a devolução?"
        ):
            return

        update_loan_return(id_loan, date_now)
        input_id_loan.delete(0, END)
        messagebox.showinfo("Sucesso", "Devolução salva com sucesso!")
        # Fazer o cursor voltar para o campo id_user
        input_id_loan.focus()

    title_new_book = Label(
        frameRight,
        text="Devolução do Empréstimo",
        width=50,
        compound=LEFT,
        padx=5,
        pady=10,
        font=("Ivy 12 bold"),
        bg=cor9,
        fg=cor4,
    )
    title_new_book.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_line = Label(
        frameRight, width=750, height=1, anchor=NW, font=("Verdana 1"), bg=cor3, fg=cor1
    )
    app_line.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    lbl_id_loan = Label(
        frameRight,
        text="ID do Empréstimo:",
        anchor=NW,
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
    )
    lbl_id_loan.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

    input_id_loan = Entry(
        frameRight,
        width=25,
        justify="left",
        font=("Ivy 12"),
        bg=cor9,
        fg=cor4,
        relief=SOLID,
    )
    input_id_loan.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

    img_save = Image.open("img/save.png")
    img_save = img_save.resize((18, 18))
    img_save = ImageTk.PhotoImage(img_save)
    btn_save_book = Button(
        frameRight,
        command=save_loan_return,
        image=img_save,
        compound=LEFT,
        width=100,
        anchor=CENTER,
        text=" Salvar Devolução",
        bg=cor11,
        fg=cor4,
        font=("Ivy 11"),
        overrelief=RIDGE,
        relief=GROOVE,
    )
    btn_save_book.grid(row=7, column=1, sticky=NSEW, pady=10, padx=5)


def list_loans():
    title_list_loan = Label(
        frameRight,
        text="Lista de Empréstimos",
        width=50,
        compound=LEFT,
        padx=5,
        pady=10,
        font=("Ivy 12 bold"),
        bg=cor9,
        fg=cor4,
    )
    title_list_loan.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_line = Label(
        frameRight, width=700, height=1, anchor=NW, font=("Verdana 1"), bg=cor3, fg=cor1
    )
    app_line.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    datas = []
    books_loans = read_loans()

    for book in books_loans:
        data = [f"{book[0]}", f"{book[1]}", f"{book[2]}", f"{book[3]}", f"{book[4]}"]
        datas.append(data)
    # Criando a tabela para visualizar os empréstimos
    list_header = ["ID", "Livro", "Usuário", "Data Empréstimo", "Data Devolução"]
    global tree
    tree = Treeview(
        frameRight,
        selectmode="extended",
        columns=list_header,
        show="headings",
        height=14,
    )

    vsb = Scrollbar(frameRight, orient="vertical", command=tree.yview)
    hsb = Scrollbar(frameRight, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=2, column=0, sticky=NSEW)
    vsb.grid(row=2, column=1, sticky=NS)
    hsb.grid(row=3, column=0, sticky=EW)

    hd = ["center", "nw", "nw", "center", "center"]
    h = [15, 280, 200, 100, 100]
    n = 0
    for col in list_header:
        tree.heading(col, text=col, anchor=NW)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1
    for item in datas:
        tree.insert("", "end", values=item)


# Função para controle do Menu
def control_menu(option):
    if option == "new_user":
        for widget in frameRight.winfo_children():
            widget.destroy()
        new_user()
    elif option == "new_book":
        for widget in frameRight.winfo_children():
            widget.destroy()
        new_book()
    elif option == "list_books":
        for widget in frameRight.winfo_children():
            widget.destroy()
        list_books()
    elif option == "list_users":
        for widget in frameRight.winfo_children():
            widget.destroy()
        list_users()
    elif option == "new_loan":
        for widget in frameRight.winfo_children():
            widget.destroy()
        new_loan()
    elif option == "return_loan":
        for widget in frameRight.winfo_children():
            widget.destroy()
        return_loan()
    elif option == "list_loans":
        for widget in frameRight.winfo_children():
            widget.destroy()
        list_loans()
    else:
        messagebox.showerror("Atenção", "Opção inválida.")


# Gerando os botões do menu
# Configurar grid do frameLeft para distribuir espaço igualmente
frameLeft.grid_rowconfigure(0, weight=1)
frameLeft.grid_rowconfigure(1, weight=1)
frameLeft.grid_rowconfigure(2, weight=1)
frameLeft.grid_rowconfigure(3, weight=1)
frameLeft.grid_rowconfigure(4, weight=1)
frameLeft.grid_rowconfigure(5, weight=1)
frameLeft.grid_rowconfigure(6, weight=1)
frameLeft.grid_columnconfigure(0, weight=1)

img_new_user = Image.open("img/novo-usuario.png")
img_new_user = img_new_user.resize((20, 20))
img_new_user = ImageTk.PhotoImage(img_new_user)
btn_new_user = Button(
    frameLeft,
    command=lambda: control_menu("new_user"),
    image=img_new_user,
    compound=LEFT,
    anchor=CENTER,
    text="Novo Usuário",
    bg=cor4,
    fg=cor1,
    font=("Ivy 11 bold "),
    overrelief=RIDGE,
    relief=GROOVE,
    padx=15,
)
btn_new_user.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)

img_new_book = Image.open("img/new-book.png")
img_new_book = img_new_book.resize((20, 20))
img_new_book = ImageTk.PhotoImage(img_new_book)
btn_new_book = Button(
    frameLeft,
    command=lambda: control_menu("new_book"),
    image=img_new_book,
    compound=LEFT,
    anchor=CENTER,
    text="Novo Livro",
    bg=cor4,
    fg=cor1,
    font=("Ivy 11 bold"),
    overrelief=RIDGE,
    relief=GROOVE,
    padx=15,
)
btn_new_book.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

img_list_books = Image.open("img/list-book.png")
img_list_books = img_list_books.resize((20, 20))
img_list_books = ImageTk.PhotoImage(img_list_books)
btn_list_books = Button(
    frameLeft,
    command=lambda: control_menu("list_books"),
    image=img_list_books,
    compound=LEFT,
    anchor=CENTER,
    text="Listar Livros",
    bg=cor4,
    fg=cor1,
    font=("Ivy 11 bold"),
    overrelief=RIDGE,
    relief=GROOVE,
    padx=15,
)
btn_list_books.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

img_list_users = Image.open("img/list-user.png")
img_list_users = img_list_users.resize((20, 20))
img_list_users = ImageTk.PhotoImage(img_list_users)
btn_list_users = Button(
    frameLeft,
    command=lambda: control_menu("list_users"),
    image=img_list_users,
    compound=LEFT,
    anchor=CENTER,
    text="Listar Usuários",
    bg=cor4,
    fg=cor1,
    font=("Ivy 11 bold"),
    overrelief=RIDGE,
    relief=GROOVE,
    padx=15,
)
btn_list_users.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)

img_new_loan = Image.open("img/new-loan.png")
img_new_loan = img_new_loan.resize((20, 20))
img_new_loan = ImageTk.PhotoImage(img_new_loan)
btn_new_loan = Button(
    frameLeft,
    command=lambda: control_menu("new_loan"),
    image=img_new_loan,
    compound=LEFT,
    anchor=CENTER,
    text="Novo Empréstimo",
    bg=cor4,
    fg=cor1,
    font=("Ivy 11 bold"),
    overrelief=RIDGE,
    relief=GROOVE,
    padx=15,
)
btn_new_loan.grid(row=4, column=0, sticky=NSEW, padx=5, pady=5)

img_return_loan = Image.open("img/return-loan.png")
img_return_loan = img_return_loan.resize((20, 20))
img_return_loan = ImageTk.PhotoImage(img_return_loan)
btn_return_loan = Button(
    frameLeft,
    command=lambda: control_menu("return_loan"),
    image=img_return_loan,
    compound=LEFT,
    anchor=CENTER,
    text="Devolver Empréstimo",
    bg=cor4,
    fg=cor1,
    font=("Ivy 11 bold"),
    overrelief=RIDGE,
    relief=GROOVE,
)
btn_return_loan.grid(row=5, column=0, sticky=NSEW, padx=5, pady=5)

img_list_loans = Image.open("img/list-loan.png")
img_list_loans = img_list_loans.resize((20, 20))
img_list_loans = ImageTk.PhotoImage(img_list_loans)
btn_list_loans = Button(
    frameLeft,
    command=lambda: control_menu("list_loans"),
    image=img_list_loans,
    compound=LEFT,
    anchor=CENTER,
    text="Listar Empréstimos",
    bg=cor4,
    fg=cor1,
    font=("Ivy 11 bold"),
    overrelief=RIDGE,
    relief=GROOVE,
    padx=8,
)
btn_list_loans.grid(row=6, column=0, sticky=NSEW, padx=5, pady=5)

janela.mainloop()
