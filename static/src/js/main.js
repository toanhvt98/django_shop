// switch mode dark-light
document.addEventListener("DOMContentLoaded", function () {
  const modeSwitch = document.getElementById("modeswitched");
  const textMode = document.getElementById("textmode");

  modeSwitch.addEventListener("click", function () {
    const isChecked = modeSwitch.querySelector("input").checked;
    if (isChecked) {
      document.body.classList.add("dark");
      localStorage.setItem("theme", "dark");
      textMode.textContent = "Dark";
    } else {
      document.body.classList.remove("dark");
      localStorage.setItem("theme", "light");
      textMode.textContent = "Light";
    }
  });
});

// check mode dark-light
document.addEventListener("DOMContentLoaded", function () {
  if (!localStorage.getItem("theme")) {
    localStorage.setItem("theme", "light");
  }
  const modeSwitch = document.getElementById("modeswitched");
  const textMode = document.getElementById("textmode");
  const input = modeSwitch.querySelector("input");
  const theme = localStorage.getItem("theme");
  if (theme === "dark") {
    input.checked = true;
    document.body.classList.add("dark");

    textMode.textContent = "Dark";
  } else {
    input.checked = false;
    document.body.classList.remove("dark");

    textMode.textContent = "Light";
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const usernameInput = document.getElementById("login_usernameInput");
  const passwordInput = document.getElementById("login_passwordInput");
  const errorMessage = document.getElementById("login_error_message");

  usernameInput.addEventListener("input", function () {
    errorMessage.textContent = "";
  });
  passwordInput.addEventListener("input", function () {
    errorMessage.textContent = "";
  });
});
