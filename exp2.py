def format_report(func):
    def wrapper(self):
        report = func(self)
        return "----- REPORT -----\n" + report + "\n------------------"
    return wrapper


class Report:
    reports = []

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return self.title + "\n" + self.content

    @classmethod
    def add_report(cls, report):
        cls.reports.append(report)

    @format_report
    def generate_report(self):
        return str(self)


report1 = Report("Student Report", "Name: Tanishka\nMarks: 90")

Report.add_report(report1)

print(report1.generate_report())