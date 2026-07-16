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


    try {

        const response = await fetch("/clone", {
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

        status.textContent = data.message;


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