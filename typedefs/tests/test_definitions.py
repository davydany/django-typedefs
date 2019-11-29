import datetime
import unittest

from typedefs.definitions import (BaseTypeDefinition, Boolean, Integer, Float,
  Date, DateTime)

class BaseTypeDefinitionTestCase(unittest.TestCase):

  def test_to_python(self):

    with self.assertRaises(NotImplementedError):

      t = BaseTypeDefinition()
      t.to_python()

  def test_from_python(self):

    with self.assertRaises(NotImplementedError):

      t = BaseTypeDefinition()
      t.from_python(True)

  def test_value(self):

    with self.assertRaises(NotImplementedError):

      t = BaseTypeDefinition(value=3)
      t.value

  def test_raw_value(self):

    t = BaseTypeDefinition(value=3)
    self.assertEqual(t.raw_value, 3)

  def test_get_value(self):
    """
    Test that calling 'i.value', where i is instantiated from a class
    that inherits from BaseTypeDefinition performs the right casting when it retrieves
    the value.
    """
    i = Integer('3')
    self.assertEqual(i.value, 3)

    i = Integer('-3')
    self.assertEqual(i.value, -3)

  def test_set_value(self):
    """
    Test that setting a value to 'i.value', where i is instantiated from a class
    that inherits from BaseTypeDefinition performs the right casting when it retrieves
    the value.
    """
    i = Integer()
    i.value = 3
    self.assertEqual(i.raw_value, '3')

    # now do the same for a negative number
    i = Integer()
    i.value = -3
    self.assertEqual(i.raw_value, '-3')


class BooleanTestCase(unittest.TestCase):

  def test_to_python(self):

    # assert Trues
    t = Boolean(value='true')
    self.assertTrue(t.to_python())

    t = Boolean(value='1')
    self.assertTrue(t.to_python())

    t = Boolean(value='t')
    self.assertTrue(t.to_python())

    t = Boolean(value='TrUe')
    self.assertTrue(t.to_python())

    # assert Falses
    t = Boolean(value='false')
    self.assertFalse(t.to_python())

    t = Boolean(value='0')
    self.assertFalse(t.to_python())

    t = Boolean(value='f')
    self.assertFalse(t.to_python())

    t = Boolean(value='FaLSe')
    self.assertFalse(t.to_python())

    # assert all other values are treated as false
    t = Boolean(value='asdfa9s8e7r293r')
    self.assertFalse(t.to_python())

  def test_from_python(self):

    t = Boolean()
    self.assertEqual(t.from_python(True), '1')

    t = Boolean()
    self.assertEqual(t.from_python(False), '0')

class IntegerTestCase(unittest.TestCase):

  def test_to_python(self):

    t = Integer(value='3')
    self.assertEqual(t.to_python(), 3)

    t = Integer(value='-3')
    self.assertEqual(t.to_python(), -3)

  def test_from_python(self):

    t = Integer()
    self.assertEqual(t.from_python(3), '3')

    t = Integer()
    self.assertEqual(t.from_python(-3), '-3')

class FloatTestCase(unittest.TestCase):

  def test_to_python(self):

    t = Float(value='3.75')
    self.assertEqual(t.to_python(), 3.75)

    t = Float(value='-3.75')
    self.assertEqual(t.to_python(), -3.75)

  def test_from_python(self):

    t = Float()
    self.assertEqual(t.from_python(3.75), '3.75')

    t = Float()
    self.assertEqual(t.from_python(-3.75), '-3.75')

class DateTestCase(unittest.TestCase):

  def test_to_python(self):

    t = Date(value='2019-10-29')
    self.assertEqual(
      t.to_python(), 
      datetime.datetime(year=2019, month=10, day=29).date())

  def test_from_python(self):

    dt = datetime.datetime.now(datetime.timezone.utc)
    t = Date()
    expected = '%s-%s-%s' % (dt.year, dt.month, dt.day)
    self.assertEqual(t.from_python(dt), expected)

class DateTimeTestCase(unittest.TestCase):

  def test_to_python(self):

    t = DateTime(value='2019-10-29T17:27:15.052655+00:00')
    self.assertEqual(
      t.to_python(),
      datetime.datetime(
        year=2019, month=10, day=29,
        hour=17, minute=27, second=15, microsecond=52655,
        tzinfo=datetime.timezone.utc
      )
    )
  
  def test_from_python(self):

    t = DateTime()
    self.assertEqual(
      t.from_python(
        datetime.datetime(
          year=2019, month=10, day=29,
          hour=17, minute=27, second=15, microsecond=52655,
          tzinfo=datetime.timezone.utc
        )
      ),
      '2019-10-29T17:27:15.052655+0000'
    )