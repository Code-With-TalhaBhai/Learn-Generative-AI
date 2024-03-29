## Hashing

Hashing is a one-way process that scrambles plaintext into a unique code that can't be reverted back into a readable form. The purpose of hashing is to prove the authenticity of data. For example, administrators can check hashed data to ensure the contents haven't been changed while in storage.


## Encryption

Encryption is a two-way process that scrambles plaintext into unreadable ciphertext. The purpose of encryption is to pass the information to another party, who can then use a key to decipher the data.



### Packages to install

1. python-jose
    - `python-jose` is a package to generate and verify the JWT tokens in Python

2. passlib
    - `passlib` is a great Python package to handle password hashes.It supports many secure hashing algorithms and utilities to work with them. The recommended algorithm is `Bcrypt`.
    pip install passlib[bcrypt]

