# User Authentication System — Documentation

## Overview

This Django authentication system supports:

- User registration

- Login

- Logout

- Profile viewing and editing

It uses Django’s built-in authentication and custom forms.

| Feature  | URL          | Description                             |
| -------- | ------------ | --------------------------------------- |
| Register | `/register/` | Create a new user account               |
| Login    | `/login/`    | Authenticate and log in                 |
| Logout   | `/logout/`   | Log out securely                        |
| Profile  | `/profile/`  | View and update profile (auth required) |

## Testing Instructions

### 1. Register a new user

    Navigate to /register/

    Fill in username, email, password

    Submit

### 2. Login

    Go to /login/

    Enter credentials

### 3. Access Profile

    Go to /profile/

    Update email/username

    Save changes

### 4. Logout

    Visit /logout/