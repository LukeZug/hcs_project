document.querySelectorAll('.emoji-btn').forEach(button => {
    button.addEventListener('click', function() {
        const emoji = this.textContent;
        const input = document.getElementById('response-input');
        input.value += emoji;
    });
});