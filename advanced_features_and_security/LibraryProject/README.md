# Django Permissions & Groups Setup

## Custom Permissions
Defined in `Book` model:

- can_view
- can_create
- can_edit
- can_delete

## Groups
Created in Django Admin:

### Viewers
- can_view

### Editors
- can_view
- can_create
- can_edit

### Admins
- can_view
- can_create
- can_edit
- can_delete

## Views Protection
Each view uses @permission_required(...) to enforce access.

Users must belong to a group with appropriate permissions.