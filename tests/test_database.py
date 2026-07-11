from src.models import Location

def test_database_connection(session):
    location = Location(
        city="Suva",
        latitude=-18.1416,
        longitude=178.4419
    )

    session.add(location)
    session.commit()
    result = (
        session.query(Location)
        .filter_by(city="Suva")
        .first()
    )


    assert result.city == "Suva"