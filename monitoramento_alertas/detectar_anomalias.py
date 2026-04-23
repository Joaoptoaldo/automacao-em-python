#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Detecção de anomalias simples em dados (z-score).
Uso: python detectar_anomalias.py
"""

import pandas as pd
import numpy as np
from utils.helpers import setup_logger, log_info

data = pd.Series([10, 12, 11, 9, 50, 13, 14])  # 50 é anomalia
mean = data.mean()
std = data.std()
z_scores = np.abs((data - mean) / std)
anomalias = data[z_scores > 2]

logger = setup_logger('anomalias')
log_info(logger, f'Dados: {data.tolist()}')
log_info(logger, f'Anomalias: {anomalias.tolist()}')

