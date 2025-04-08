document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    // Temporary login logic (replace with backend API later)
    if (username === "admin" && password === "admin123") {
        window.location.href = "admin.html";
    } else if (username === "developer" && password === "dev123") {
        window.location.href = "developer.html";
    } else if (username === "user" && password === "user123") {
        window.location.href = "user.html";
    } else {
        document.getElementById('errorMsg').textContent = "Invalid credentials!";
    }
});
