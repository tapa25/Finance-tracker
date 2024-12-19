# Imports
import pytest

from apps.tracker.factories import TransactionFactory


# Function to create transactions
@pytest.fixture
def transactions():
    # Create transactions using the factory
    return TransactionFactory.create_batch(20)
