# Run ALL tests
pytest

# Run ALL tests with verbose output
pytest -v

# Run a specific test class
pytest test_factorize_smarter.py::TestFactorizeSmarter

# Run a specific test function
pytest test_factorize_smarter.py::TestFactorizeSmarter::test_factoize_prime_number

# Run tests matching a pattern
pytest -k "prime"

# Run with coverage report
pytest --cov=factorize_smarter
