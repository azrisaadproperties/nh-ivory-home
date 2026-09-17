/**
 * ============================================================
 * NH Ivory Home Sdn. Bhd. — Google Apps Script (simpan lead)
 * ============================================================
 *
 * CARA PASANG:
 * 1. Buka https://sheets.google.com dan cipta Google Sheet baru.
 *    Namakan tab pertama: Lead
 * 2. Menu: Extensions > Apps Script
 * 3. Padam kod asal, tampal SEMUA kod fail ini, kemudian Save.
 * 4. Klik Deploy > New deployment > pilih jenis "Web app".
 *      - Description   : NH Lead Endpoint
 *      - Execute as    : Me
 *      - Who has access: Anyone
 *    Klik Deploy dan benarkan akses (Authorize).
 * 5. Salin URL "Web app" (berakhir dengan /exec).
 * 6. Tampal URL tersebut ke dalam index.html:
 *      appsScriptUrl: "https://script.google.com/macros/s/xxxx/exec"
 * 7. Setiap kali anda ubah kod ini, perlu Deploy > Manage deployments
 *    > Edit > Version: New version > Deploy.
 */

var SHEET_NAME = "Lead";
var NOTIFY_EMAIL = "azrisaadproperties@gmail.com"; // kosongkan "" jika tak mahu email

var HEADERS = [
  "Masa",
  "Nama",
  "No. WhatsApp",
  "Lokasi Tanah",
  "Sumber",
  "Rujukan",
  "utm_source",
  "utm_medium",
  "utm_campaign",
  "utm_content",
  "utm_term",
  "fbclid",
  "gclid"
];

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    var data = {};
    if (e && e.postData && e.postData.contents) {
      data = JSON.parse(e.postData.contents);
    }

    var sheet = getSheet();
    var utm = data.utm || {};

    sheet.appendRow([
      new Date(),
      data.nama || "",
      data.telefon || "",
      data.lokasi || "",
      data.sumber || "",
      data.rujukan || "",
      utm.utm_source || "",
      utm.utm_medium || "",
      utm.utm_campaign || "",
      utm.utm_content || "",
      utm.utm_term || "",
      utm.fbclid || "",
      utm.gclid || ""
    ]);

    if (NOTIFY_EMAIL && NOTIFY_EMAIL.indexOf("{{") === -1) {
      MailApp.sendEmail({
        to: NOTIFY_EMAIL,
        cc: "azrimdsaad@gmail.com",
        subject: "Lead Baru: " + (data.nama || "Tanpa Nama") + " (" + (data.lokasi || "-") + ")",
        body:
          "Lead baru dari laman web:\n\n" +
          "Nama: " + (data.nama || "-") + "\n" +
          "WhatsApp: " + (data.telefon || "-") + "\n" +
          "Lokasi tanah: " + (data.lokasi || "-") + "\n\n" +
          "Sumber: " + (data.sumber || "-")
      });
    }

    return ContentService
      .createTextOutput(JSON.stringify({ status: "ok" }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return ContentService
    .createTextOutput(JSON.stringify({ status: "ok", message: "NH Ivory Home lead endpoint aktif." }))
    .setMimeType(ContentService.MimeType.JSON);
}

function getSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.getRange(1, 1, 1, HEADERS.length)
      .setFontWeight("bold")
      .setBackground("#C8102E")
      .setFontColor("#FFFFFF");
    sheet.setFrozenRows(1);
  }
  return sheet;
}
