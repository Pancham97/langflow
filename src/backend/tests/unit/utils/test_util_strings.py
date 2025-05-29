import pytest
from langflow.utils import util_strings


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("sqlite:///test.db", True),
        ("sqlite:////var/folders/test.db", True),
        ("sqlite:///:memory:", True),
        ("sqlite+aiosqlite:////var/folders/test.db", True),
        ("singlestoredb://user:pass@localhost/dbname", True),
        ("singlestore://user:pass@localhost:3306/database", True),
        ("memsql://user:pass@host:3306/db", True),
        ("mysql://user:pass@localhost/dbname", True),
        ("mysql+mysqldb://scott:tiger@localhost/foo", True),
        ("mysql+pymysql://scott:tiger@localhost/foo", True),
        ("oracle://scott:tiger@127.0.0.1:1521/?service_name=freepdb1", True),
        ("oracle+cx_oracle://scott:tiger@tnsalias", True),
        ("oracle+oracledb://scott:tiger@127.0.0.1:1521/?service_name=freepdb1", True),
        ("", False),
        (" invalid ", False),
        ("not_a_url", False),
        (None, False),
        ("invalid://database", False),
        ("invalid://:@/test", False),
    ],
)
def test_is_valid_database_url(value, expected):
    assert util_strings.is_valid_database_url(value) == expected
