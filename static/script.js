// Global object to store student records
let students = {};

function openPage(page) {
    let content = "";

    if (page === "addStudent") {
        content = `
            <h2>Add Student</h2>
            <div class="form">
                <input type="text" id="student_id" placeholder="Student ID">
                <input type="text" id="name" placeholder="Name">
                <input type="number" id="age" placeholder="Age">
                <input type="text" id="grade" placeholder="Grade">
                <button onclick="addStudent()">Add</button>
            </div>
        `;
    } else if (page === "searchStudent") {
        content = `
            <h2>Search Student</h2>
            <input type="text" id="search_id" placeholder="Enter Student ID">
            <button onclick="searchStudent()">Search</button>
            <div id="search_result"></div>
        `;
    } else if (page === "updateStudent") {
        content = `
            <h2>Update Student</h2>
            <div class="form">
                <input type="text" id="update_id" placeholder="Student ID">
                <input type="text" id="update_name" placeholder="New Name">
                <input type="number" id="update_age" placeholder="New Age">
                <input type="text" id="update_grade" placeholder="New Grade">
                <button onclick="updateStudent()">Update</button>
            </div>
        `;
    }

    document.getElementById("content").innerHTML = content;
}

// Function to add a student
function addStudent() {
    let id = document.getElementById("student_id").value;
    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;
    let grade = document.getElementById("grade").value;

    if (id && name && age && grade) {
        students[id] = { name, age, grade };
        alert("✅ Student Added Successfully!");
    } else {
        alert("⚠️ Please fill all fields!");
    }
}

// Function to search a student
function searchStudent() {
    let id = document.getElementById("search_id").value;
    let resultDiv = document.getElementById("search_result");

    if (id in students) {
        let student = students[id];
        resultDiv.innerHTML = `<p>ID: ${id}, Name: ${student.name}, Age: ${student.age}, Grade: ${student.grade}</p>`;
        alert("🔍 Student Found!");
    } else {
        resultDiv.innerHTML = "<p>❌ Student Not Found</p>";
        alert("⚠️ Student Not Found!");
    }
}

// Function to update a student
function updateStudent() {
    let id = document.getElementById("update_id").value;
    let newName = document.getElementById("update_name").value;
    let newAge = document.getElementById("update_age").value;
    let newGrade = document.getElementById("update_grade").value;

    if (id in students) {
        students[id] = { name: newName, age: newAge, grade: newGrade };
        alert("✅ Student Updated Successfully!");
    } else {
        alert("⚠️ Student Not Found!");
    }
}


