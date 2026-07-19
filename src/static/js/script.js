const urlInput = document.getElementById("url");
const folderInput = document.getElementById("folder");
const cloneButton = document.getElementById("cloneButton");
const status = document.getElementById("status");


cloneButton.addEventListener("click", async () => {

    const repoUrl = urlInput.value.trim();
    const folder = folderInput.value.trim();


    if (!repoUrl) {
        alert("Enter GitHub repository URL");
        return;
    }


    if (!folder) {
        alert("Enter destination folder");
        return;
    }


    status.textContent = "Deploying...";


    try {

        const response = await fetch("/deploy", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                url: repoUrl,
                folder: folder
            })
        });


        const data = await response.json();


        if (response.ok) {
            status.textContent = data.message;
        } else {
            status.textContent =
                data.message || "Deployment failed";
        }


    } catch(error) {

        console.error(error);

        status.textContent =
            "Server error";
    }

});


console.log(urlInput);
console.log(folderInput);
console.log(cloneButton);
console.log(status);