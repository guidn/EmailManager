from imap_tools import MailBox, AND
from secreto import Dados

class Start:
    user = Dados.user()
    senha = Dados.senha()
    
    meu_email = MailBox('imap.gmail.com').login(user, senha)



Start()