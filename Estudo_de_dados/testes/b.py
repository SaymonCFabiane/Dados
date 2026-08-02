from PIL import Image

# Abra a sua imagem
img = Image.open("./sua_imagem.jpeg")
largura, altura = img.size

# Defina o número de colunas e linhas do seu painel/grade
colunas = 2
linhas = 2

largura_quadro = largura // colunas
altura_quadro = altura // linhas

quadro_num = 1
for i in range(linhas):
    for j in range(colunas):
        box = (
            j * largura_quadro,
            i * altura_quadro,
            (j + 1) * largura_quadro,
            (i + 1) * altura_quadro,
        )
        quadro = img.crop(box)
        quadro.save(f"slide_{quadro_num}.png")
        quadro_num += 1

print("Quadros separados com sucesso!")