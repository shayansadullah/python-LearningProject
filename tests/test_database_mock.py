"""Examples of mocking SQL database operations."""

from unittest.mock import MagicMock, patch

import pytest


# Example 1: Simple database class to test
class UserDatabase:
    """Simple database handler for user operations."""

    def __init__(self, connection):
        """Initialize with a database connection.

        Args:
            connection: Database connection object.

        """
        self.connection = connection

    def get_user_by_id(self, user_id):
        """Retrieve a user by ID.

        Args:
            user_id: The user's ID.

        Returns:
            Dictionary containing user data or None if not found.

        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return {"id": result[0], "name": result[1], "email": result[2]}
        return None

    def create_user(self, name, email):
        """Create a new user.

        Args:
            name: User's name.
            email: User's email.

        Returns:
            The ID of the newly created user.

        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.connection.commit()
        user_id = cursor.lastrowid
        cursor.close()
        return user_id

    def get_all_users(self):
        """Get all users from the database.

        Returns:
            List of user dictionaries.

        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        results = cursor.fetchall()
        cursor.close()

        return [{"id": row[0], "name": row[1], "email": row[2]} for row in results]


# Test Examples using unittest.mock


def test_get_user_by_id_found():
    """Test retrieving an existing user by ID using mocked database."""
    # Create mock connection and cursor
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    # Configure the mock to return our cursor
    mock_connection.cursor.return_value = mock_cursor

    # Mock the database response
    mock_cursor.fetchone.return_value = (1, "John Doe", "john@example.com")

    # Create the database instance with mocked connection
    db = UserDatabase(mock_connection)

    # Execute the method
    user = db.get_user_by_id(1)

    # Assertions
    assert user is not None
    assert user["id"] == 1
    assert user["name"] == "John Doe"
    assert user["email"] == "john@example.com"

    # Verify the SQL was called correctly
    mock_cursor.execute.assert_called_once_with(
        "SELECT id, name, email FROM users WHERE id = ?", (1,)
    )
    mock_cursor.close.assert_called_once()


def test_get_user_by_id_not_found():
    """Test retrieving a non-existent user returns None."""
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    # Mock empty result
    mock_cursor.fetchone.return_value = None

    db = UserDatabase(mock_connection)
    user = db.get_user_by_id(999)

    assert user is None
    mock_cursor.execute.assert_called_once()


def test_create_user():
    """Test creating a new user with mocked database."""
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    # Mock the lastrowid to simulate inserted user ID
    mock_cursor.lastrowid = 42

    db = UserDatabase(mock_connection)
    user_id = db.create_user("Jane Smith", "jane@example.com")

    # Verify the returned ID
    assert user_id == 42

    # Verify SQL execution
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        ("Jane Smith", "jane@example.com"),
    )

    # Verify commit was called
    mock_connection.commit.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_get_all_users():
    """Test retrieving all users from database."""
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    # Mock multiple rows
    mock_cursor.fetchall.return_value = [
        (1, "Alice", "alice@example.com"),
        (2, "Bob", "bob@example.com"),
        (3, "Charlie", "charlie@example.com"),
    ]

    db = UserDatabase(mock_connection)
    users = db.get_all_users()

    # Verify results
    assert len(users) == 3
    assert users[0]["name"] == "Alice"
    assert users[1]["name"] == "Bob"
    assert users[2]["name"] == "Charlie"

    mock_cursor.execute.assert_called_once_with("SELECT id, name, email FROM users")


# Example 2: Using @patch decorator to mock sqlite3 module


@patch("sqlite3.connect")
def test_database_connection_with_patch(mock_connect):
    """Test database operations using @patch decorator.

    Args:
        mock_connect: Mocked sqlite3.connect function.

    """
    # Setup mock connection and cursor
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    # Mock query result
    mock_cursor.fetchone.return_value = (1, "Test User", "test@example.com")

    # Your code that uses sqlite3.connect
    import sqlite3

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (1,))
    result = cursor.fetchone()

    # Assertions
    assert result[1] == "Test User"
    mock_connect.assert_called_once_with("test.db")
    cursor.execute.assert_called_once()


# Example 3: Testing error handling


def test_database_connection_error():
    """Test handling of database connection errors."""
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    # Simulate a database error
    mock_cursor.execute.side_effect = Exception("Database connection lost")

    db = UserDatabase(mock_connection)

    # Verify exception is raised
    with pytest.raises(Exception, match="Database connection lost"):
        db.get_user_by_id(1)


# Example 4: Testing transaction rollback


def test_transaction_rollback_on_error():
    """Test that transactions are rolled back on error."""
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    # Simulate commit failure
    mock_connection.commit.side_effect = Exception("Commit failed")

    db = UserDatabase(mock_connection)

    with pytest.raises(Exception, match="Commit failed"):
        db.create_user("Test", "test@example.com")

    # Even though commit failed, execute was still called
    mock_cursor.execute.assert_called_once()


# Example 5: More realistic scenario with context manager


class DatabaseManager:
    """Database manager with context manager support."""

    def __init__(self, db_path):
        """Initialize database manager.

        Args:
            db_path: Path to the database file.

        """
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        """Enter context manager."""
        import sqlite3

        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager."""
        if self.connection:
            if exc_type:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()


@patch("sqlite3.connect")
def test_context_manager_success(mock_connect):
    """Test successful database operations with context manager.

    Args:
        mock_connect: Mocked sqlite3.connect function.

    """
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    # Use the context manager
    with DatabaseManager("test.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Test User",))

    # Verify commit was called (no exception)
    mock_connection.commit.assert_called_once()
    mock_connection.close.assert_called_once()


@patch("sqlite3.connect")
def test_context_manager_rollback(mock_connect):
    """Test rollback on exception in context manager.

    Args:
        mock_connect: Mocked sqlite3.connect function.

    """
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    # Simulate an error during execution
    mock_cursor.execute.side_effect = Exception("Constraint violation")

    try:
        with DatabaseManager("test.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name) VALUES (?)", ("Test",))
    except Exception:
        pass

    # Verify rollback was called instead of commit
    mock_connection.rollback.assert_called_once()
    mock_connection.commit.assert_not_called()
    mock_connection.close.assert_called_once()
