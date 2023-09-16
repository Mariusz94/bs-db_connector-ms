import os
import sys

import grpc
import pytest
import service.connectors.db_connector_service as db_connector_service

from default_msg import default_pb2
from bs_db_connector_msg import db_connector_pb2


@pytest.mark.parametrize(
    "user_id",
    [
        ("6242d2c0-0cfe-4b71-bbc7-f9bed50d687a"),
        ("cf32f337-afe4-4876-a835-6ba853c32804"),
    ],
)
def test_get_balance(user_id: str):
    data: dict = db_connector_service.get_balance(user_id)

    assert data["balance"] >= 0
    assert data["currency"] == "PLN"


@pytest.mark.parametrize(
    "user_id",
    [
        ("6242d2c0-0cfe-4b71-bbc7-f9bed50d687a"),
        ("cf32f337-afe4-4876-a835-6ba853c32804"),
    ],
)
def test_get_user_info(user_id: str):
    data: dict = db_connector_service.get_user_info(user_id)

    assert "id" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "phone_number" in data
    assert "address" in data
    assert "login" in data
