/* ============================================================
   NH Ivory Home Sdn. Bhd. — form.js
   Borang ringkas (nama, telefon, lokasi)
   → hantar email + salinan CC → sambung ke WhatsApp
   ============================================================ */

(function () {
  "use strict";

  var CONFIG = window.NH_CONFIG || {};

  /* ---------- Utiliti ---------- */
  function decode(value) {
    if (!value) return "";
    try { return atob(value); } catch (e) { return value; }
  }

  function formEndpoint() {
    if (CONFIG.formEndpointB64) return decode(CONFIG.formEndpointB64);
    return CONFIG.formEndpoint || "";
  }

  function formCc() {
    if (CONFIG.formCcB64) return decode(CONFIG.formCcB64);
    return CONFIG.formCc || "";
  }

  function normalisePhone(raw) {
    var digits = String(raw || "").replace(/[^0-9]/g, "");
    if (digits.indexOf("0") === 0) digits = "60" + digits.slice(1);
    if (digits.indexOf("60") !== 0) digits = "60" + digits;
    return digits;
  }

  function getUtm() {
    var params = new URLSearchParams(window.location.search);
    var keys = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "fbclid", "gclid"];
    var utm = {};
    keys.forEach(function (k) {
      var v = params.get(k);
      if (v) utm[k] = v;
    });
    return utm;
  }

  function fieldValue(form, name) {
    var el = form.elements[name];
    if (!el || el.value === undefined) return "";
    return String(el.value).trim();
  }

  function setError(form, name, message) {
    var input = form.elements[name];
    var slot = form.querySelector('[data-error-for="' + name + '"]');
    if (slot) slot.textContent = message || "";
    if (input && input.closest) {
      var wrap = input.closest(".field");
      if (wrap) wrap.classList.toggle("invalid", Boolean(message));
    }
  }

  function clearErrors(form) {
    form.querySelectorAll(".error").forEach(function (el) { el.textContent = ""; });
    form.querySelectorAll(".field.invalid").forEach(function (el) { el.classList.remove("invalid"); });
    var status = form.querySelector(".form-status");
    if (status) { status.textContent = ""; status.className = "form-status"; }
  }

  /* ---------- Validasi ---------- */
  function validate(form) {
    clearErrors(form);
    var ok = true;
    var firstInvalid = null;

    function fail(name, message) {
      setError(form, name, message);
      ok = false;
      if (!firstInvalid) firstInvalid = form.elements[name];
    }

    if (fieldValue(form, "nama").length < 3) {
      fail("nama", "Sila masukkan nama penuh anda.");
    }

    var phone = normalisePhone(fieldValue(form, "telefon"));
    if (!/^60[0-9]{8,11}$/.test(phone)) {
      fail("telefon", "Sila masukkan nombor WhatsApp yang sah.");
    }

    if (fieldValue(form, "lokasi").length < 3) {
      fail("lokasi", "Sila masukkan lokasi tanah anda.");
    }

    if (firstInvalid && firstInvalid.focus) {
      try { firstInvalid.focus({ preventScroll: true }); } catch (e) { /* senyap */ }
      if (firstInvalid.scrollIntoView) {
        firstInvalid.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    }
    return ok;
  }

  /* ---------- WhatsApp ---------- */
  function buildWhatsAppUrl(lead) {
    var phone = normalisePhone(CONFIG.whatsapp);
    var lines = [
      "Hai NH Ivory Home, saya ingin konsultasi percuma untuk bina rumah atas tanah sendiri.",
      "",
      "Nama: " + lead.nama,
      "No. WhatsApp: " + lead.telefon,
      "Lokasi tanah: " + lead.lokasi
    ];
    return "https://wa.me/" + phone + "?text=" + encodeURIComponent(lines.join("\n"));
  }

  /* ---------- Hantar email (FormSubmit) ---------- */
  function sendEmail(lead) {
    var endpoint = formEndpoint();
    if (!endpoint || endpoint.indexOf("{{") !== -1) return Promise.resolve();

    var body = {
      _subject: "Lead Baharu Laman Web: " + lead.nama + " (" + lead.lokasi + ")",
      _template: "table",
      _captcha: "false",
      Nama: lead.nama,
      "No. WhatsApp": lead.telefon,
      "Lokasi Tanah": lead.lokasi,
      Masa: lead.masa,
      Sumber: lead.sumber,
      Rujukan: lead.rujukan,
      UTM: JSON.stringify(lead.utm)
    };
    var cc = formCc();
    if (cc && cc.indexOf("{{") === -1) body._cc = cc;

    return fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(body)
    }).catch(function () { /* senyap — WhatsApp tetap diteruskan */ });
  }

  /* ---------- Hantar ke Google Sheets (pilihan) ---------- */
  function sendToSheets(lead) {
    var url = CONFIG.appsScriptUrl;
    if (!url || url.indexOf("{{") !== -1) return Promise.resolve();
    return fetch(url, {
      method: "POST",
      mode: "no-cors",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(lead)
    }).catch(function () { /* senyap */ });
  }

  /* ---------- Kendali borang ---------- */
  function setupForm(form) {
    var status = form.querySelector(".form-status");
    var submitBtn = form.querySelector('button[type="submit"]');

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      if (fieldValue(form, "website")) return; /* honeypot */

      if (!validate(form)) {
        if (status) {
          status.textContent = "Sila semak medan yang bertanda merah.";
          status.className = "form-status err";
        }
        return;
      }

      var lead = {
        nama: fieldValue(form, "nama"),
        telefon: fieldValue(form, "telefon"),
        lokasi: fieldValue(form, "lokasi"),
        sumber: window.location.href,
        rujukan: document.referrer || "",
        masa: new Date().toISOString(),
        utm: getUtm()
      };

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Menghantar...";
      }
      if (status) { status.textContent = ""; status.className = "form-status"; }

      window.nhTrack && window.nhTrack("Lead", {
        content_name: "Borang Konsultasi",
        value: 1,
        currency: "MYR"
      });

      var waUrl = buildWhatsAppUrl(lead);

      var jobs = [sendEmail(lead), sendToSheets(lead)];
      var timeout = new Promise(function (resolve) { setTimeout(resolve, 2500); });

      Promise.race([
        Promise.all(jobs).catch(function () { return null; }),
        timeout
      ]).then(function () {
        window.location.href = waUrl;
      });
    });

    form.addEventListener("input", function (e) {
      if (e.target && e.target.name) setError(form, e.target.name, "");
    });
  }

  ["leadForm", "quickForm"].forEach(function (id) {
    var form = document.getElementById(id);
    if (form) setupForm(form);
  });
})();
