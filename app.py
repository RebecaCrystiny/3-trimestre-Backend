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
     return render_template ('index.html')

@app.route ('/login', methods=['GET', 'POST'])
def login():
     error=None
     if request.method == 'POST':
          username = request.form ['username']
          password = request.form ['password']
          if username == 'admin' and password == 'password':
               return 'Login com sucesso' 
          else:
               error = 'Credenciais invalidas. Tente novamente.'
     return render_template('login.html', error=error)

if __name__ == '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port, debug=True)