let darkMode = false;

function toggleDarkMode() {
    darkMode =!darkMode;
    document.body.classList.toggle("dark-mode");
}

function download(){
    // Get the URL input value
    var url = document.getElementById("url").value;

    // Check if the URL input field is empty
    if (url.trim() === "") {
        alert("Invalid URL, please enter a valid URL.");
        return;
    }

    // Create a new FormData object to hold form data
    var formData = new FormData();

    // Add the URL data to the FormData object
    formData.append('url', url);

    // Send a POST request to the Flask endpoint to start the download
    fetch('/download', {
        method: 'POST',
        body: formData
        })
        .then(response => {
            if (response.ok) {
                // If download successful, display an alert message
                alert("Download successful!");
            } else {
                // If download failed, display an error alert message
                alert("Download failed!");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            // If an error occurred, display an error alert message
            alert("An error occurred while downloading.");
        });
}