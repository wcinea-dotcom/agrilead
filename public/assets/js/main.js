/* AGRILEAD — small progressive-enhancement script.
   Handles the mobile menu and gentle scroll reveals. */
(function () {
  "use strict";

  /* Flag JS so CSS can safely hide reveal elements only when scripts run */
  document.documentElement.classList.add("js");

  function revealAll(items) {
    for (var i = 0; i < items.length; i++) items[i].classList.add("in");
  }

  /* Mobile navigation */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // Close menu when a link is chosen (mobile)
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* Scroll reveal */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var items = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    revealAll(items);
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: "0px 0px -40px 0px" });
  items.forEach(function (el) { io.observe(el); });

  /* Failsafe: never leave content hidden if the observer never fires */
  window.addEventListener("load", function () {
    setTimeout(function () { revealAll(document.querySelectorAll(".reveal:not(.in)")); }, 1600);
  });
})();
