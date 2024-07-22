# WhatsApp Repository

Este é um repositório online para armazenar e categorizar memes, gifs e mensagens de bom dia compartilhados no grupo de WhatsApp "Bate-papo | Estágio". O projeto foi desenvolvido para facilitar o acesso e a organização desses conteúdos, melhorando a experiência dos membros do grupo.

## Funcionalidades

- **Visualização**: Exiba todos os memes, gifs e mensagens armazenados.
- **Upload**: Faça o upload de novos memes, gifs e mensagens.
- **Organização**: Categorize e acesse facilmente o conteúdo compartilhado.

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: SQLite
- **Frontend**: HTML

## Estrutura do Projeto

```
whatsapp_repository/
│
├── app.py
├── database.py
├── models.py
├── requirements.txt
└── templates/
    ├── index.html
    └── upload.html
```

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/whatsapp_repository.git
   cd whatsapp_repository
   ```

2. **Crie um ambiente virtual e ative-o (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Crie o banco de dados:**

   ```bash
   python
   >>> from app import app
   >>> from models import db
   >>> with app.app_context():
   >>>     db.create_all()
   ```

5. **Execute a aplicação:**

   ```bash
   python app.py
   ```

6. **Acesse a aplicação:**

   Abra seu navegador e vá para `http://127.0.0.1:5000`

## Uso

- **Página Inicial**: Visualize todos os memes, gifs e mensagens.
- **Upload**: Navegue até `/upload` para adicionar novos memes, gifs e mensagens.

## Contribuições

Se você deseja contribuir para este projeto, siga estas etapas:

1. Fork o repositório.
2. Crie uma branch para suas alterações (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`).
5. Envie um pull request.
