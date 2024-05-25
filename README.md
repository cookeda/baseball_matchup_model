# Baseball Batter-Pitcher Matchup Model

## Overview

This project aims to build a machine learning model to analyze and predict outcomes of batter-pitcher matchups in baseball. The model leverages data from Baseball Savant, processed through the `pybaseball` package, to identify pitcher weaknesses and batter strengths. The ultimate goal is to predict the success of batters against specific pitchers based on various performance metrics.

## Project Structure

baseball_matchup_model/
- data/
  - raw/
  - processed/
- notebooks/
  - data_exploration.ipynb
  - model_building.ipynb
  - evaluation.ipynb
- scripts/
  - data_collection.py
  - data_preprocessing.py
  - feature_engineering.py
  - model_training.py
  - model_evaluation.py
- models/
  - model.pkl
- reports/
  - figures/
  - final_report.md
- requirements.txt
- README.md
- .gitignore

## Stats Needed
- Pitcher Data:
  - Pitch type
  - Release speed
  - Spin rate
  - Break angle and length
  - Pitch location (plate_x, plate_z)
  - Pitcher handedness (p_throws)
  - Game context (outs, inning, home/away team)
- Batter Data:
  - Batter handedness (stand)
  - Performance metrics (BA, OBP, SLG, wOBA)
  - Split stats (performance against LHP/RHP)
  - Contact rates (O-Swing%, Z-Swing%, Contact%)
  - Outcome Data:
  - Events (hit, strikeout, walk, etc.)
  - Hit metrics (launch speed, launch angle, hit distance)