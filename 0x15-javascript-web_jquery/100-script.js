<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
    <script>
      document.addEventListener("DOMContentLoaded", function () {
        const headerElement = document.querySelector("header.my_header");
        if (headerElement) {
          headerElement.style.color = "#FF0000";
        }
      });
    </script>
  </head>
  <body>
    <header class="my_header">
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

