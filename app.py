#rodar no cmd
#pip install Flask

#importar biblioteca Flask
from flask import Flask
#Cria uma instancia de aplicação Flask
app = Flask(__name__)
#este é um decorador que associa a URL
# '/' (a URL é do site) á função que vem logo abaixo
@app.route('/')
#a função que é executada quando a rota '/' é acessada 
#ela retorna a string "hello world"
def hello_world():
     return 'Hello, world!'

#executa o servidor de desenvolvimento
if__name__ == '__main__':
    app.run(debug=True)
