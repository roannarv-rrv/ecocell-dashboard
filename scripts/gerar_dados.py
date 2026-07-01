"""
gerar_dados.py
==============
Script de geração de dados fictícios para o projeto EcoCell Dashboard.

Os valores foram calibrados com base em benchmarks públicos da indústria
de celulose brasileira (Relatório de Sustentabilidade Suzano, anuário IBÁ).

Autor: Roanna
Projeto: EcoCell Dashboard — Portfólio de Data Analytics
"""

import csv
import random
from datetime import date

random.seed(42)  # garante reprodutibilidade

# ── Configurações ──────────────────────────────────────────────────────────────
MUNICIPIOS = [
    ('Eunápolis', 'BA'), ('Teixeira de Freitas', 'BA'), ('Mucuri', 'BA'),
    ('Itabela', 'BA'), ('Porto Seguro', 'BA'), ('Caravelas', 'BA'),
    ('Nanuque', 'MG'), ('Aracruz', 'ES'), ('São Mateus', 'ES'),
]
ESPECIES = ['Eucalyptus urograndis', 'Eucalyptus grandis', 'Eucalyptus saligna']
TIPOS_INCIDENTE = [
    'Vazamento de efluente', 'Derramamento de produto químico',
    'Queimada não autorizada', 'Descarte irregular de resíduo',
    'Emissão acima do limite',
]
SEVERIDADES = ['Baixa', 'Média', 'Alta']

def gerar_meses(inicio=(2022, 1), qtd=36):
    """Gera lista de objetos date com o 1º dia de cada mês."""
    meses = []
    y, m = inicio
    for _ in range(qtd):
        meses.append(date(y, m, 1))
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return meses

def tendencia(base, reducao_anual_pct, idx, ruido=0.04):
    """Simula melhoria gradual com ruído aleatório."""
    fator = 1 - (reducao_anual_pct / 12) * idx
    return round(base * fator * random.uniform(1 - ruido, 1 + ruido), 2)

def salvar_csv(nome, cabecalho, linhas):
    with open(nome, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(cabecalho)
        w.writerows(linhas)
    print(f'✓ {nome}')

# ── 1. Consumo mensal ──────────────────────────────────────────────────────────
meses = gerar_meses()
linhas = []
for i, dt in enumerate(meses):
    linhas.append([
        dt.year, dt.month, dt.strftime('%Y-%m'),
        tendencia(28.5, 0.04, i),   # água m³/ton  → meta: -4%/ano
        tendencia(11.2, 0.03, i),   # energia GJ/ton → meta: -3%/ano
        tendencia(185.0, 0.05, i),  # CO2 kg/ton   → meta: -5%/ano
        int(random.uniform(42000, 48000)),
    ])
salvar_csv('data/consumo_mensal.csv',
    ['ano','mes','data','agua_m3_por_ton','energia_gj_por_ton',
     'co2_kg_por_ton','producao_celulose_ton'], linhas)

# ── 2. Reflorestamento ─────────────────────────────────────────────────────────
linhas = []
for ano in [2022, 2023, 2024]:
    for mun, uf in MUNICIPIOS:
        plantada = round(random.uniform(800, 3200), 1)
        nativa   = round(plantada * random.uniform(0.18, 0.35), 1)
        carbono  = round(plantada * random.uniform(5.2, 7.8), 1)
        linhas.append([mun, uf, random.choice(ESPECIES),
                       plantada, nativa, ano, carbono])
salvar_csv('data/reflorestamento.csv',
    ['municipio','estado','especie','area_plantada_ha',
     'area_nativa_preservada_ha','ano_plantio','carbono_sequestrado_ton'], linhas)

# ── 3. Efluentes e resíduos ────────────────────────────────────────────────────
linhas = []
for i, dt in enumerate(meses):
    trat = round(min(99.5, tendencia(94.0, -0.015, i, 0.01)), 1)
    rec  = round(min(85,   tendencia(62.0, -0.06,  i, 0.03)), 1)
    linhas.append([
        dt.year, dt.month, dt.strftime('%Y-%m'),
        int(random.uniform(18000, 24000)), trat,
        round(random.uniform(320, 480), 1), rec, round(100 - rec, 1),
        round(random.uniform(6.8, 7.6), 1),
        round(random.uniform(45, 95), 1),
    ])
salvar_csv('data/efluentes_residuos.csv',
    ['ano','mes','data','efluente_gerado_m3','efluente_tratado_pct',
     'residuo_solido_ton','residuo_reciclado_pct','residuo_aterro_pct',
     'ph_medio_efluente','dbo_mg_l'], linhas)

# ── 4. Incidentes ──────────────────────────────────────────────────────────────
linhas = []
inc_id = 1
for dt in meses:
    for _ in range(random.randint(0, 4)):
        mun, uf = random.choice(MUNICIPIOS)
        sev  = random.choices(SEVERIDADES, weights=[55, 35, 10])[0]
        dias = {'Baixa': random.randint(1, 7),
                'Média': random.randint(5, 21),
                'Alta':  random.randint(10, 45)}[sev]
        linhas.append([
            f'INC-{inc_id:04d}',
            date(dt.year, dt.month, random.randint(1, 28)).strftime('%Y-%m-%d'),
            random.choice(TIPOS_INCIDENTE), sev, mun, uf,
            f'Ocorrência registrada na unidade de {mun}.',
            random.choice(['Resolvido', 'Em tratamento', 'Monitorando']), dias,
        ])
        inc_id += 1
salvar_csv('data/incidentes.csv',
    ['id','data','tipo','severidade','municipio','estado',
     'descricao','status','dias_para_resolucao'], linhas)

# ── 5. Metas ───────────────────────────────────────────────────────────────────
indicadores = [
    ('Consumo de água',        'm³/ton',   24.0,  25.1,  22.0,  30.2),
    ('Emissão de CO2',         'kg/ton',  160.0, 162.5, 145.0, 200.0),
    ('Energia consumida',      'GJ/ton',   10.2,  10.0,   9.5,  12.1),
    ('Efluente tratado',       '%',        99.0,  98.7,  99.5,  91.0),
    ('Reciclagem de resíduos', '%',        78.0,  76.2,  82.0,  58.0),
    ('Área reflorestada',      'ha/ano', 18000, 19420, 21000, 12000),
    ('Carbono sequestrado',    'ton/ano',120000,131400,145000,78000),
    ('Incidentes Altos',       'qtd/ano',     3,     4,     2,    10),
]
salvar_csv('data/metas_ambientais.csv',
    ['indicador','unidade','meta_2024','realizado_2024','meta_2025','baseline_2021'],
    indicadores)

print('\n✅ Dataset gerado! Importe os arquivos da pasta data/ no Power BI.')
