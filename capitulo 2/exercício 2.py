capa = 24.95
desconto = capa * 0.40
precocapalivraria = capa - desconto

freteprimeiroexemplar = 3.00
freterestanteexemplares = 0.75

custoatacadoprimeiroexemplar = precocapalivraria + freteprimeiroexemplar
custoatacado = custoatacadoprimeiroexemplar + (precocapalivraria + freterestantelivraria)

print("O custo total de atacado de 60 copias é de: ", custoatacado)