Attendance Tracking System

PROG103 – Structured Programming Assignment

A terminal‑based Python application that helps teachers in Sierra Leone record and monitor student attendance. The system supports **SDG 4 (Quality Education)** by providing clear, actionable data to identify at‑risk students and reduce dropout rates.

== Table of Contents ==

- [Features](#features)
- [Technologies & Principles](#technologies--principles)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Example Output](#example-output)
- [Project Structure](#project-structure)
- [Author](#author)

---

## Features

- Add attendance records with student name, date, and status (`Present`, `Absent`, `Late`)
- Store multiple records during a single session (in memory)
- Generate a detailed summary report:
  - Per‑student totals (Present / Absent / Late)
  - Per‑student attendance percentage
  - Overall class statistics (total present, absent, late records)
  - Overall class attendance rate
- Clean, menu‑driven terminal interface
- Input validation (handles invalid menu choices, data type error, and empty inputs)


## Technologies & Principles

This project strictly follows **structured programming** principles:

| Principle | Implementation |
|-----------|----------------|
| Variables & constants | `STATUS_OPTIONS`, `MENU_EXIT`, `attendance_records` list |
| Data types | `str`, `int`, `float`, `list`, `dict` |
| Error Handling Function | `try-catch`
| Decision structures | `if`/`elif`/`else` (menu selection, status mapping) |
| Iteration | `while` loop (main menu), `for` loops (processing records) |
| Modularity (functions) | `add_attendance()`, `generate_report()`, `main()` |
| Single entry point | `if __name__ == "__main__":` |

**Language:** Python 3


## Requirements

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

## Installation & Setup

1. **Clone the repository** (or download the file):
   ```bash
   git clone https://github.com/rayanmartynt/PROG103_Assignment1_RayanMartinTuray_905005656.git
   cd PROG103_Assignment1_RayanMartinTuray_905005656

2. **Run the program**
   ```bash
   python main.py
       OR
   py main.py
  
## How to Use
   When you run the program, you will see a menu:
   
     ===== ATTENDANCE TRACKING SYSTEM MENU =====
      1. Add Attendance Record
      2. Generate Summary Report
      3. Exit
    
  EXAMPLE Output
   Adding a record

     --- Add New Attendance Record ---
      Student name: Amadu Kamara
      Date (YYYY-MM-DD): 2025-04-25

      Status options:
      1. Present
      2. Absent
      3. Late
      Enter choice (1/2/3): 1
      Attendance record added: Amadu Kamara - 2026-04-27 - Present

  Generating a report

    ========== ATTENDANCE SUMMARY REPORT ==========

    Student: Amadu Kamara
      Present: 1  |  Absent: 0  |  Late: 0
      Attendance Rate: 100.0%
    ---------------------------------------------

    Student: Babatunde Bangura
      Present: 0  |  Absent: 2  |  Late: 0
      Attendance Rate: 0.0%
    ---------------------------------------------

    ====== CLASS TOTAL ======
    Total Present   : 1
    Total Absent    : 2
    Total Late      : 0
    Total Records   : 3
    Overall Attendance Rate: 33.3%

## Project Structure
    PROG103_Assignment1_RayanMartinTuray_905005656/
    ├── main.py                   # Main source code
    └── README.md                 # This file

## Author
    Name: Rayan Martin Turay
    Student ID: 905005656
    Module: PROG103 - Principles Of Structured Programming
    Lecturer: Mr. Amadu Kamara (Amkam)
    Lecturer GitHub: AmaduKamara
    Institution: Limkokwing University of Creative Technology
    GitHub: https://github.com/rayanmartynt
