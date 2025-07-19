document.addEventListener('DOMContentLoaded', function() {
    const textElement = document.getElementById('typewriter-text');
    const text = "Welcome to HouseWise! 👌"; // Text to type
    const typingSpeed = 100; // Speed of typing (ms per character)
    const deletingSpeed = 100; // Speed of deleting (ms per character)
    const delayBeforeDeleting = 1000; // Delay before starting to delete (in ms)
    const delayBeforeStarting = 500; // Initial delay before typing starts (in ms)
    
    let index = 0;
    let isDeleting = false;

    function typeWriter() {
        if (isDeleting) {
            if (index > 0) {
                textElement.textContent = text.substring(0, index - 1);
                index--;
                setTimeout(typeWriter, deletingSpeed);
            } else {
                isDeleting = false;
                setTimeout(typeWriter, delayBeforeDeleting);
            }
        } else {
            if (index < text.length) {
                textElement.textContent = text.substring(0, index + 1);
                index++;
                setTimeout(typeWriter, typingSpeed);
            } else {
                isDeleting = true;
                setTimeout(typeWriter, delayBeforeDeleting);
            }
        }
    }

    setTimeout(typeWriter, delayBeforeStarting); // Start typing after a delay
});
