const paragraphs = document.querySelectorAll('.animated-paragraph');
let currentIndex = 0;

function animateParagraphs() {
    if (currentIndex < paragraphs.length) {
        setTimeout(() => {
            paragraphs[currentIndex].style.opacity = 1; // Make the paragraph visible
            currentIndex++;
            animateParagraphs(); // Move to the next paragraph with a delay
        }, 1800); // Delay before showing the next paragraph
    }
}

animateParagraphs(); // Start showing and animating paragraphs one by one


// Get the current URL
const currentURL = window.location.pathname;

// Select the link based on the current URL and add the "active" class
document.querySelectorAll('nav a').forEach(link => {
    if (link.getAttribute('href') === currentURL) {
        link.classList.add('active');
    }
});
