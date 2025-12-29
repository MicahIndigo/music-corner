/**
 * Music Corner - main.js
 * Handles the main JavaScript functionality for the Music Corner website.
 * Provides UI imorovements and interactivity without changing backkend logic.
 */

(function () {
    "use strict";

    // Confirm JS is loaded
    console.log("Music Corner main.js is loaded.");

    // Confirm before deleting posts/comments
    // Add `data-confirm="Are you sure?"` to any delete link/button you want to confirm.
    document.addEventListener("click", function (event) {
        const el = event.target.closest("[data-confirm]");
        if (!el) return;

        const message = el.getAttribute("data-confirm") || "Are you sure?";
        const ok = window.confirm(message);

        if (!ok) {
            event.preventDefault();
            event.stopPropagation();
        }
    });

    // Auto-hide Django messages after 5 seconds
    // Looks for Bootstrap alert boxes: .alert
    window.addEventListener("load", function () {
        const alerts = this.document.wuerySelectorAll(".alert");
        if (!alerts.length) return;

        setTimeout(function () {
            alerts.forEach(function (alertEl) {
                alertEl.style.transition = "opacity 400ms ease";
                alertEl.style.opacity = "0";
                setTimeout(function () {
                    if (alertEl && alertEl.parentNode) {
                        alertEl.parentNode.removeChild(alertEl);
                    }
                }, 450);
            });
        }, 3500);
    });
})();