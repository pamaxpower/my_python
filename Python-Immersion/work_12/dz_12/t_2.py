import csv


class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding="UTF-8") as file:
            subjects = csv.reader(file)
            subjects_list = next(subjects)
            for subject in subjects_list:
                self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if grade not in range(2, 6):
            print("Оценка должна быть целым числом от 2 до 5")
            return
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if test_score not in range(0, 101):
            print("Результат теста должен быть целым числом от 0 до 100")
            return
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        average_score = sum(test_scores) / len(test_scores)
        return average_score

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            total_grades.extend(grades)
        average_grade = sum(total_grades) / len(total_grades)
        return average_grade

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.istitle() or not value.replace(' ', '').isalpha():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name not in self.subjects:
            print(f"Предмет {name} не найден")
            return
        return self.subjects[name]

    def __str__(self):
        subjects = ", ".join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {subjects}"


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
