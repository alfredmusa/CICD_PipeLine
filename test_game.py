import validate_email

import pytest

@pytest.mark.parametrize('email, is_ok' ,[
    ('agonzalez26117@gmail.com', True),
    ('agonzalez@gmail.com', True),
    ('agonzalez', False)
])
def test_validate_email(email, is_ok):
    assert validate_email(email)== is_ok
