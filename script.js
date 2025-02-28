function uploadFile() {
    let fileInput = document.getElementById("fileInput");
    let resultText = document.getElementById("result");
    let previewImg = document.getElementById("preview");

    if (fileInput.files.length === 0) {
        alert("Please select an image!");
        return;
    }

    let file = fileInput.files[0];
    let formData = new FormData();
    formData.append("file", file);

    // Show image preview
    let reader = new FileReader();
    reader.onload = function (e) {
        previewImg.src = e.target.result;
        previewImg.style.display = "block";
    };
    reader.readAsDataURL(file);

    // Send file to Flask backend
    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultText.innerText = "Predicted Category: " + data.category;
    })
    .catch(error => {
        console.error("Error:", error);
        resultText.innerText = "Prediction failed!";
    });
}
