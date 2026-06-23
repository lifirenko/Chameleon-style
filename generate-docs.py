#!/usr/bin/env python3
"""Генератор документации MFT StatArb & News Bot"""
import os
from pathlib import Path

FILES = {}

FILES["README.md"] = """# 📚 MFT StatArb & News Bot

**MFT StatArb & News Bot** — среднечастотный торговый робот на базе:
- Статистического арбитража (парный трейдинг)
- Анализа макро-новостей (FinBERT NLP)
- Двухуровневой защиты от структурных сдвигов (ADF + CUSUM + PELT)

## 📖 Документация

Смотрите папку `docs/` для полной документации.

## 🛠 Стек

- Python 3.11+, Asyncio, TimescaleDB, Docker, Prometheus, Grafana

## 📊 Целевые метрики

| Метрика | Значение |
|---|---|
| Sharpe Ratio | > 1.5 |
| Max Drawdown | < 10% |
| Win Rate | 55-65% |
| Uptime | > 99.5% |
"""

FILES["docs/01-discovery/market-research.md"] = """# Market Research

**Дата:** 24 июня 2026 | **Статус:** ✅ Approved

## 1. Макроэкономический контекст (2026)

- **ФРС:** Переход к нейтральной политике
- **M2:** Стабилизация ~$21.5 трлн (+4% YoY)
- **ETF:** Приток в IBIT, FBTC, ETHW

## 2. Институционализация

| Показатель | 2023 | 2025 | 2026 |
|---|---|---|---|
| BTC-ETF AUM | $10B | $85B | $150B+ |
| Доля институционалов | 15% | 35% | 50%+ |
| Спред BTC/USDT | 0.05% | 0.02% | 0.01% |

## 3. Возможности для MFT

| Стратегия | Потенциал | Конкуренция |
|---|---|---|
| HFT скальпинг | Низкий | Экстремальная |
| **StatArb** | **Средний-Высокий** | **Умеренная** |
| News-based | Высокий | Низкая |

**Вывод:** StatArb + News = оптимальный выбор.
"""

FILES["docs/01-discovery/competitive-analysis.md"] = """# Competitive Analysis

## 1. Розничные боты

| Критерий | 3Commas | Pionex | HaasOnline |
|---|---|---|---|
| StatArb | ❌ | ❌ | ⚠️ |
| News Integration | ❌ | ❌ | ⚠️ |
| Regime Detection | ❌ | ❌ | ❌ |
| Sharpe Ratio | 0.3-0.8 | 0.2-0.5 | 0.5-1.2 |

## 2. Институциональные платформы

| Критерий | Hummingbot | QuantConnect |
|---|---|---|
| StatArb | ✅ | ✅ |
| Regime Detection | ⚠️ | ✅ |
| Сложность | Высокая | Очень высокая |

## 3. Наша ниша

**Prosumer StatArb с интеллектуальной защитой**
- Средняя сложность + Средняя-Высокая доходность
- Sharpe 1.0-2.0
"""

FILES["docs/01-discovery/user-personas.md"] = """# User Personas

## Persona 1: Алексей — Solo Quant
- **Капитал:** $10K-100K
- **Цель:** Автоматизация + Sharpe > 1.5
- **Боль:** Эмоциональная торговля, нет времени

## Persona 2: Марина — Pro Trader
- **Капитал:** $100K-500K
- **Цель:** Диверсификация стратегий
- **Боль:** Выгорание от ручной торговли

## Persona 3: Дмитрий — Fund Manager
- **AUM:** $500K-5M
- **Цель:** Масштабирование до $10M
- **Боль:** Высокие комиссии институциональных платформ
"""

FILES["docs/02-planning/lean-canvas.md"] = """# Lean Canvas

## 1. Problem
- Розничные трейдеры теряют на эмоциях
- Существующие боты предлагают только простые стратегии
- StatArb требует сложных знаний

## 2. Customer Segments
- **Primary:** Solo Quant ($10K-100K)
- **Secondary:** Small Crypto Fund ($100K-1M)

## 3. Value Proposition
"Институциональная стратегия StatArb с защитой от структурных сдвигов"

## 4. Solution
- StatArb Engine (парный трейдинг)
- Regime Detection (ADF + CUSUM + PELT)
- News Sentiment Layer (FinBERT)
- Dynamic Position Sizing

## 5. Revenue Streams
- Open Core: Free / $99/мес / $499/мес
- Performance Fee: 2% + 20%
- Proprietary Trading

## 6. Key Metrics
- Sharpe > 1.5, Max DD < 10%, Win Rate 55-65%
"""

FILES["docs/02-planning/PRD.md"] = """# Product Requirements Document

**Продукт:** MFT StatArb & News Bot  
**Версия:** 1.0 | **Дата:** 24 июня 2026

## 1. Success Metrics

| Метрика | Цель |
|---|---|
| Sharpe Ratio | > 1.5 |
| Max Drawdown | < 10% |
| Win Rate | 55-65% |
| Uptime | > 99.5% |

## 2. Functional Requirements

### 2.1 Data Collection
- FR-1.1: Сбор 1m/5m свечей для топ-20 пар
- FR-1.2: Сбор Funding Rates
- FR-1.3: Сбор макро-новостей

### 2.2 Regime Detection
- FR-2.1: ADF Test (p < 0.05)
- FR-2.2: CUSUM Test
- FR-2.3: PELT Change Points
- FR-2.4: Confidence Score (0.0-1.0)

### 2.3 Alpha Generation
- FR-3.1: Hedge Ratio через OLS
- FR-3.2: Z-Score calculation
- FR-3.3: Сигналы ENTRY/EXIT

### 2.4 News Sentiment
- FR-4.1: FinBERT анализ
- FR-4.2: Блокировка перед FOMC/CPI

### 2.5 Execution
- FR-5.1: Bybit API v5
- FR-5.2: Limit orders (Maker)
- FR-5.3: TWAP для больших позиций

### 2.6 Risk Management
- FR-6.1: Kelly Criterion (0.5)
- FR-6.2: Max position 20%
- FR-6.3: Max drawdown 10%

## 3. Non-Functional Requirements
- Latency < 200ms
- Uptime > 99.5%
- Code coverage > 80%
"""

FILES["docs/02-planning/roadmap.md"] = """# Roadmap

**Горизонт:** 10 недель до production

## Phase 1: Foundation (Weeks 1-2)
- Data Pipeline
- TimescaleDB
- Docker Compose

## Phase 2: Core Analytics (Weeks 3-4)
- Regime Detection (ADF + CUSUM + PELT)
- Alpha Engine (Z-Score)
- Backtest

## Phase 3: Execution & Risk (Weeks 5-6)
- Execution Engine
- Risk Manager
- Paper Trading

## Phase 4: News Layer (Weeks 7-8)
- NewsCollector
- SentimentAnalyzer
- Economic Calendar

## Phase 5: Production (Weeks 9-10)
- Final integration
- Optimization
- Live deployment

## Milestones

| Week | Milestone |
|---|---|
| 2 | Data Pipeline Ready |
| 4 | Analytics Ready |
| 6 | Execution Ready |
| 8 | News Layer Ready |
| 10 | Production Launch |
"""

FILES["docs/03-architecture/system-architecture.md"] = """# System Architecture

## Context Diagram (Level 1)


