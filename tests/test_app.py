from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_zero.app import app

client = TestClient(app)


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa (o SUT)
    - A: Assert - Garanta que A é A
    """

    # arrange
    client = TestClient(app)

    # act
    response = client.get('/')

    # assert
    assert response.json() == {'message': 'Olá, Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_root_deve_retornar_ola_mundo_html():
    """
    Esse teste tem etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa (o SUT)
    - A: Assert - Garanta que A é A
    """

    # arrange
    client = TestClient(app)

    # act
    response = client.get('/html')

    # assert
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá, Mundo! </h1>' in response.text
