# Imports
import pytest

from apps.tracker.factories import TransactionFactory, UserFactory


# Function to create transactions
@pytest.fixture
def transactions():
    # List to store all the transactions
    transactions = []

    # Traverse to create 5 users
    for _ in range(5):
        # Create a user
        user = UserFactory()

        # Batch create transactions for the user
        transactions.extend(TransactionFactory.create_batch(25, user=user))

    # Return the transactions
    return transactions


# Function to create user transactions
@pytest.fixture
def user_transactions():
    # Create a user
    user = UserFactory()

    # Create transactions using the factory
    transactions = TransactionFactory.create_batch(25, user=user)

    # Return the user and transactions
    return user, transactions


# Function to create a user
@pytest.fixture
def user():
    # Create a user using the factory and return it
    return UserFactory()


# Function to create a transaction
@pytest.fixture
def transaction_dict_params(user):
    # Create a transaction
    transaction = TransactionFactory.create(user=user)

    # Return the transaction dictionary
    return {
        "date": transaction.date,
        "category": transaction.category.id,
        "type": transaction.type,
        "amount": transaction.amount,
    }
