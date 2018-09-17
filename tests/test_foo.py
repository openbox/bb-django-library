import pytest

from bb_django_library.models import Foo


@pytest.mark.django_db
def test_should_create_foo_instance_successfully():
    foo = Foo.objects.create(bar='foobar')
    assert foo.bar == 'foobar'
