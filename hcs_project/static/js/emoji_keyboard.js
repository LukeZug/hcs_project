document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to all emoji buttons
    document.querySelectorAll('.emoji-btn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            // Prevent the default form submit behavior
            event.preventDefault();

            // Find the closest .emoji-keyboard and get its data-input-target attribute
            var keyboard = this.closest('.emoji-keyboard');
            var inputSelector = keyboard.getAttribute('data-input-target');

            // Find the associated input box
            var inputBox = document.querySelector(inputSelector);

            // Append the emoji to the input box's value
            inputBox.value += this.textContent;
        });
    });
});