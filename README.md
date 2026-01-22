# 🎓 Academic Management System
<img width="1717" height="766" alt="image" src="https://github.com/user-attachments/assets/5648be87-9ee1-4e7d-8e5c-e38595fa2482" />

**Final Project – Flask & MySQL**

This project is a **web application developed with Flask and MySQL** for the **comprehensive management of students from different educational institutions**, allowing the administration of institutions, courses, specializations, academic plans, and student enrollment.

---

## 🧠 Overview

The system allows you to:

* Manage **educational institutions**
* Administer **students** and their personal information
* Create and organize **courses** and **specializations**
* Manage **academic plans**
* Enroll students in courses and specializations according to their plan
* Maintain data integrity through controlled cascading deletions

The application follows a **simple MVC architecture**, using Flask as the backend and MySQL as the relational database system.

---

## ⚙️ Technologies Used

* **Python 3**
* **Flask**
* **Flask-MySQLdb**
* **MySQL**
* **HTML / CSS**
* **Jinja2**
* **Bootstrap**

---

## 🧩 Modules & Features

### 🏫 Institutions

* Create, list, edit, and delete institutions
* Each institution can have associated courses and specializations
* Controlled cascading deletion of dependent entities

<img width="1586" height="695" alt="image" src="https://github.com/user-attachments/assets/9618607d-1cb3-4075-8370-c8ab44941e20" />

---

### 📚 Courses

* Create courses associated with an institution
* Assign courses to one or more **academic plans**
* Categorize courses using **categories**
* Edit and delete courses
* View categories associated with each course
<img width="1695" height="638" alt="image" src="https://github.com/user-attachments/assets/addca256-65e1-48e3-8eca-c00a4d4f86b3" />

---

### 🎓 Specializations

* Create specializations per institution
* Assign them to academic plans
* Associate courses with specializations
* Edit and delete specializations
* Manage courses within each specialization
<img width="1633" height="681" alt="image" src="https://github.com/user-attachments/assets/be3f32a2-2fd0-4ba8-b5be-68001b0d2c81" />

---

### 👨‍🎓 Students

* Register students with personal information
* Assign an **academic plan**
* Edit and delete students
* Enroll students in:

  * Courses
  * Specializations
* View and manage enrolled courses and specializations

<img width="1606" height="761" alt="image" src="https://github.com/user-attachments/assets/14f04288-3591-41d5-a9d5-fe19fa7b1f4a" />
<img width="1378" height="877" alt="image" src="https://github.com/user-attachments/assets/44f44991-d028-4ce2-af8e-fd45d1249915" />

---

### 📑 Academic Plans

* Plans determine:

  * Which courses a student can enroll in
  * Which specializations are available
* Enrollment is automatically validated based on the student’s plan

---

## 🔐 Database Configuration

The application uses **MySQL** and connects through `app.py`:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'proyecto'
app.config['MYSQL_PORT'] = 10061
```


---

## 🚀 Running the Project

1. **Clone the repository**

```bash
git clone https://github.com/Geison117/proyecto_final.git
```

2. **Activate the virtual environment**

```bash
Entorno\Scripts\activate   # Windows
```

3. **Install dependencies**

```bash
pip install flask flask-mysqldb
```

4. **Set up the database**

* Import the SQL scripts from the `Base de datos` folder
* Ensure MySQL is running

5. **Run the application**

```bash
python app.py
```

6. **Open in your browser**

```
http://localhost:2900
```

