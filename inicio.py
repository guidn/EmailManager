from imap_tools import MailBox, AND
from secreto import Dados

class Start:
    user = Dados.user()
    senha = Dados.senha()
    
    meu_email = MailBox('imap.gmail.com').login(user, senha)

    #LISTA_EMAIL
    lista_uber = []

    lista_email_uber = meu_email.fetch(AND(from_='uber'))

    print('\nLista de emails do remetente:')
    for lista in lista_email_uber:
        lista_uber = {(f'\nEmail ID:{lista.uid}\n{lista.subject}\n{lista.text} {lista.flags} FIMSE')}
        print(lista_uber)



Start()