# daje-servicos-mvp
MVP de suporte operacional e vistorias técnicas para a DAJE Serviços — Alinhado ao ODS 8.


```markdown
# DAJE Serviços — Sistema de Vistorias e Apoio de Campo (MVP)

> **Projeto de Software — Experiência Prática**  
> Solução tecnológica para descentralização técnica, capacitação operacional e vistorias de contrapiso na instalação de pisos vinílicos.

---

## 📌 1. Visão Geral do Projeto

A **DAJE Serviços** é uma empresa prestadora de serviços na área de acabamentos da construção civil, especializada na instalação de pisos vinílicos. O negócio enfrentava um gargalo operacional crítico: a dependência exclusiva da proprietária e responsável técnica para a realização de vistorias preliminares nos canteiros de obra.

Este **Minimum Viable Product (MVP)** foi desenvolvido para capacitar e dar autonomia aos ajudantes operacionais de campo (representados pelo ajudante Carlos Eduardo Santos). A solução combina:
1. **Ferramenta de Apoio de Campo:** Calculadora automática de insumos (pisos e argamassa) e checklist digital para inspeção de patologias em contrapiso (trincas, umidade, desnível).
2. **Plataforma de Microlearning:** Módulos de capacitação técnica assíncrona para nivelamento e qualificação profissional da equipe.

---

## 🎯 2. Impacto Social e Alinhamento com o ODS 8 (ONU)

Este software está diretamente comprometido com o **Objetivo de Desenvolvimento Sustentável 8 da ONU (Trabalho Decente e Crescimento Econômico)**, atuando em duas metas estratégicas:
- **Meta 8.2 (Produtividade e Inovação):** Redução do tempo de vistoria, eliminação de retrabalhos na aplicação de pisos e aumento da eficiência operacional da microempresa.
- **Meta 8.5 (Trabalho Decente e Qualificação):** Transformação do ajudante operacional em um avaliador técnico autônomo, promovendo qualificação profissional contínua e valorização no canteiro de obras.

---

## 🏗️ 3. Arquitetura e Tecnologias

A aplicação adota uma arquitetura em camadas orientada a microserviços/APIs RESTful, priorizando execução rápida e resiliência em ambientes de obra:

- **Frontend:** HTML5 semântico, CSS3 (Mobile-First, alvos táteis de 48px, alto contraste) e JavaScript Vanilla puro (processamento do cálculo no client-side para resposta instantânea < 0,5s).
- **Backend:** Python 3.12 com **FastAPI** para alta performance assíncrona, tipagem estática e geração automática de documentação OpenAPI (Swagger).
- **Segurança e Validação:** Esquemas de validação de dados com **Pydantic**, autenticação via tokens **JWT** (JSON Web Tokens) e sanitização contra injeção de scripts (OWASP).
- **Persistência de Dados:** SQLite (desenvolvimento/testes) com suporte para migração a PostgreSQL.
- **Qualidade e CI:** Testes unitários e de integração automatizados via **Pytest**, orquestrados por esteira de **GitHub Actions**.

---

## ♿ 4. Acessibilidade e Condições de Uso em Campo (WCAG 2.1 AA)

A interface foi projetada especificamente para as condições adversas do canteiro de obras (manuseio com uma mão, iluminação solar direta e luvas/sujidade):
- **Alvos de Toque Ampliados:** Botões e chaves de seleção com dimensões mínimas de 48x48 pixels, prevenindo toques acidentais.
- **Contraste Aumentado:** Relação de contraste superior a 7:1 entre texto e fundo, garantindo legibilidade sob incidência de luz solar.
- **Feedback Multimodal:** Notificações e alertas técnicos utilizam dupla codificação (ícones descritivos + texto legível + cores funcionais), assegurando compreensão independentemente de percepção cromática.

---

## 📂 5. Estrutura do Repositório

```text
daje-servicos-mvp/
├── .github/
│   └── workflows/
│       └── ci.yml               # Pipeline de Integração Contínua (CI)
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints.py     # Rotas da API (POST /vistorias, POST /auth/login)
│   │   ├── core/
│   │   │   └── security.py      # Gestão de tokens JWT e segurança
│   │   ├── models/
│   │   │   └── schemas.py       # Esquemas Pydantic para validação
│   │   ├── services/
│   │   │   └── calculator.py    # Lógica de cálculo de pisos e argamassa
│   │   └── main.py              # Ponto de entrada da aplicação FastAPI
│   ├── tests/
│   │   ├── test_calculator.py   # Testes unitários do motor de cálculo
│   │   └── test_api.py          # Testes de integração dos endpoints
│   └── requirements.txt         # Dependências do backend
├── frontend/
│   ├── css/
│   │   └── style.css            # Folha de estilos acessível (WCAG AA)
│   ├── js/
│   │   └── app.js               # Lógica de cálculo reativo e envio assíncrono
│   └── index.html               # Aplicação responsiva de vistoria e checklist
├── docs/
│   └── plano-validacao.md       # Documentação do plano de teste e métricas
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 6. Como Executar a Aplicação Localmente

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Git instalado.
- Navegador web moderno.

### Passo 1: Clonar o Repositório
```bash
git clone [suspicious link removed]
cd daje-servicos-mvp
```

### Passo 2: Configurar o Backend
```bash
# Navegar até a pasta do backend
cd backend

# Criar e ativar o ambiente virtual
python -m venv venv
# No Linux/macOS:
source venv/bin/activate
# No Windows:
.\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor de desenvolvimento
uvicorn app.main:app --reload --port 8000
```
O backend estará acessível em `http://localhost:8000`. A documentação interativa da API poderá ser consultada em `http://localhost:8000/docs`.

### Passo 3: Executar a Interface (Frontend)
Abra o arquivo `frontend/index.html` diretamente em seu navegador ou utilize a extensão *Live Server* do Visual Studio Code.

### Passo 4: Executar a Suíte de Testes Automatizados
```bash
# Na pasta backend (com o venv ativo):
pytest -v
```

---

## 🧪 7. Metodologia de Validação com a Comunidade

O sistema é submetido a rodadas de testes práticos de usabilidade no canteiro de obras, avaliando o ajudante operacional através de três critérios de aceitação rigorosos:
- **Usabilidade:** Meta de 100% de conclusão autônoma das tarefas operacionais sem ajuda direta.
- **Eficiência:** Meta de tempo inferior a 120 segundos para conclusão da funcionalidade central (cálculo e envio de vistoria).
- **Satisfação:** Avaliação mínima de 4 em escala padronizada de 1 a 5 (de muito difícil a muito fácil).

---

## 📄 Licença

Este projeto é desenvolvido para fins educacionais e acadêmicos sob a licença **MIT** — consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
```

---

