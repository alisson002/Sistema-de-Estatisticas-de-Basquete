import base64 # Para manipulação de imagens e centralização da imagem do Grupo Allure
from io import BytesIO # Para manipulação de imagens e centralização da imagem do Grupo Allure

# Função para converter imagem em base64
def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()