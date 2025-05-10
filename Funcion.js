function showForm(formType) 
{
    document.getElementById("login-form").style.display = formType === "login" ? "block" : "none";
    document.getElementById("register-form").style.display = formType === "register" ? "block" : "none";
    document.getElementById("login-tab").classList.toggle("active", formType === "login");
    document.getElementById("register-tab").classList.toggle("active", formType === "register");
}
    function toggleDropdown() {
        var menu = document.getElementById("crearMenu");
        menu.style.display = menu.style.display === "block" ? "none" : "block";
    }

    window.onclick = function(e) {
        if (!e.target.matches('a[href="#"]')) {
            var dropdown = document.getElementById("crearMenu");
            if (dropdown && dropdown.style.display === "block") {
                dropdown.style.display = "none";
            }
        }
    }