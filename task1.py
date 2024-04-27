"""Module 4/Task 1"""

from file_helper import read_file


def total_salary(path):
    """Return total and average salary"""
    total_salary = 0
    developers_count = 0

    for line in read_file(path):
        if len(line) > 1:
            developer_salary = int(line.split(",")[1])
            developers_count += 1
            total_salary += developer_salary

    average_salary = total_salary // developers_count

    return (total_salary, average_salary)


if __name__ == "__main__":
    FILE_PATH = "data_for_dz/task1.txt"
    
    total, average = total_salary(FILE_PATH)
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )
