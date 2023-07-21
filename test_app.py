import app



def test_filtro_correcto():

    lista = [ ['daniel', 'masculino'], ['ana', 'femenino'], ['david', 'masculino'] ]
    lista_filtrada = app.filtar_lista(lista, 1, 'masculino')
    assert len(lista_filtrada) == 2
    assert lista_filtrada[0][0] == 'daniel'
    assert lista_filtrada[1][0] == 'david'
   
def test_filtro_inexistente():

    lista = [ ['daniel', 'masculino'], ['ana', 'femenino'], ['david', 'masculino'] ]
    lista_filtrada = app.filtar_lista(lista, 0, 'maria')
    assert len(lista_filtrada) == 0