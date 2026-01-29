from student_card import StudentCard

class IStudentCard(StudentCard):
    def __init__(self, id, name, nationality):
        self.nationality = nationality
        super().__init__(id, name)

    def print_info(self):
        print(f'国籍: {self.nationality}')
        super().print_info()

card = IStudentCard('A123456', '赤松佑哉', '日本')
card.print_info()
