# test_nearprotocol.py
"""
Tests for NearProtocol module.
"""

import unittest
from nearprotocol import NearProtocol

class TestNearProtocol(unittest.TestCase):
    """Test cases for NearProtocol class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NearProtocol()
        self.assertIsInstance(instance, NearProtocol)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NearProtocol()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
