# Sankofa AI API

API em **Python** para classificação de comentários usando o modelo [sankofa/sankofa-ai](https://huggingface.co/sankofa/sankofa-ai).  
A API identifica se um comentário é **racista** ou **não racista**.

---

## 🛠 Tecnologias

- **Python 3.10+**
- **FastAPI** → Framework web
- **Uvicorn** → Servidor ASGI
- **Transformers** → Biblioteca Hugging Face
- **PyTorch** → Backend para inferência do modelo

---

## ⚡ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sankofa-ai-api.git
cd sankofa-ai-api 
```

2. Crie um ambiente virtual e ative:
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
# ou
venv\Scripts\activate    
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
``
Se não houver requirements.txt, instale manualmente:
```bash
pip install fastapi uvicorn transformers torch
```
🚀 Rodando a API

Execute(na raiz):
```bash
uvicorn app:app --reload
```
A API estará disponível em: http://127.0.0.1:8000

📝 Endpoints
POST /classify

Classifica um comentário como racista ou não racista.

Request Body:
```json
{
  "text": "Seu comentário aqui"
}
```
Response:
```json
{
  "label": "Racista",
  "score": 0.95
}
```
label: "Racista" ou "Não racista"

score: probabilidade da classificação

💻 Exemplo de uso com Node.js / TypeScript

```ts
import axios from "axios";

async function classifyText(text: string) {
  const res = await axios.post("http://127.0.0.1:8000/classify", { text });
  console.log(res.data);
}

classifyText("comentário teste");
```

⚠️ Observações

A primeira execução baixa o modelo do Hugging Face, pode demorar alguns segundos.

Funciona offline após o download do modelo.

Recomendado para uso local ou apps desktop (Electron/Tauri).

📌 Referências

Hugging Face - sankofa/sankofa-ai
