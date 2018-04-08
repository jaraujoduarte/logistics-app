import sys
import unittest
from flask.cli import FlaskGroup
from logistics import db, create_app
from logistics.models import *

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('api/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        sys.exit(0)
    sys.exit(1)


if __name__ == '__main__':
    cli()
