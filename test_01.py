import pytest

from test03 import Base


class TestPage:
    @pytest.fixture(autouse=True)
    def init_fixture(self, request):
        self.request = request

    def test_add(self):
        kw = Base(request=self.request)

        kw.base_fixture('driver')