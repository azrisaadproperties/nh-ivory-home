/* ============================================================
   NH Ivory Home Sdn. Bhd. — main.js
   Header, menu, sticky CTA, WhatsApp links, kalkulator
   ============================================================ */

(function () {
  "use strict";

  var CONFIG = window.NH_CONFIG || {};

  /* ---------- Helper tracking ---------- */
  window.nhTrack = function (eventName, params) {
    try {
      if (typeof window.fbq === "function") window.fbq("track", eventName, params || {});
      if (typeof window.gtag === "function") {
        window.gtag("event", eventName.toLowerCase(), params || {});
      }
    } catch (e) { /* senyap */ }
  };

  function normalisePhone(raw) {
    var digits = String(raw || "").replace(/[^0-9]/g, "");
    if (digits.indexOf("0") === 0) digits = "60" + digits.slice(1);
    return digits;
  }

  /* ---------- WhatsApp links ---------- */
  function buildWhatsAppLinks() {
    var phone = normalisePhone(CONFIG.whatsapp);
    if (!phone) return;
    var text = encodeURIComponent(
      "Hai NH Ivory Home, saya berminat untuk bina rumah atas tanah sendiri. Boleh saya dapatkan konsultasi percuma?"
    );
    var href = "https://wa.me/" + phone + "?text=" + text;
    document.querySelectorAll(".js-wa-link").forEach(function (el) {
      el.setAttribute("href", href);
      el.setAttribute("target", "_blank");
      el.setAttribute("rel", "noopener");
    });
  }

  /* ---------- Menu mudah alih ---------- */
  function initMobileNav() {
    var toggle = document.getElementById("navToggle");
    var nav = document.querySelector(".nav");
    if (!toggle || !nav) return;

    var mobile = document.createElement("nav");
    mobile.className = "mobile-nav";
    mobile.setAttribute("aria-label", "Navigasi mudah alih");
    mobile.innerHTML = nav.innerHTML +
      '<a href="#borang" class="btn btn-primary">Sebut Harga Percuma</a>';
    nav.parentNode.insertBefore(mobile, toggle.nextSibling);

    toggle.addEventListener("click", function () {
      var open = mobile.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Tutup menu" : "Buka menu");
    });

    mobile.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        mobile.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------- Header & sticky CTA ---------- */
  function initScrollEffects() {
    var header = document.getElementById("siteHeader");
    var sticky = document.getElementById("stickyCta");
    var form = document.getElementById("borang");
    var ticking = false;

    function update() {
      var y = window.pageYOffset || document.documentElement.scrollTop;
      if (header) header.classList.toggle("scrolled", y > 10);

      if (sticky) {
        var show = y > 500;
        if (form) {
          var rect = form.getBoundingClientRect();
          if (rect.top < window.innerHeight && rect.bottom > 0) show = false;
        }
        sticky.classList.toggle("visible", show);
      }
      ticking = false;
    }

    window.addEventListener("scroll", function () {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }, { passive: true });
    update();
  }

  /* ---------- Kalkulator ansuran ---------- */
  function initCalculator() {
    var kos = document.getElementById("calcKos");
    var deposit = document.getElementById("calcDeposit");
    var kadar = document.getElementById("calcKadar");
    var tempoh = document.getElementById("calcTempoh");
    var out = document.getElementById("calcAnswer");
    if (!kos || !deposit || !kadar || !tempoh || !out) return;

    function formatRM(n) {
      return "RM " + n.toLocaleString("ms-MY", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }

    function calc() {
      var jumlahKos = parseFloat(kos.value) || 0;
      var peratusDeposit = Math.min(Math.max(parseFloat(deposit.value) || 0, 0), 90);
      var kadarTahun = (parseFloat(kadar.value) || 0) / 100;
      var tahun = Math.max(parseFloat(tempoh.value) || 1, 1);

      var pinjaman = jumlahKos * (1 - peratusDeposit / 100);
      var bulan = tahun * 12;
      var faedahBulanan = kadarTahun / 12;

      var ansuran;
      if (faedahBulanan > 0) {
        var faktor = Math.pow(1 + faedahBulanan, bulan);
        ansuran = pinjaman * (faedahBulanan * faktor) / (faktor - 1);
      } else {
        ansuran = pinjaman / bulan;
      }

      out.textContent = isFinite(ansuran) ? formatRM(ansuran) : "RM 0.00";
    }

    [kos, deposit, kadar, tempoh].forEach(function (el) {
      el.addEventListener("input", calc);
      el.addEventListener("change", calc);
    });
    calc();
  }

  /* ---------- CTA tracking ---------- */
  function initCtaTracking() {
    document.querySelectorAll("[data-cta]").forEach(function (el) {
      el.addEventListener("click", function () {
        var label = el.getAttribute("data-cta");
        window.nhTrack(label.indexOf("whatsapp") === 0 ? "Contact" : "InitiateCheckout", {
          content_name: label
        });

        if (el.hasAttribute("data-pakej")) {
          var pakej = document.getElementById("pakejPilihan");
          if (pakej) pakej.value = el.getAttribute("data-pakej");
        }
        if (el.hasAttribute("data-pembayaran")) {
          var nilai = el.getAttribute("data-pembayaran");
          var radio = document.querySelector('input[name="pembayaran"][value="' + nilai + '"]');
          if (radio) radio.checked = true;
        }
      });
    });
  }

  /* ---------- Video testimoni (klik untuk main) ---------- */
  function initVideos() {
    document.querySelectorAll(".video-card").forEach(function (card) {
      var thumb = card.querySelector(".video-thumb");
      var id = card.getAttribute("data-video-id");
      if (!thumb || !id) return;

      thumb.addEventListener("click", function () {
        var iframe = document.createElement("iframe");
        iframe.className = "video-iframe";
        iframe.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0&modestbranding=1";
        iframe.title = thumb.getAttribute("aria-label") || "Video testimoni NH Ivory Home";
        iframe.setAttribute("allow", "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share");
        iframe.setAttribute("allowfullscreen", "");
        iframe.setAttribute("loading", "lazy");
        thumb.replaceWith(iframe);
        window.nhTrack("ViewContent", { content_name: "video-testimoni", content_ids: [id] });
      });
    });
  }

  /* ---------- Widget WhatsApp terapung ---------- */
  function initWaWidget() {
    var widget = document.querySelector(".wa-widget");
    var float = document.getElementById("waFloat");
    var popup = document.getElementById("waPopup");
    var closeBtn = document.getElementById("waPopupClose");
    var label = document.getElementById("waLabel");
    if (!float || !popup) return;

    function openPopup() {
      popup.classList.add("open");
      float.setAttribute("aria-expanded", "true");
      float.classList.add("is-open");
      if (label) label.classList.remove("show");
      var firstInput = popup.querySelector("input");
      if (firstInput) {
        setTimeout(function () { try { firstInput.focus(); } catch (e) { /* senyap */ } }, 250);
      }
      window.nhTrack("Contact", { content_name: "whatsapp-popup" });
    }

    function closePopup() {
      popup.classList.remove("open");
      float.setAttribute("aria-expanded", "false");
      float.classList.remove("is-open");
    }

    float.addEventListener("click", function () {
      if (popup.classList.contains("open")) closePopup();
      else openPopup();
    });

    if (closeBtn) closeBtn.addEventListener("click", closePopup);

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closePopup();
    });

    document.addEventListener("click", function (e) {
      if (!popup.classList.contains("open")) return;
      if (widget && !widget.contains(e.target)) closePopup();
    });

    if (label) {
      setTimeout(function () {
        if (!popup.classList.contains("open")) label.classList.add("show");
      }, 4000);
    }
  }

  /* ---------- Tahun footer ---------- */
  function initYear() {
    var y = document.getElementById("year");
    if (y) y.textContent = new Date().getFullYear();
  }

  document.addEventListener("DOMContentLoaded", function () {
    buildWhatsAppLinks();
    initMobileNav();
    initScrollEffects();
    initCalculator();
    initCtaTracking();
    initVideos();
    initWaWidget();
    initYear();
  });
})();
