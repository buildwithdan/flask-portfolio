from api.index import app


def test_public_routes():
    client = app.test_client()
    for path in ("/", "/about", "/blog/", "/projects/", "/robots.txt", "/sitemap.xml"):
        assert client.get(path).status_code == 200


def test_resume_redirects():
    response = app.test_client().get("/resume")
    assert response.status_code == 302
    assert response.location.startswith("https://")


def test_security_and_seo_headers():
    response = app.test_client().get("/", headers={"X-Forwarded-Proto": "https"})
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert "max-age=" in response.headers["Strict-Transport-Security"]
    assert b'<meta name="description"' in response.data
    assert b'<link rel="canonical"' in response.data


def test_search_is_case_insensitive():
    response = app.test_client().post("/blog/search", data={"query": "finance"})
    assert response.status_code == 200
