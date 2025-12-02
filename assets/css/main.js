// Smooth fade-in on scroll
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".card, .hero-inner, .page h2");
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("fade-in");
            }
        });
    });
    elements.forEach(el => observer.observe(el));
});
