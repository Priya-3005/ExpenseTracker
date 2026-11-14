class ExpenseNotFoundException(Exception):

    def __init__(self, expense_id: int):
        self.expense_id = expense_id
        self.message = f"Expense with ID {expense_id} not found."
        super().__init__(self.message)


class UserNotFoundException(Exception):

    def __init__(self):
        self.message = "User not found."
        super().__init__(self.message)


class InvalidCredentialsException(Exception):

    def __init__(self):
        self.message = "Invalid username or password."
        super().__init__(self.message)