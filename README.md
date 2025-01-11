# Produtos

- Programa para gerenciar produtos.

- Para usar, execute os comandos abaixo no terminal, no diretório onde se encontra o arquivo `manage.py`:

- **Ativação do Ambiente Virtual:**

    - **Windows:**
        ```
        python -m venv venv
        venv\Scripts\activate
        ```

    - **Linux / macOS:**
        ```
        python3 -m venv venv
        source venv/bin/activate
        ```

- **Instalação das Bibliotecas:**

```
pip install -r requirements.txt
```

- **Base de Dados (padrão: SQLite):**

 ```
 python manage.py makemigrations
 python manage.py migrate
 ```