document.addEventListener("DOMContentLoaded", function () {
  const btn = document.createElement("button");
  btn.innerText = "Show Email";
  btn.classList.add("btn", "btn-primary", "mt-3", "mx-4");
  document.body.appendChild(btn);

  btn.addEventListener("click", function () {
    window.location.href = "mailto:awang27@nd.edu";
  });
});