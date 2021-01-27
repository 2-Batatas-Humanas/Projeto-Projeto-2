import os
import tempfile

import pytest

from rpg import rpg


@pytest.fixture
def client():
    db_fd, rpg.app.config['DATABASE'] = tempfile.mkstemp()
    rpg.app.config['TESTING'] = True

    with rpg.app.test_client() as client:
        with rpg.app.app_context():
            rpg.init_db()
        yield client

    os.close(db_fd)
    os.unlink(rpg.app.config['DATABASE'])