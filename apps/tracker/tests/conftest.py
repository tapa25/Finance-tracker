# Imports
import pytest

from apps.tracker.factories import TransactionFactory, UserFactory


# Function to create transactions
@pytest.fixture
def transactions():
    # Create transactions using the factory
    return TransactionFactory.create_batch(20)


# Function to create user transactions
@pytest.fixture
def user_transactions():
    # Create a user
    user = UserFactory()

    # Create transactions using the factory
    transactions = TransactionFactory.create_batch(20, user=user)

    # Return the user and transactions
    return user, transactions
