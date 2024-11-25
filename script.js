document.getElementById("contactForm").addEventListener("submit", function (e) {
    e.preventDefault(); // Voorkom dat de pagina herlaadt
    const name = document.getElementById("name").value;
    const message = `Thank you, ${name}, for reaching out!`;
    document.getElementById("formMessage").innerText = message;
    this.reset(); // Reset het formulier
  });
  