document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const statusMessage = document.getElementById('statusMessage');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form values
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();

        // Simple validation
        if (name === '' || email === '' || message === '') {
            showStatus('Please fill in all fields', 'error');
            return;
        }

        if (!isValidEmail(email)) {
            showStatus('Please enter a valid email address', 'error');
            return;
        }

        // Simulate form submission
        // alert('Sending message...', 'success');
        
        // Simulate an API call
        setTimeout(() => {
            alert('Message sent successfully!', 'success');
            form.reset();
        }, 2000);
    });

    function showStatus(message, type) {
        statusMessage.textContent = message;
        statusMessage.className = type;
    }

    function isValidEmail(email) {
        // Simple email validation regex
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
});