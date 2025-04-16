[app]

# (str) Title of your application
title = Book Listing App

# (str) Package name (e.g., com.mycompany.myapp)
package.name = booklistingapp

# (str) Package domain (use your domain name to ensure uniqueness)
package.domain = org.yourdomain

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = kivy, firebase-admin, requests

# (list) Application source files to include
source.include_exts = py,png,jpg,kv

# (list) Application source directories to include (optional)
# source.include_patterns = assets/*

# (list) Android permissions
android.permissions = INTERNET

[buildozer]

# (bool) Use the default buildozer toolchain
use_pip = True
