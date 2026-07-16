#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deteccao de anomalias simples em dados (z-score).
Uso: python detectar_anomalias.py
"""

import numpy as np
import pandas as pd

from utils.helpers import setup_logger, log_info


def detectar_anomalias(data, limite_zscore=2.0):
    """Retorna os valores considerados anomalias usando z-score."""
    serie = pd.Series(data)
    mean = serie.mean()
    std = serie.std()

    if std == 0 or np.isnan(std):
        return pd.Series(dtype=serie.dtype)

    z_scores = np.abs((serie - mean) / std)
    return serie[z_scores > limite_zscore]


def main() -> None:
    data = pd.Series([10, 12, 11, 9, 50, 13, 14])
    anomalias = detectar_anomalias(data)
    logger = setup_logger("anomalias")
    log_info(logger, f"Dados: {data.tolist()}")
    log_info(logger, f"Anomalias: {anomalias.tolist()}")


if __name__ == "__main__":
    main()
