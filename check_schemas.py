import six
from target.schemas.swagger_client.schemas.models.tag import Tag

def test_tag():
    t = Tag(id=1,name="test")
    assert t.id == 1
    assert t.name == "test"
    assert t.to_dict() == {'id': 1, 'name': 'test'}