#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classificação de imagens com Torch.
Uso: Baixe imagem.jpg e rode python classificar_imagens.py imagem.jpg
"""

import torch
from torchvision import models, transforms
from PIL import Image
from utils.helpers import setup_logger, log_info
import sys

model = models.resnet50(pretrained=True)
model.eval()

transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


def classificar(imagem_path):
    """_summary_: função para classificar uma imagem usando o modelo ResNet-50 pré-treinado. A imagem é processada e a classe prevista é logada.
     O logger é configurado para registrar as previsões de classificação.

    Args:
        imagem_path (_type_): _description_: caminho para a imagem a ser classificada
    """
    logger = setup_logger("classificacao")
    img = Image.open(imagem_path).convert("RGB")
    batch = transform(img).unsqueeze(0)
    with torch.no_grad():
        outputs = model(batch)
    _, pred = torch.max(outputs, 1)
    log_info(logger, f"Classe prevista: {pred.item()} (ID {pred.item()})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python classificar_imagens.py <imagem.jpg>")
        sys.exit(1)
    classificar(sys.argv[1])
