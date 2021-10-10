# Pontos Turísticos API

- API para exposição de pontos turísticos de uma região realizada durante o curso Criando poderosas API's RESTful com Django Rest Framework (https://www.udemy.com/course/apis-restful-com-django-rest-framework/)

- Para o desenvolvimento foi utilizando: Python, Django e Django Rest Framework.

# 1. Requisitos Necessários

- Python 3.

# 2. Configurações Essenciais

## 2.1. Criando o Arquivo .env
- Na raíz do projeto crie o arquivo .env.

### 2.1.1. Preenchendo o Arquivo .env
- O arquivo .env tem como conteúdo a chave secreta (SECRET_KEY) do django e a flag DEBUG.
- Copie o código abaixo e cole no seu arquivo .env

```sh
SECRET_KEY=minha_chave_secreta
DEBUG=True
```

### 2.1.2. Gerando uma chave secreta (SECRET_KEY)
-  Abra o terminal e acesse a pasta raíz do projeto;

#### Opção 1 - Gerar a chave secreta pelo shell do Python.
- Abra o shell do python. Digite no terminal: python3 manage.py shell
- Cole o seguinte código:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
- Dica: Talvez seja necessário pressionar o enter duas vezes;
- Copie a chave secreta gerada;
- Abra o arquivo .env;
- Substitua o *minha_chave_secreta* pela chave gerada.

#### Opção 2 - Gerar pelo terminal
- Abra o terminal;
- Cole o seguinte código:
```sh
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
- Copie a chave secreta gerada;
- Abra o arquivo .env;
- Substitua o *minha_chave_secreta* pela chave gerada.


#### Opção 3 (Para Python 3.6+) - Gerar a chave secreta pelo shell do Python utilizando a biblioteca secrets.
- Abra o shell do python. Digite no terminal: python3 manage.py shell
- Cole o seguinte código:
```python
import secrets

print(secrets.token_urlsafe())
```
- Dica: Talvez seja necessário pressionar o enter duas vezes;
- Copie a chave secreta gerada;
- Abra o arquivo .env;
- Substitua o *minha_chave_secreta* pela chave gerada.

#### Opção 4 (Para Python 3.6+) - Gerar pelo terminal utilizando a biblioteca secrets do Python.
- Abra o terminal;
- Cole o seguinte código:
```sh
python3 -c "import secrets; print(secrets.token_urlsafe())"
```
- Copie a chave secreta gerada;
- Abra o arquivo .env;
- Substitua o *minha_chave_secreta* pela chave gerada.








## 2.2. Criando uma VirtualEnv (Ambientes Virtuais)
-  Abra o terminal e acesse a pasta raíz do projeto;
- Crie uma pasta chamada venv;
```sh
mkdir venv
```
- Essa pasta guardara os arquivos da VirtualEnv;
- Execute o seguinte comando para gerar a VirtualEnv:
```sh
python3 -m venv ./venv/
```

*Referências: https://docs.python.org/pt-br/3/library/venv.html*

## 2.3. Ativar a VirtualEnv 
-  Abra o terminal e acesse a pasta raíz do projeto;
- Os comandos variam de acordo com o sistema operacional;

| Plataforma | Shell | Comando para ativar o ambiente virtual |
| ------     | ------ | ------ |
| POSIX  | bash/zsh | source venv/bin/activate |
|        | fish     | source venv/bin/activate.fish |
|        | csh/tcsh     | source venv/bin/activate.csh |
|        | PowerShell Core   | venv/bin/Activate.ps1 |
| Windows | cmd.exe   | C:\> venv\Scripts\activate.bat |
|         | PowerShell   | C:\> venv\Scripts\Activate.ps1 |

Para mais informações acesse: https://docs.python.org/pt-br/3/library/venv.html

## 2.4. Instalando as dependências necessárias
- Abra o terminal e acesse a pasta raíz do projeto;
- Execute o comando:
```sh
pip install -r requirements.txt
```

## 2.5. Rodando as migrations
- Abra o terminal e pasta raíz do projeto;
- Execute o seguinte comando:
```sh
python3 manage.py migrate
```

## 2.6. Criando um superuser para acessar a área administrativa do Django.
- Abra o terminal e acesse a pasta raíz do projeto;
- Digite o seguinte comando: 
```sh
python3 manage.py createsuperuser
```
- Informe um username (nome de usuário);
- Informe um email (opcional);
- Informe uma senha;
- O superuser será gerado e você utilizar as credenciais para acessar a área administrativa do django;


# 3. Subindo a aplicação
- Abra o terminal e acesse a pasta raíz do projeto;
- Execute o comando:
```sh
python3 manage.py runserver
```
- A aplicação rodará na port 8000;
- http:/localhost:8000/

# 3.1. Acessando a rota administrativa
- Após subir a aplicação acesse o seguinte endereço: http:/localhost:8000/admin
- Utilize o nome de usuário (username) e senha definidos na etapa 2.6 para realizar login.
