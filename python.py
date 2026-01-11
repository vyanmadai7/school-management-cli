import json, os, datetime

FILE = "school_database.json"

# ---------------- Storage ----------------
def load_db():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {
        "students": {},
        "teachers": {},
        "subjects": {}
    }

def save_db(db):
    with open(FILE, "w") as f:
        json.dump(db, f, indent=4)

# ---------------- Student ----------------
def add_student(db):
    sid = input("Student ID: ")
    name = input("Name: ")
    grade = input("Grade/Class: ")

    db["students"][sid] = {
        "name": name,
        "grade": grade,
        "marks": {},
        "attendance": []
    }
    save_db(db)
    print("Student added.")

def mark_attendance(db):
    sid = input("Student ID: ")
    if sid not in db["students"]:
        print("Not found.")
        return
    
    today = str(datetime.date.today())
    db["students"][sid]["attendance"].append(today)
    save_db(db)
    print("Attendance marked.")

def add_marks(db):
    sid = input("Student ID: ")
    if sid not in db["students"]:
        print("Not found.")
        return

    subject = input("Subject: ")
    marks = float(input("Marks (0-100): "))
    db["students"][sid]["marks"][subject] = marks
    save_db(db)
    print("Marks added.")

def calculate_gpa(marks):
    if not marks: return 0
    avg = sum(marks.values()) / len(marks)
    if avg >= 90: return 4.0
    if avg >= 80: return 3.6
    if avg >= 70: return 3.2
    if avg >= 60: return 2.8
    if avg >= 50: return 2.4
    if avg >= 40: return 2.0
    return 0

def student_report(db):
    sid = input("Student ID: ")
    if sid not in db["students"]:
        print("Not found.")
        return
    
    s = db["students"][sid]
    gpa = calculate_gpa(s["marks"])

    print("\n----- REPORT CARD -----")
    print("Name:", s["name"])
    print("Grade:", s["grade"])
    print("Marks:", s["marks"])
    print("GPA:", gpa)
    print("Attendance days:", len(s["attendance"]))

# ---------------- Ranking ----------------
def rank_students(db):
    records = []
    for sid, s in db["students"].items():
        gpa = calculate_gpa(s["marks"])
        records.append((sid, s["name"], gpa))

    records.sort(key=lambda x: x[2], reverse=True)

    print("\n--- Student Ranking ---")
    for i, r in enumerate(records, start=1):
        print(f"{i}. {r[1]} (ID:{r[0]}) GPA:{r[2]}")

# ---------------- Teacher ----------------
def add_teacher(db):
    tid = input("Teacher ID: ")
    name = input("Name: ")
    subject = input("Subject: ")

    db["teachers"][tid] = {"name": name, "subject": subject}
    save_db(db)
    print("Teacher added.")

def view_teachers(db):
    print("\n--- Teachers ---")
    for t in db["teachers"].values():
        print(t["name"], "-", t["subject"])

# ---------------- Menu ----------------
def main():
    db = load_db()

    while True:
        print("\n====== SCHOOL MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Marks")
        print("4. Mark Attendance")
        print("5. Student Report")
        print("6. Rank Students")
        print("7. View Teachers")
        print("8. Exit")

        ch = input("Select: ")

        if ch == "1": add_student(db)
        elif ch == "2": add_teacher(db)
        elif ch == "3": add_marks(db)
        elif ch == "4": mark_attendance(db)
        elif ch == "5": student_report(db)
        elif ch == "6": rank_students(db)
        elif ch == "7": view_teachers(db)
        elif ch == "8": break
        else: print("Invalid choice")

main()
