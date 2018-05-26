import pytest
from op_stats.aplicacion import app
from op_stats.datosPc import Datos

import sys
sys.path.append('/home/sebastian/Escritorio/so-exam3/A00329796/')


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_darPorcentajePc(mocker, client):
    mocker.patch.object(Datos, 'darPorcentajeCpu', return_value=100)
    response = client.get('/darDatos/cpu')
    assert response.data.decode('utf-8') == '{"Porcentaje cpu": 100}'
    assert response.status_code == 200


def test_darMemoriaRam(mocker, client):
    mocker.patch.object(Datos, 'darMemoriaRam', return_value=3000)
    response = client.get('/darDatos/memoriaram')
    assert response.data.decode('utf-8') == '{"Memoria ram": 3000}'
    assert response.status_code == 200


def test_darEspacioDiscoLibre(mocker, client):
    mocker.patch.object(Datos, 'darEspacioLibreDisco', return_value=3000)
    response = client.get('/darDatos/espaciolibre')
    assert response.data.decode('utf-8') == '{"Espacio disponible": 3000}'
    assert response.status_code == 200
