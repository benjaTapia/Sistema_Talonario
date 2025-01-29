// Ejemplo: Mensaje de bienvenida en la consola
console.log("Bienvenido al administrador del Sistema Talonario");

// Ejemplo: Personalización de campos
document.addEventListener("DOMContentLoaded", () => {
    // Cambiar el color de fondo de los campos de texto
    document.querySelectorAll("input[type='text']").forEach(input => {
        input.style.backgroundColor = "#f8f9fa";
    });

    // Notificación en un botón
    const saveButton = document.querySelector(".submit-row input[type='submit']");
    if (saveButton) {
        saveButton.addEventListener("click", () => {
            alert("Guardando los cambios...");
        });
    }
});
