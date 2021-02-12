from datetime import datetime, date

import pytest

from api.index import create_app
from api.models import (
    Hole,
    TeeBox,
    GolfCourse,
    GolfClub,
    GolfRound,
)


class TestAppConfig:
    TESTING = True
    APP_NAME = "test-footwedge"


@pytest.fixture
def app():
    app = create_app(TestAppConfig)
    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture
def content_type_header():
    return {"Content-Type": "application/json"}


@pytest.fixture
def tee_box_id():
    return 1


@pytest.fixture
def golf_course_id():
    return 1


@pytest.fixture
def golf_club_id():
    return 1


@pytest.fixture
def test_user_id():
    return -1


@pytest.fixture
def holes_post_body():
    return {
        "holes": [
            {
                "hole_number": 1,
                "name": "",
                "par": 4,
                "handicap": 7,
                "distance": 413,
                "unit": "yards"
            },
            {
                "hole_number": 2,
                "name": "",
                "par": 3,
                "handicap": 16,
                "distance": 168,
                "unit": "yards"
            },
        ]
    }


@pytest.fixture
def holes_18(golf_course_id, tee_box_id):
    return [
        Hole(
            id=1,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=1,
            name="Hole 1 Name",
            par=5,
            handicap=5,
            distance=626,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=2,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=2,
            name="Hole 2 Name",
            par=4,
            handicap=7,
            distance=471,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=3,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=3,
            name="Hole 3 Name",
            par=4,
            handicap=1,
            distance=461,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=4,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=4,
            name="Hole 4 Name",
            par=4,
            handicap=9,
            distance=400,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=5,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=5,
            name="Hole 5 Name",
            par=4,
            handicap=13,
            distance=417,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=6,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=6,
            name="Hole 6 Name",
            par=3,
            handicap=17,
            distance=187,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=7,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=7,
            name="Hole 7 Name",
            par=4,
            handicap=11,
            distance=430,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=8,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=8,
            name="Hole 8 Name",
            par=3,
            handicap=15,
            distance=247,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=9,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=9,
            name="Hole 9 Name",
            par=4,
            handicap=3,
            distance=445,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=10,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=10,
            name="Hole 10 Name",
            par=4,
            handicap=8,
            distance=444,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=11,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=11,
            name="Hole 11 Name",
            par=4,
            handicap=14,
            distance=402,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=12,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=12,
            name="Hole 12 Name",
            par=4,
            handicap=10,
            distance=389,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=13,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=13,
            name="Hole 13 Name",
            par=3,
            handicap=18,
            distance=168,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=14,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=14,
            name="Hole 14 Name",
            par=4,
            handicap=2,
            distance=444,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=15,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=15,
            name="Hole 15 Name",
            par=5,
            handicap=4,
            distance=576,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=16,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=16,
            name="Hole 16 Name",
            par=3,
            handicap=16,
            distance=215,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=17,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=17,
            name="Hole 17 Name",
            par=4,
            handicap=12,
            distance=455,
            unit="yards",
            created_ts=datetime.now(),
        ),
        Hole(
            id=18,
            golf_course_id=golf_course_id,
            tee_box_id=tee_box_id,
            hole_number=18,
            name="Hole 18 Name",
            par=4,
            handicap=6,
            distance=496,
            unit="yards",
            created_ts=datetime.now(),
        )
    ]


@pytest.fixture
def tee_box_dict():
    return dict(
        tee_color="Black",
        par=71,
        distance=7334,
        unit="yards",
        course_rating=75.6,
        slope=148.0,
    )


@pytest.fixture
def tee_box_model(tee_box_id, golf_course_id, tee_box_dict):
    return TeeBox(
        id=tee_box_id,
        golf_course_id=golf_course_id,
        created_ts=datetime.now(),
        touched_ts=None,
        **tee_box_dict,
    )


@pytest.fixture
def blue_tee_box(tee_box_id, golf_course_id):
    return TeeBox(
        id=tee_box_id,
        golf_course_id=golf_course_id,
        tee_color="Blue",
        par=72,
        distance=7150,
        unit="yards",
        course_rating=74.1,
        slope=144.0,
        created_ts=datetime.now(),
        touched_ts=None,
        golf_holes=[],
    )


@pytest.fixture
def golf_course_model(golf_course_id, golf_club_id, blue_tee_box):
    return GolfCourse(
        id=golf_course_id,
        golf_club_id=golf_club_id,
        name="Champions - Main",
        num_holes=18,
        created_ts=datetime.now(),
        touched_ts=None,
        tee_boxes=[blue_tee_box]
    )


@pytest.fixture
def random_golf_club_model_with_golf_course(golf_club_id, golf_course_model):
    return GolfClub(
        id=golf_club_id,
        name="Prestigious Golf Club",
        address="123 Fairways and Greens",
        city="Houston",
        state_code="TX",
        zip_code="77024",
        phone_number="713-555-1234",
        email="champions_club@gmail.com",
        created_ts=datetime.now(),
        touched_ts=None,
        golf_courses=[golf_course_model],
    )


@pytest.fixture
def golf_club_dict():
    return dict(
        name="Some Golf Club",
        address="123 Fairways and Greens",
        city="Chicago",
        state_code="IL",
        zip_code="60647",
        phone_number="312-555-1234",
        email="great_club@gmail.com",
    )


@pytest.fixture
def golf_club_model_no_golf_course(golf_club_dict):
    return GolfClub(id=-1, **golf_club_dict)


@pytest.fixture
def golf_course_post_body():
    return {
        'name': 'A Wonderful Course',
        'num_holes': 18,
    }


@pytest.fixture
def olympia_fields_golf_club_id():
    return 2


@pytest.fixture
def olympia_fields_north_course_id():
    return 2


@pytest.fixture
def olympia_fields_south_course_id():
    return 3


@pytest.fixture
def olympia_fields_north_black_tee_box(olympia_fields_north_course_id):
    return TeeBox(
        id=2,
        golf_course_id=olympia_fields_north_course_id,
        tee_color="Black",
        par=70,
        distance=7273,
        unit="yards",
        course_rating=76.6,
        slope=150.0,
        created_ts=datetime.now(),
        touched_ts=None,
        golf_holes=[],
    )


@pytest.fixture
def olympia_fields_south_black_tee_box(olympia_fields_south_course_id):
    return TeeBox(
        id=3,
        golf_course_id=olympia_fields_south_course_id,
        tee_color="Black",
        par=71,
        distance=7106,
        unit="yards",
        course_rating=75.0,
        slope=146.0,
        created_ts=datetime.now(),
        touched_ts=None,
        golf_holes=[],
    )


@pytest.fixture
def olympia_fields_north_course(
        olympia_fields_north_course_id,
        olympia_fields_golf_club_id,
        olympia_fields_north_black_tee_box,
):
    return GolfCourse(
        id=olympia_fields_north_course_id,
        golf_club_id=olympia_fields_golf_club_id,
        name="Olympia Fields CC - North",
        num_holes=18,
        created_ts=datetime.now(),
        touched_ts=None,
        tee_boxes=[olympia_fields_north_black_tee_box]
    )


@pytest.fixture
def olympia_fields_south_course(
        olympia_fields_south_course_id,
        olympia_fields_golf_club_id,
        olympia_fields_south_black_tee_box,
):
    return GolfCourse(
        id=olympia_fields_south_course_id,
        golf_club_id=olympia_fields_golf_club_id,
        name="Olympia Fields CC - South",
        num_holes=18,
        created_ts=datetime.now(),
        touched_ts=None,
        tee_boxes=[olympia_fields_south_black_tee_box]
    )


@pytest.fixture
def olympia_fields(
        olympia_fields_golf_club_id,
        olympia_fields_north_course,
        olympia_fields_south_course,
):
    return GolfClub(
        id=olympia_fields_golf_club_id,
        name="Olympia Fields Country Club",
        address="2800 Country Club Dr",
        city="Olympia Fields",
        state_code="IL",
        zip_code="60461",
        phone_number="708-748-0495",
        email="",
        created_ts=datetime.now(),
        touched_ts=None,
        golf_courses=[olympia_fields_north_course, olympia_fields_south_course],
    )


@pytest.fixture
def golf_round_factory(golf_course_id, tee_box_id):
    def _golf_round_factory(**kwargs):
        _id = kwargs.get('id') or -1
        _golf_course_id = kwargs.get('golf_course_id') or golf_course_id
        _tee_box_id = kwargs.get('tee_box_id') or tee_box_id
        user_id = kwargs.get('user_id') or -1
        gross_score = kwargs.get('gross_score') or 80
        towards_handicap = kwargs.get('towards_handicap') or True
        played_on = kwargs.get('played_on') or date.today()
        created_ts = kwargs.get('created_ts') or datetime.now()
        stats = kwargs.get('stats') or []
        return GolfRound(
            id=_id,
            golf_course_id=_golf_course_id,
            tee_box_id=_tee_box_id,
            user_id=user_id,
            gross_score=gross_score,
            towards_handicap=towards_handicap,
            played_on=played_on,
            created_ts=created_ts,
            touched_ts=None,
            stats=stats,
        )
    return _golf_round_factory


@pytest.fixture
def golf_round_post_body_factory(golf_course_id, tee_box_id):
    def _golf_round_post_body_factory(**kwargs):
        _golf_course_id = kwargs.get('golf_course_id') or golf_course_id
        _tee_box_id = kwargs.get('tee_box_id') or tee_box_id
        gross_score = kwargs.get('gross_score') or 80
        towards_handicap = kwargs.get('towards_handicap') or True
        played_on = kwargs.get('played_on') or date.today()
        return {
            "golf_course_id": golf_course_id,
            "tee_box_id": tee_box_id,
            "gross_score": gross_score,
            "towards_handicap": towards_handicap,
            "played_on": played_on,
        }
    return _golf_round_post_body_factory
