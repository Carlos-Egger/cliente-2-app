from app.processor import calcular_media_idade

def test_media_idade():
    media = calcular_media_idade('data/usuarios.csv')
    assert round(media, 2) == 30.0
