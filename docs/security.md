# Security and limits

[Back to the README](../README.md)

## Security design, in short

- **Keys come from your password.** The vault password goes through Argon2id to make a key. That key unwraps the vault's master key. The recovery words are a second way to unwrap the same master key.
- **Files are encrypted with XChaCha20-Poly1305**, in 1 MiB chunks. Each file has its own key.
- **No password verifier is stored.** There is nothing on the phone to test a guess against. The only way to test a password is the full key derivation.
- **A per-file password replaces the vault key for that file.** So the vault password and the recovery words do not open it.
- **No backdoor key and no escrow.** Nobody, including the developer, can open a vault without the password or the recovery words.

## What it does not do

- **Nobody can reset your password.** There is no account, no email recovery and no support desk. Lose the password and the recovery words, and the files are gone permanently.
- **Nothing is backed up.** Lose the phone and the vaults go with it. A vault is not a backup.
- **The original file stays where it was.** Adding a file copies it. Delete the original yourself.
- **Video and audio write a temporary copy.** The player needs a real file, so a decrypted copy sits in the app's private storage while it plays. The app deletes it when you close the file, when the vault locks, and at every launch. Photos and text open in memory only.
- **The vault name is not encrypted.** The app has to list vaults before any of them is open. Use a plain name like "Documents".
- **File size and date are not encrypted.** Names and file types are inside the encrypted data. File size and date are stored in the clear.
- **Wrong guesses are not rate-limited in 0.1.0.** Nothing slows down repeated wrong guesses at the passcode or a vault password. Pick a vault password that is long and hard to guess.
