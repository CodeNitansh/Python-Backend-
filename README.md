# Banking System Application

This is a simplified banking system application that follows the principles of clean architecture. The application consists of three layers: Domain, Use Case, and Infrastructure.

## Project Structure

The project is organized into the following directories:

- **domain**: Contains entities representing domain concepts (e.g., Account, Customer).
- **service**: Includes use case classes for specific functionalities (e.g., creating an account, making a transaction).
- **infra**: Deals with the interaction between the application and the outside world (e.g., AccountRepository for data persistence).
- **tests**: Contains unit tests for the implemented functionality.
- **main.py**: The main script demonstrating the use of various classes and methods.
- **README.md**: This file which you are reading and providing information about the project.

## How to Run

1. Ensure you have Python installed (version 3.x).
2. Navigate to the project directory.
3. Run the `main.py` script using the following command:

   ```bash
   python main.py
   ```

4. for runing unit test cases
    ```bash
    python -m unittest discover tests
    ```

