def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

# Test the function
student_marks = [85, 90, 78, 92, 88]
total_marks, avg_marks = sum_avg(student_marks)

print(f"Marks: {student_marks}")
print(f"Total: {total_marks}")
print(f"Average: {avg_marks:.2f}")

# Another example
another_student = [65, 72, 81, 79, 77]
total2, avg2 = sum_avg(another_student)

print(f"\nMarks: {another_student}")
print(f"Total: {total2}")
print(f"Average: {avg2:.2f}")
