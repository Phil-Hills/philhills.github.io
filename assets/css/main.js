// Theme toggle + persistence
document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("theme-toggle");

    // Load stored theme
    const stored = localStorage.getItem("theme");
    if (stored === "dark") {
        document.body.classList.add("dark");
    }

    if (toggle) {
        toggle.addEventListener("click", () => {
            document.body.classList.toggle("dark");
            const isDark = document.body.classList.contains("dark");
            localStorage.setItem("theme", isDark ? "dark" : "light");
        });
    }

    // Fade-in animation for visible elements
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("fade-in");
            }
        });
    });

    const fadeTargets = document.querySelectorAll(".card, .hero-inner, .page h2, .page h3");
    fadeTargets.forEach(el => {
        el.classList.add("fade-target");
        observer.observe(el);
    });
});
