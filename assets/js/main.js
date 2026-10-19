(function () {
  "use strict";

  var doc = document.documentElement;
  doc.classList.add("js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var WHATSAPP = "27643953029";
  var STORE_KEY = "bb-order-v1";
  // Boxes that count toward the bridal party special (buy 3 matching, 4th free).
  var SPECIAL = ["bridesmaid", "groomsmen"];

  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Header background and the mobile bar both switch on once the hero leaves view.
  var header = document.querySelector("[data-header]");
  var bar = document.querySelector("[data-mobile-bar]");
  var hero = document.querySelector(".hero");
  if (hero && "IntersectionObserver" in window) {
    var sentinel = document.createElement("div");
    sentinel.style.cssText = "position:absolute;top:0;left:0;width:1px;height:60px;pointer-events:none";
    hero.appendChild(sentinel);
    new IntersectionObserver(function (entries) {
      header.classList.toggle("is-scrolled", !entries[0].isIntersecting);
    }).observe(sentinel);
    new IntersectionObserver(function (entries) {
      if (bar) bar.classList.toggle("is-visible", !entries[0].isIntersecting);
    }, { threshold: 0.2 }).observe(hero);
  }

  // Mobile nav
  var toggle = document.querySelector("[data-menu-toggle]");
  var mobileNav = document.querySelector("[data-mobile-nav]");
  function setNav(open) {
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    toggle.innerHTML = open ? '<i class="ph ph-x" aria-hidden="true"></i>' : '<i class="ph ph-list" aria-hidden="true"></i>';
    mobileNav.hidden = !open;
    if (open) header.classList.add("is-scrolled");
  }
  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () { setNav(toggle.getAttribute("aria-expanded") !== "true"); });
    mobileNav.addEventListener("click", function (e) { if (e.target.closest("a")) setNav(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") { setNav(false); toggle.focus(); }
    });
  }

  // Scroll reveal, staggered within each parent.
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var groups = new Map();
    reveals.forEach(function (el) {
      var p = el.parentElement;
      var i = groups.get(p) || 0;
      el.style.setProperty("--stagger", Math.min(i, 5) * 70 + "ms");
      groups.set(p, i + 1);
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-in"); io.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }

  // Extras row arrows
  var row = document.querySelector("[data-row]");
  document.querySelectorAll("[data-scroll-row]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (!row) return;
      var card = row.querySelector(".extra");
      var step = card ? card.getBoundingClientRect().width + 18 : 280;
      row.scrollBy({ left: step * Number(btn.dataset.scrollRow), behavior: reduceMotion ? "auto" : "smooth" });
    });
  });

  /* ---------- Order basket ---------- */

  var catalog = {};
  document.querySelectorAll("[data-item]").forEach(function (el) {
    catalog[el.dataset.item] = { name: el.dataset.name, af: el.dataset.af || "", img: el.dataset.img || "", icon: el.dataset.icon || "" };
  });

  var order = {};
  try {
    var saved = JSON.parse(localStorage.getItem(STORE_KEY) || "{}");
    Object.keys(saved).forEach(function (id) { if (catalog[id] && saved[id] > 0) order[id] = Math.min(99, saved[id] | 0); });
  } catch (err) { order = {}; }

  function save() {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(order)); } catch (err) { /* private mode: keep it in memory */ }
  }

  function total() {
    return Object.keys(order).reduce(function (n, id) { return n + order[id]; }, 0);
  }

  var summary = document.querySelector("[data-summary]");
  var empty = document.querySelector("[data-empty]");
  var specialNote = document.querySelector("[data-special-note]");
  var summaryError = document.querySelector("[data-summary-error]");

  function render(bumpCount) {
    var n = total();
    document.querySelectorAll("[data-count]").forEach(function (el) {
      el.textContent = n;
      if (bumpCount && !reduceMotion) { el.classList.remove("bump"); void el.offsetWidth; el.classList.add("bump"); }
    });
    document.querySelectorAll("[data-count-text]").forEach(function (el) { el.textContent = n; });

    document.querySelectorAll("[data-add]").forEach(function (btn) {
      var q = order[btn.dataset.add] || 0;
      var label = btn.querySelector("span");
      var icon = btn.querySelector("i");
      var short = btn.closest(".extra");
      btn.setAttribute("aria-pressed", String(q > 0));
      label.textContent = q > 0 ? (short ? "Added (" + q + ")" : "Added (" + q + "), add another") : (short ? "Add" : "Add to order");
      icon.className = q > 0 ? "ph ph-check" : "ph ph-plus";
    });

    if (!summary) return;
    summary.innerHTML = "";
    Object.keys(order).forEach(function (id) {
      var item = catalog[id];
      var li = document.createElement("li");
      li.className = "summary-item";
      var thumb = item.img
        ? '<img src="' + item.img + '" alt="" width="56" height="56" loading="lazy">'
        : '<span class="thumb-icon"><i class="ph ' + item.icon + '" aria-hidden="true"></i></span>';
      li.innerHTML = thumb +
        '<div><strong></strong>' + (item.af ? "<small></small>" : "") + "</div>" +
        '<div class="stepper" role="group"><button type="button" data-step="-1"><i class="ph ph-minus" aria-hidden="true"></i></button>' +
        '<output aria-live="polite"></output><button type="button" data-step="1"><i class="ph ph-plus" aria-hidden="true"></i></button></div>';
      li.querySelector("strong").textContent = item.name;
      if (item.af) li.querySelector("small").textContent = item.af;
      li.querySelector("output").textContent = order[id];
      li.querySelector(".stepper").setAttribute("aria-label", "Quantity of " + item.name);
      li.querySelector('[data-step="-1"]').setAttribute("aria-label", order[id] > 1 ? "One less " + item.name : "Remove " + item.name);
      li.querySelector('[data-step="1"]').setAttribute("aria-label", "One more " + item.name);
      li.dataset.id = id;
      summary.appendChild(li);
    });
    empty.hidden = n > 0;
    specialNote.hidden = !SPECIAL.some(function (id) { return (order[id] || 0) >= 4; });
    if (n > 0) summaryError.hidden = true;
  }

  var toast = document.querySelector("[data-toast]");
  var toastText = document.querySelector("[data-toast-text]");
  var toastTimer;
  function showToast(msg) {
    if (!toast) return;
    toastText.textContent = msg;
    toast.classList.add("is-on");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove("is-on"); }, 3200);
  }
  if (toast) toast.querySelector("a").addEventListener("click", function () { toast.classList.remove("is-on"); });

  document.addEventListener("click", function (e) {
    var add = e.target.closest("[data-add]");
    if (add) {
      var id = add.dataset.add;
      order[id] = Math.min(99, (order[id] || 0) + 1);
      save(); render(true);
      showToast(catalog[id].name + " added to your order");
      return;
    }
    var step = e.target.closest("[data-step]");
    if (step) {
      var li = step.closest(".summary-item");
      var sid = li.dataset.id;
      var next = (order[sid] || 0) + Number(step.dataset.step);
      if (next <= 0) delete order[sid]; else order[sid] = Math.min(99, next);
      save(); render(false);
      var again = summary.querySelector('[data-id="' + sid + '"] [data-step="' + step.dataset.step + '"]');
      (again || summary.querySelector("[data-step]") || document.querySelector("#summary-title")).focus({ preventScroll: true });
    }
  });

  render(false);

  /* ---------- Order form: validate, then open WhatsApp with the order written out ---------- */

  var form = document.querySelector("[data-order-form]");
  if (form) {
    var dateInput = form.querySelector("#o-date");
    if (dateInput) dateInput.min = new Date().toISOString().slice(0, 10);

    function setInvalid(input, bad) {
      input.closest(".field").classList.toggle("is-invalid", bad);
      input.setAttribute("aria-invalid", String(bad));
      var err = input.closest(".field").querySelector(".error");
      if (err) {
        if (!err.id) err.id = input.id + "-err";
        var ids = (input.getAttribute("aria-describedby") || "").split(" ").filter(function (x) { return x && x !== err.id; });
        if (bad) ids.push(err.id);
        if (ids.length) input.setAttribute("aria-describedby", ids.join(" ")); else input.removeAttribute("aria-describedby");
      }
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var first = null;
      form.querySelectorAll("[required]").forEach(function (input) {
        var bad = input.value.trim() === "";
        setInvalid(input, bad);
        if (bad && !first) first = input;
      });
      var d = form.elements;
      var nothing = total() === 0 && d.notes.value.trim() === "";
      summaryError.hidden = !nothing;
      if (first) { first.focus(); return; }
      if (nothing) { d.notes.focus(); return; }

      var lines = ["Hi Boxed and Blushing! I'd like to order:", ""];
      Object.keys(order).forEach(function (id) {
        var item = catalog[id];
        lines.push("- " + order[id] + " x " + item.name + (item.af ? " (" + item.af + ")" : ""));
      });
      if (total() === 0) lines.push("- A custom box (see my notes)");
      if (d.names.value.trim()) {
        lines.push("", "Names to print:");
        d.names.value.trim().split(/\n+/).forEach(function (n) { if (n.trim()) lines.push(n.trim()); });
      }
      lines.push("");
      if (d.theme.value.trim()) lines.push("Theme and colours: " + d.theme.value.trim());
      if (d.date.value) {
        var when = d.date.value;
        try {
          when = new Date(d.date.value + "T12:00:00").toLocaleDateString("en-ZA", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
        } catch (err) { /* keep ISO date */ }
        lines.push("Needed by: " + when);
      }
      lines.push("Deliver to: " + d.town.value.trim());
      if (d.notes.value.trim()) lines.push("Notes: " + d.notes.value.trim());
      lines.push("", "Name: " + d.name.value.trim());

      window.open("https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(lines.join("\n")), "_blank", "noopener");
    });

    form.addEventListener("input", function (e) {
      var field = e.target.closest(".field");
      if (field && field.classList.contains("is-invalid") && e.target.value.trim() !== "") setInvalid(e.target, false);
      if (e.target.name === "notes" && e.target.value.trim()) summaryError.hidden = true;
    });
  }

  /* ---------- Gallery ---------- */

  var gallery = document.querySelector("[data-gallery]");
  var more = document.querySelector("[data-gallery-more]");
  if (more) {
    more.addEventListener("click", function () {
      var extra = gallery.querySelectorAll("[data-extra]");
      extra.forEach(function (b) { b.hidden = false; });
      more.parentElement.remove();
      if (extra[0]) extra[0].focus();
    });
  }

  var lb = document.querySelector("[data-lightbox]");
  if (gallery && lb && typeof lb.showModal === "function") {
    var lbImg = lb.querySelector("[data-lb-img]");
    var lbCount = lb.querySelector("[data-lb-count]");
    var current = 0;
    var opener = null;
    function shots() { return Array.prototype.filter.call(gallery.querySelectorAll("button"), function (b) { return !b.hidden; }); }
    function show(i) {
      var list = shots();
      current = (i + list.length) % list.length;
      var b = list[current];
      var img = b.querySelector("img");
      lbImg.src = b.dataset.full;
      lbImg.alt = img.alt;
      lbCount.textContent = (current + 1) + " of " + list.length;
    }
    gallery.addEventListener("click", function (e) {
      var b = e.target.closest("button");
      if (!b) return;
      opener = b;
      show(shots().indexOf(b));
      lb.showModal();
    });
    lb.addEventListener("click", function (e) {
      if (e.target === lb) { lb.close(); return; }
      var st = e.target.closest("[data-lb-step]");
      if (st) show(current + Number(st.dataset.lbStep));
      if (e.target.closest("[data-lb-close]")) lb.close();
    });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") show(current + 1);
      if (e.key === "ArrowLeft") show(current - 1);
    });
    var touchX = null;
    lb.addEventListener("touchstart", function (e) { touchX = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (touchX === null) return;
      var dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
      touchX = null;
    });
    lb.addEventListener("close", function () { lbImg.removeAttribute("src"); if (opener) opener.focus(); });
  } else if (gallery) {
    gallery.addEventListener("click", function (e) {
      var b = e.target.closest("button");
      if (b) window.open(b.dataset.full, "_blank");
    });
  }
})();
