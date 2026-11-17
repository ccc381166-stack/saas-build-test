from app import app

def test_health():
    assert app.test_client().get('/healthz').status_code == 200

def test_index():
    assert app.test_client().get('/').json['message'] == 'hello saas'
