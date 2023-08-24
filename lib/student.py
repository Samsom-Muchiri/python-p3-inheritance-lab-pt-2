class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        super().hello()  # Inherit and call parent class's hello() method
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()  # Call parent class's raise_hand() method ten times

# Creating instances
normal_student = Student()
chatty_student = ChattyStudent()

# Testing methods
normal_student.hello()
normal_student.raise_hand()

print("\n")  # Adding a newline for separation

chatty_student.hello()
chatty_student.raise_hand()
