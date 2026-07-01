🌿 EcoCell Dashboard — Gestão Ambiental na Indústria de Celulose
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/Dataset-CSV%20Fictício-4CAF50?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-orange?style=for-the-badge)
> Dashboard de monitoramento de indicadores ambientais para empresas do setor de celulose e papel, com foco em conformidade, eficiência hídrica, emissões de carbono e reflorestamento.
---
📌 Objetivo
Criar uma solução de BI que permita acompanhar os principais KPIs ambientais de uma empresa de celulose ao longo do tempo, identificando tendências, desvios de metas e oportunidades de melhoria — apoiando decisões orientadas à sustentabilidade.
---
📊 Páginas do Dashboard
Página	Conteúdo
Visão Geral	KPIs consolidados, gauge de metas e alertas
Consumo de Recursos	Água, energia e CO₂ por tonelada produzida (2022–2024)
Reflorestamento	Área plantada por município, carbono sequestrado, espécies
Efluentes & Resíduos	% tratamento, reciclagem vs aterro, pH e DBO
Incidentes Ambientais	Mapa de ocorrências, severidade, tempo de resolução
Metas 2024 vs 2025	Painel comparativo de realizado vs meta
---
🗂️ Estrutura do Projeto
```
ecocell-dashboard/
├── data/
│   ├── consumo_mensal.csv          # Água, energia, CO₂ e produção (2022-2024)
│   ├── reflorestamento.csv         # Área plantada por município e espécie
│   ├── efluentes_residuos.csv      # Tratamento de efluentes e resíduos sólidos
│   ├── incidentes.csv              # Registro de incidentes ambientais
│   └── metas_ambientais.csv        # Metas vs realizado por indicador
├── dashboard/
│   └── EcoCell_Dashboard.pbix      # Arquivo Power BI
├── assets/
│   └── screenshots/                # Prints das páginas do dashboard
├── scripts/
│   └── gerar_dados.py              # Script Python que gerou os dados fictícios
└── README.md
```
---
📁 Sobre os Dados
> ⚠️ **Os dados deste projeto são 100% fictícios**, gerados com Python para fins educacionais e de portfólio. Os valores foram calibrados com base em benchmarks públicos do setor de celulose (relatórios Suzano, BRACELPA/IBÁ).
Período: Janeiro/2022 a Dezembro/2024  
Municípios simulados: Sul da Bahia, Norte do Espírito Santo e Nordeste de Minas Gerais  
Geração: `scripts/gerar_dados.py`
---
💡 Principais Insights
📉 O consumo de água reduziu ~11% entre 2022 e 2024, indicando avanço nas metas de eficiência hídrica
♻️ A taxa de reciclagem de resíduos subiu de 62% para 76%, ainda abaixo da meta de 78%
🌳 A área reflorestada em 2024 superou a meta anual em ~8% (19.420 ha vs meta de 18.000 ha)
⚠️ Emissões de CO₂ e consumo de água ainda estão acima da meta 2024, indicando necessidade de ação
---
🛠️ Como Usar
Clone o repositório:
```bash
git clone https://github.com/seu-usuario/ecocell-dashboard.git
```
Abra o arquivo `dashboard/EcoCell_Dashboard.pbix` no Power BI Desktop
Se necessário, atualize o caminho das fontes de dados em:  
`Página Inicial → Transformar Dados → Configurações da Fonte de Dados`
---
🔧 Tecnologias
Power BI Desktop — visualização e modelagem de dados
Python 3.x — geração dos dados fictícios (`pandas`, `csv`, `datetime`)
DAX — medidas calculadas e KPIs no Power BI
Git/GitHub — versionamento
---
🗺️ Próximos Passos
[ ] Adicionar página de análise preditiva (tendência de metas futuras)
[ ] Conectar a fonte de dados real via API pública (ex: dados IBAMA/SISNAMA)
[ ] Criar versão em Streamlit para publicação web gratuita
[ ] Adicionar drill-through por município nos incidentes
---
👩‍💻 Autora
Roanna — Estudante de Análise e Desenvolvimento de Sistemas (IFBA)  
Auxiliar de Dados em transição para a área de Analytics & BI
![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
---
Projeto desenvolvido para fins de aprendizado e composição de portfólio.
