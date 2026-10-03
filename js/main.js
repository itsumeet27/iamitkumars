(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  var filters = document.querySelector(".filters");
  var pubs = document.querySelectorAll(".pub");
  if (filters && pubs.length) {
    filters.addEventListener("click", function (event) {
      var button = event.target.closest("button");
      if (!button) return;
      filters.querySelectorAll("button").forEach(function (item) {
        item.setAttribute("aria-pressed", item === button ? "true" : "false");
      });
      var year = button.dataset.year;
      pubs.forEach(function (pub) {
        var show = year === "all" || pub.dataset.year === year;
        pub.classList.toggle("hidden", !show);
      });
    });
  }

  var copy = document.querySelector("[data-copy-email]");
  if (copy) {
    copy.addEventListener("click", function () {
      var email = copy.dataset.copyEmail;
      var note = document.querySelector("[data-copy-note]");
      function done(message) {
        if (note) note.textContent = message;
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(email).then(function () {
          done("Email copied.");
        }).catch(function () {
          done(email);
        });
      } else {
        done(email);
      }
    });
  }

  var form = document.querySelector("#contact-form");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var note = form.querySelector(".form-note");
      var name = form.name.value.trim();
      var email = form.email.value.trim();
      var message = form.message.value.trim();
      if (!name || !email || !message) {
        if (note) note.textContent = "Please fill in your name, email, and message.";
        return;
      }
      var subject = encodeURIComponent("Website enquiry from " + name);
      var body = encodeURIComponent(message + "\n\n— " + name + "\n" + email);
      window.location.href = "mailto:iamitkumars@gmail.com?subject=" + subject + "&body=" + body;
      if (note) note.textContent = "Your email app should open with this message addressed to Dr. Sharma.";
    });
  }
})();
