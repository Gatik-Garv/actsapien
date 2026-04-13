---
title: ActSapien
emoji: 🌿
colorFrom: green
colorTo: blue
sdk: docker
pinned: false
license: mit
short_description: ActSapien — eco-habit tracker & carbon scorer
app_port: 7860
---

# ActSapien 🌿

A daily eco-habit tracking app that turns your travel choices, lifestyle actions and advocacy into a real Carbon Score.

## Features
- 🚗 Getting Around — walk, cycle, transit, carpool, EV
- ⚡ EV Charged — log kWh for verifiable real-world impact  
- 🌿 Lifestyle — veg meals, electricity saving, recycling, advocacy
- ✦ Verified logs via Strava, Apple Health, Google Fit, Garmin
- 📊 Impact screen — Weekly / Monthly / Yearly / Lifetime CO₂
- 🎯 User-set daily CO₂ goal
- 🌓 Auto light / dark mode

## API Endpoints
- `GET /` — serves the app
- `POST /reset` — resets environment state
- `GET /health` — health check
