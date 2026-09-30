# Vault — a locked folder for your files

Put anything inside. It gets encrypted on the way in, and the password you chose
is the only thing that opens it again.

**[Download the Android app](https://github.com/BrianArfi/lock-my-files/releases/latest)**

This repository exists to host the release download. The source is not published
here.

## What it is

- Make a **vault** and give it a password. Make as many as you like; each one has
  its own.
- Files are encrypted before they are stored. File names are encrypted too.
- A single file can have **its own password**, separate from the vault. Then even
  opening the vault does not open that file.
- The app has **no internet permission at all**, so Android will not let it open
  a network connection. You can check that in the app info screen.

## What it does not do

- **Nobody can reset your password.** There is no account, no email recovery and
  no support desk. Each vault gives you 12 recovery words when you create it;
  lose both those and the password, and the files are gone permanently.
- **Nothing is backed up.** Lose the phone and the vaults go with it.
- **The original file stays where it was.** Adding a file copies it; the original
  remains in your gallery or downloads until you delete it yourself.

## Status

Version 0.1.0, Android only. The encryption is checked against published test
vectors and the whole flow passes an automated end-to-end test, but that test has
only ever run in an iOS simulator — this Android build has not been run on a real
phone. Do not put anything in it that you cannot afford to lose.

Verify your download against the SHA-256 published with the release before
installing it.

## Changelog

What changed in each release is in [CHANGELOG.md](CHANGELOG.md). Each
[release](https://github.com/BrianArfi/lock-my-files/releases) also carries its
own notes and the SHA-256 of its download.
