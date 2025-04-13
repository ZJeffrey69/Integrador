function showForm(formType) 
{
    document.getElementById("login-form").style.display = formType === "login" ? "block" : "none";
    document.getElementById("register-form").style.display = formType === "register" ? "block" : "none";
    document.getElementById("login-tab").classList.toggle("active", formType === "login");
    document.getElementById("register-tab").classList.toggle("active", formType === "register");
}