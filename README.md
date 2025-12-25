Hello folks, here I present a python project that implements basic sign-up and log-in functionality. User credentials are stored in a JSON file, and authentication is handled by validating input against the stored data. Since this is my first project and I am new to programming, I am learning how to build tools that could be useful in real-world applications. I continue to improve this project as I learn new concepts, trying my best to make it more complete and reliable.
## Features (so far)

- Sign-up
  - Requires user email address
  - Validates email format using common providers and domains
  - Username creation with constraints
    - 4–8 characters long
    - Must contain at least one alphabet
    - Allowed special characters: ' . ',' - ',' _ ' 
  - Password creation with constraints
    - 8 characters long
    - Must contain alphabets
    - At least one uppercase letter
    - Must include digits
    - Must include special characters
  - Stores user credentials in a JSON file
- Log-in
  - Requires registered username and password
  - Displays **“ACCESS ALLOWED”** on successful authentication
- “Forgot Password” feature with local OTP generation in the CLI (can be replaced with an API-based OTP service).
