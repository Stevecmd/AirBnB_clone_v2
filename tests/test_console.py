"""
Unit tests for console using doctest
"""

import unittest
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    """Contains the tests for the console"""

    def setUp(self):
        """Set up test environment"""
        self.backup = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test environment"""
        sys.stdout = self.backup
        self.output.close()

    def test_do_create(self):
        """Test create command"""
        command = HBNBCommand()
        create_command = (
            'create User '
            'email="example@example.com" '
            'password="password"'
        )
        command.onecmd(create_command)
        output = self.output.getvalue().strip()
        print(f"Output from create command: {output}")  # Debugging line
        all_objects = storage.all()
        print(f"All objects in storage: {all_objects}")  # Debugging line
        key = f"User.{output}"  # Adjust key format if necessary
        self.assertTrue(key in all_objects.keys())

    def test_do_show(self):
        """Test show command"""
        HBNBCommand().onecmd('create State name="California"')
        state_id = self.output.getvalue().strip()
        self.output.truncate(0)
        self.output.seek(0)
        HBNBCommand().onecmd(f"show State {state_id}")
        expected_output = f"[State] ({state_id})"
        actual_output = self.output.getvalue().strip()
        self.assertIn(expected_output, actual_output)

    def test_do_destroy(self):
        """Test destroy command"""
        command = HBNBCommand()
        create_command = (
            'create City '
            'name="San Francisco" '
            'state_id="dummy_state_id"'
        )
        command.onecmd(create_command)
        city_id = self.output.getvalue().strip()
        self.output.truncate(0)
        self.output.seek(0)
        HBNBCommand().onecmd(f"destroy City {city_id}")
        self.assertNotIn(city_id, storage.all().keys())

    def test_do_all(self):
        """Test all command"""
        command = HBNBCommand()
        create_command = (
            'create User '
            'email="example2@example.com" '
            'password="password"'
        )
        command.onecmd(create_command)
        user_id = self.output.getvalue().strip()
        self.output.truncate(0)
        self.output.seek(0)
        HBNBCommand().onecmd("all User")
        self.assertIn(f"[User] ({user_id})", self.output.getvalue().strip())

    def test_do_update(self):
        """Test update command"""
        command = HBNBCommand()
        command_string = """create Place
        name="My Place"
        city_id="dummy_city_id"
        user_id="dummy_user_id"
        """
        command.onecmd(command_string)
        place_id = self.output.getvalue().strip()
        self.output.truncate(0)
        self.output.seek(0)
        command = HBNBCommand()
        update_command = (
            f"update Place {place_id} name \"Updated Place\""
        )
        command.onecmd(update_command)
        self.assertIn("Updated Place", storage.all()[f"Place.{place_id}"].name)


if __name__ == "__main__":
    unittest.main()
