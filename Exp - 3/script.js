var users = [
    { username: "admin", password: "admin123" },
    { username: "user", password: "user123" }
];



document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    var isValid = users.some(function(user) {
        return user.username === username && user.password === password;
    });

    if (isValid) {
        document.getElementById("response").innerText = "Login successful!";
        document.getElementById("response").className = "success";
    } else {
        document.getElementById("response").innerText = "Unauthorized";
        document.getElementById("response").className = "error";
    }
});

document.getElementById("force401Error").addEventListener("click", function() {
    fetch("/error/401", {
        method: "GET"
    }).then(function(response) {
        if (response.status === 401) {
            document.getElementById("response").innerText = "Unauthorized";
            document.getElementById("response").className = "error";
        }
    });
});

document.getElementById("force403Error").addEventListener("click", function() {
    fetch("/error/403", {
        method: "GET"
    }).then(function(response) {
        if (response.status === 403) {
            document.getElementById("response").innerText = "Forbidden";
            document.getElementById("response").className = "error";
        }
    });
});

document.getElementById("force404Error").addEventListener("click", function() {
    fetch("/error/404", {
        method: "GET"
    }).then(function(response) {
        if (response.status === 404) {
            document.getElementById("response").innerText = "Not Found";
            document.getElementById("response").className = "error";
        }
    });
});

document.getElementById("force500Error").addEventListener("click", function() {
    fetch("/error/500", {
        method: "GET"
    }).then(function(response) {
        if (response.status === 500) {
            document.getElementById("response").innerText = "Internal Server Error";
            document.getElementById("response").className = "error";
        }
    });
});