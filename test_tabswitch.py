# test_tabswitch.py
"""
Tests for TabSwitch module.
"""

import unittest
from tabswitch import TabSwitch

class TestTabSwitch(unittest.TestCase):
    """Test cases for TabSwitch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TabSwitch()
        self.assertIsInstance(instance, TabSwitch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TabSwitch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
