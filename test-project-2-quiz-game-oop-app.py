import random
import re


class QuizGame:

    def __init__(self):
        self.execute = 'Y'
        self.no_of_questions = 5
        self.score = 0

    def get_list_of_questions(self):
        questions = {
            'What is jedidiah\'s nickname': 'jed',
            'When is jedidiah\'s birthday': 'jan-1-1990',
            'What is jedidiah\'s age': '35',
            'What is jedidiah\'s favorite food': ['bbq', 'barbeque', 'Egg'],
            'What is jedidiah\'s favorite color': ['red', 'black'],
            'What is jedidiah\'s favorite sports': 'basketball',
            'What is jedidiah\'s favorite computer game': ['ragnarok', 'cabal'],
        }

        return questions

    def select_random_questions(self):
        selected_questions = random.sample(
            list(self.get_list_of_questions().items()), self.no_of_questions)

        return selected_questions

    def process_question_and_answer(self):
        selected_questions = self.select_random_questions()

        for question, correct_answer in selected_questions:
            answer = input(f"{question} ? ").strip().lower()
            self.check_answer(correct_answer, answer)

    def check_answer(self, correct_answer, answer):
        def normalize(text):
            # Removes special characters and converts text to lowercase.
            return re.sub(r"[^a-zA-Z0-9\s]", "", text).lower().strip()

        normalized_answer = normalize(answer)

        if isinstance(correct_answer, list):
            normalized_correct_answers = [
                normalize(ans) for ans in correct_answer]
            is_correct = normalized_answer in normalized_correct_answers
            correct_display = " or ".join(correct_answer)
        else:
            is_correct = normalized_answer == normalize(correct_answer)
            correct_display = correct_answer

        if is_correct:
            print("Your answer is correct")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_display}")

    def run(self):
        while self.execute == 'Y':
            print('--------Quiz Game 2025--------')
            player_name = input('Enter your name: ')
            self.process_question_and_answer()
            print(f"{player_name}'s score is {self.score}/{self.no_of_questions}")

            self.execute = input(
                "Do you want to play another game? (Y or N): ").strip().upper()
            if self.execute == 'N':
                break
            else:
                self.score = 0


# Run the quiz game
if __name__ == "__main__":
    QuizGame().run()
