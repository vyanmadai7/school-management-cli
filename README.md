# School Management CLI

A simple command-line school management system built with Python that helps manage students, teachers, attendance, marks, and generate academic reports.

## Features

- **Student Management**
  - Add new students with ID, name, and grade/class
  - Record and track attendance by date
  - Add subject-wise marks (0-100 scale)
  - Generate individual student report cards with GPA
  - Rank students based on GPA performance

- **Teacher Management**
  - Add teachers with ID, name, and subject specialty
  - View list of all registered teachers

- **Academic Tracking**
  - Automatic GPA calculation based on average marks
  - Subject-wise marks recording
  - Attendance tracking with date stamps
  - Student ranking system

## GPA Scale

| Average Marks | GPA  |
|--------------|------|
| 90-100       | 4.0  |
| 80-89        | 3.6  |
| 70-79        | 3.2  |
| 60-69        | 2.8  |
| 50-59        | 2.4  |
| 40-49        | 2.0  |
| Below 40     | 0.0  |

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vyanmadai7/school-management-cli.git
cd school-management-cli
```

2. Ensure you have Python 3.6+ installed:
```bash
python --version
```

## Usage

Run the application:
```bash
python school_management.py
```

### Menu Options

1. **Add Student** - Register a new student
2. **Add Teacher** - Register a new teacher
3. **Add Marks** - Record marks for a student in a subject
4. **Mark Attendance** - Mark attendance for a student (current date)
5. **Student Report** - Generate detailed report card for a student
6. **Rank Students** - View all students ranked by GPA
7. **View Teachers** - Display list of all teachers
8. **Exit** - Close the application

## Data Storage

All data is stored in `school_database.json` in the following structure:
```json
{
    "students": {
        "student_id": {
            "name": "Student Name",
            "grade": "Grade/Class",
            "marks": {"Subject": 85.0},
            "attendance": ["2025-01-10"]
        }
    },
    "teachers": {
        "teacher_id": {
            "name": "Teacher Name",
            "subject": "Subject"
        }
    },
    "subjects": {}
}
```

## Example Workflow
```bash
# Add a student
Select: 1
Student ID: S001
Name: John Doe
Grade: 10A

# Add marks
Select: 3
Student ID: S001
Subject: Mathematics
Marks (0-100): 95

# Mark attendance
Select: 4
Student ID: S001

# View report
Select: 5
Student ID: S001
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## License

MIT License - feel free to use and modify for your needs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Future Enhancements

- Subject management functionality
- Export reports to PDF/CSV
- Search and filter capabilities
- Bulk data import
- Data validation improvements
- Password protection for admin functions
