const button = document.getElementById("folderButton");
const folderName = document.getElementById("folderName");

button.addEventListener("click", async () => {

    if (!window.showDirectoryPicker) {
        folderName.textContent =
            "Your browser doesn't support folder selection.";
        return;
    }

    try {
        const dir = await window.showDirectoryPicker();
        folderName.textContent = `Selected: ${dir.name}`;
    } catch {
        folderName.textContent = "Folder selection cancelled.";
    }

});

const cloneButton = document.getElementById("cloneButton");

cloneButton.addEventListener("click", async () => {

    const response = await fetch("/clone", {
        method: "POST"
    });

    const data = await response.json();

    alert(data.message);

});