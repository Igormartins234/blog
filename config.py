AMBIENTE = "teste"

if AMBIENTE == "teste":
#CONFIG DO BD
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if AMBIENTE == "producao":
#CONFIG DO BD
    DB_HOST = 'Igormartins.mysql.pythonanywhere-services.com'
    DB_USER = 'Igormartins'
    DB_PASSWORD = 'Senaisp@2024'
    DB_NAME = 'Igormartins$blog'


#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_PASSWORD = "Blog@adm123"
MASTER_EMAIL = "adm@adm"