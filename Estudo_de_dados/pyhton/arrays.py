lista = [1,2,3,[10,'alvo',15], 18,20]
print()
print('<','='*100,'>')
print()
print(lista[3])
print(lista[3][1])

tupla = (1,2,3)

print(tupla)

cadastro = {'nome':'João', 'idade':30, 'sexo':'Masculino'}

print(type(cadastro))
print(cadastro['nome'])
print(cadastro['idade'])
print('João' in cadastro)
print('João' in cadastro.values())
print('nome' in cadastro)
print('nome' in cadastro.keys())
print(cadastro.items())
print(('nome','João') in cadastro.items())

cadastro['nome'] = 'Pedro'

print(cadastro)

cadastro['altura'] =  1.79
print(cadastro)

del(cadastro['sexo'])
print(cadastro)

cadastro_igual = cadastro

copia = cadastro.copy()

print(cadastro_igual)
print(copia)

cadastro['idade'] = 80

print(cadastro)
print(cadastro_igual)
print(copia)

meus_contatos = {'Tiago':'9999-9999', 'Felipe':'8888-8888', 'Carolina':'7777-7777'}
seus_contatos = {'Raphaela':'6666-6666', 'Luiza':'5555-5555', 'Bia':'4444-4444'}

meus_contatos.update(seus_contatos)

print(meus_contatos) 

print()
print('<','='*100,'>')
print() 
