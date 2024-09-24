from arithmetic import Arithmetic


class UserInterface:

    @staticmethod
    def prompt_user_for_number() -> int:
        return int(input("Please enter an integer: "))

    def add_nums_from_user_input() -> None:

        num1 = UserInterface.prompt_user_for_number()
        num2 = UserInterface.prompt_user_for_number()
        # change the function call
        print(
            f"The sum of {num1} + {num2} is:", Arithmetic.add_nums(num1, num2)
        )
