import cv2
import numpy as np

# Caminho para a imagem de satélite (substitua pelo caminho correto no seu ambiente)
image_path = 'satelite_imagem.jpg'  # Imagem deve ser salva localmente, caso tenha baixado

# Carregar a imagem
imagem = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Imagem em escala de cinza

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    raise FileNotFoundError(f"Imagem não encontrada no caminho: {image_path}")

# Total de pixels na imagem
total_pixels = imagem.size

# Contar os pixels com códigos específicos
pixels_sem_dados = np.sum(imagem == 0)      # Código 0: sem dados
pixels_soja = np.sum(imagem == 39)          # Código 39: soja
pixels_pastagem = np.sum(imagem == 15)      # Código 15: pastagem

# Calcular a área de cobertura do Brasil em hectares (1 hectare = 10,000 m²)
# A área total do Brasil em hectares (estimada): 8.5e6 km² = 8.5e10 m² = 8.5e6 hectares
area_brasil_hectares = 8.5e6  # Área do Brasil em hectares

# Calcular a proporção de cobertura de soja e pastagem
# Excluindo os pixels "sem dados" para o cálculo
pixels_validos = total_pixels - pixels_sem_dados

# Proporção de soja e pastagem no território
soja_area_hectares = (pixels_soja / pixels_validos) * area_brasil_hectares
pastagem_area_hectares = (pixels_pastagem / pixels_validos) * area_brasil_hectares

# Exibir os resultados
print(f"Total de pixels: {total_pixels}")
print(f"Total de pixels sem dados (código 0): {pixels_sem_dados}")
print(f"Total de pixels de soja (código 39): {pixels_soja}")
print(f"Total de pixels de pastagem (código 15): {pixels_pastagem}")

print(f"\nÁrea de plantio de soja: {soja_area_hectares:.2f} hectares, Contagem de pixels: {pixels_soja}")
print(f"Área de cobertura de pastagem: {pastagem_area_hectares:.2f} hectares, Contagem de pixels: {pixels_pastagem}")
