from webresponse import ResponseBuilder


def test_builder_with_no_params():
    rb = ResponseBuilder()
    r = rb.build()

    assert r.status_code == 200
    assert r.message == "OK"
    assert r.data is None
    assert r.errors is None


def test_builder_with_status_code_only():
    rb = ResponseBuilder()
    rb.status = 201
    r = rb.build()

    assert r.status_code == 201
    assert r.message == "CREATED"
    assert r.data is None
    assert r.errors is None


def test_builder_with_data():
    data = {"test1": "test data", "test2": {"dict_type": 1}}
    rb = ResponseBuilder()
    rb.status = 200
    rb.data = data
    r = rb.build()

    assert r.status_code == 200
    assert r.message == "OK"
    assert r.data["test1"] == "test data"
    assert r.data["test2"]["dict_type"] == 1
    assert r.errors is None


def test_builder_with_named_error():
    rb = ResponseBuilder()
    rb.status = 500
    rb.add_named_error("error_1", "error one")
    rb.add_named_error("error_2", "error two")
    r = rb.build()

    assert r.status_code == 500
    assert r.message == "INTERNAL_SERVER_ERROR"
    assert r.errors[0] == {"error_1": "error one"}
    assert r.errors[1] == {"error_2": "error two"}


def test_builder_with_unnamed_error():
    rb = ResponseBuilder()
    rb.status = 500
    rb.add_unnamed_error("error one")
    rb.add_unnamed_error("error two")
    r = rb.build()

    assert r.status_code == 500
    assert r.message == "INTERNAL_SERVER_ERROR"
    assert r.errors[0] == {"error_1": "error one"}
    assert r.errors[1] == {"error_2": "error two"}


def test_builder_with_exception():
    rb = ResponseBuilder()
    rb.status = 500
    rb.add_exception(Exception("Oh no"))
    r = rb.build()

    assert r.status_code == 500
    assert r.message == "INTERNAL_SERVER_ERROR"
    assert r.errors[0] == {"error_1": "Oh no"}