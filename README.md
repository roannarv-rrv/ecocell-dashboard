# 🌿 EcoCell Dashboard — Gestão Ambiental na Indústria de Celulose

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-4D8B6F?style=for-the-badge)

> Dashboard de monitoramento de indicadores ambientais para empresas do setor de celulose e papel, com foco em conformidade, eficiência hídrica, emissões de carbono e reflorestamento.

---

## 📌 Objetivo

Criar uma solução de BI que permita acompanhar os principais **KPIs ambientais** de uma empresa de celulose ao longo do tempo, identificando tendências, desvios de metas e oportunidades de melhoria — apoiando decisões orientadas à sustentabilidade e ESG.

---

## 📊 Páginas do Dashboard

| Página | Conteúdo |
|---|---|
| **Visão Geral** | KPIs consolidados, tendência de consumo e status das metas 2024 |
| **Recursos & Floresta** | Água, CO₂ e energia por ano, carbono sequestrado por município e espécies plantadas |
| **Efluentes & Incidentes** | % tratamento, reciclagem vs aterro, incidentes por severidade e tipo |

---

## 💡 Principais Insights

- 📉 O consumo de água reduziu de **28,5 para 25,6 m³/ton** entre 2022 e 2024, mas ainda está **6,7% acima da meta** de 24,0
- ✅ A eficiência energética foi a **única meta 100% atingida** em 2024: 10,26 vs meta 10,2 GJ/ton
- 🌳 A área reflorestada **superou a meta** em 2024: 19.420 ha vs meta de 18.000 ha (+7,9%)
- ⚠️ A reciclagem de resíduos é o **maior gargalo**: 67,8% vs meta de 78%
- 🔴 Foram registrados **4 incidentes de alta severidade** — acima da meta máxima de 3

---

## 🗂️ Estrutura do Projeto

```
ecocell-dashboard/
├── data/
│   ├── consumo_mensal.csv          # Água, energia, CO₂ e produção (2022-2024)
│   ├── reflorestamento.csv         # Área plantada por município e espécie
│   ├── efluentes_residuos.csv      # Tratamento de efluentes e resíduos sólidos
│   ├── incidentes.csv              # Registro de incidentes ambientais
│   └── metas_ambientais.csv        # Metas vs realizado por indicador
├── scripts/
│   └── gerar_dados.py              # Script Python que gerou os dados fictícios
├── assets/
│   └── screenshots/                # Prints das páginas do dashboard
└── README.md
```

---

## 📁 Sobre os Dados

> ⚠️ **Os dados deste projeto são 100% fictícios**, gerados com Python para fins educacionais e de portfólio. Os valores foram calibrados com base em benchmarks públicos do setor de celulose (relatórios Suzano, IBÁ).

**Período:** Janeiro/2022 a Dezembro/2024  
**Municípios simulados:** Sul da Bahia, Norte do Espírito Santo e Nordeste de Minas Gerais  
**Geração:** [`scripts/gerar_dados.py`](scripts/gerar_dados.py)

---

## 🛠️ Tecnologias

- **Power BI Desktop** — modelagem estrela, medidas DAX, visualizações
- **Python 3.x** — geração dos dados fictícios
- **Figma** — prototipação do layout do dashboard
- **IA generativa** — apoio no desenvolvimento e aprendizado
- **Git/GitHub** — versionamento do projeto

---

## ⚙️ Modelagem de Dados

O projeto utiliza **esquema estrela (Star Schema)** com tabelas dimensão e fato:

```
     DimData          DimMunicipio
    (ano, mes)       (municipio, UF)
        │                  │
  ┌─────┼─────┐      ┌─────┘
  │     │     │      │
consumo efluentes metas  reflorestamento  incidentes
```

---

## 🔧 Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/roannarv-rrv/ecocell-dashboard.git
```

2. Abra o arquivo `.pbix` no **Power BI Desktop**

3. Se necessário, atualize o caminho dos CSVs em:  
   `Página Inicial → Transformar Dados → Configurações da Fonte de Dados`

---

## 🗺️ Próximos Passos

- [ ] Adicionar página de análise preditiva (tendência de metas futuras)
- [ ] Conectar a fonte de dados real via API pública (ex: dados IBAMA)
- [ ] Criar versão em **Streamlit** para publicação web gratuita
- [ ] Adicionar drill-through por município nos incidentes

---

## 👩‍💻 Autora

**Roanna** — Estudante de Análise e Desenvolvimento de Sistemas (IFBA)  
Em transição para a área de Analytics & BI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/roannarv-rrv)

---

*Projeto desenvolvido para fins de aprendizado e composição de portfólio.*
