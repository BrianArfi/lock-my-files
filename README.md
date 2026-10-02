# Lock My Files

**Keep your ID cards, contracts and private photos out of the gallery, locked behind a password only you know.**

For Android users who keep scans of important papers on their phone and want them encrypted, not just hidden behind a PIN screen.

[![Version 0.1.0](https://img.shields.io/badge/version-0.1.0-green.svg)](CHANGELOG.md)
[![Made for Android 7+](https://img.shields.io/badge/made%20for-Android%207%2B-3DDC84.svg)](docs/install.md#requirements)
[![Early build](https://img.shields.io/badge/status-early%20build-orange.svg)](#status)

![Animated illustration: an ID card and a signed rental contract slide into a phone vault called Documents and appear at the top of its list, highlighted, above a passport scan and a bank statement. Below, the storage panel gains two new scrambled .enc file names. Headline: Your private files, locked away.](docs/hero.gif)

**[Download the Android app (APK)](https://github.com/BrianArfi/lock-my-files/releases/latest)**

## The problem

Dina rents a flat. For the contract she scanned her ID card, the signed rental contract and the house certificate the landlord sent her. The scans landed in Downloads and the camera roll, right next to her holiday photos. Then her nephew Sam borrows her phone to play a game.

- **Anyone holding the phone can scroll to them.** Show someone one photo, and they can swipe to the next one: your ID card.
- **The file names give it away.** `KTP_contoh.pdf`, `Kontrak_sewa.pdf`, `Sertifikat_rumah_scan.pdf`: you do not even need to open them to know what they are.
- **Other apps can read them too.** Any app you gave access to your photos and files can list and open those scans.
- **"Hidden" folders are often only hidden.** A PIN screen in front of a folder does not change the files behind it: they are still readable.
- **Sending them to yourself in a chat** only puts another copy somewhere else.

Lock My Files puts those files in a vault that is encrypted on the phone, name included, and opens them only with your password.

## Who it is for

**Good fit if you...**

- keep ID scans, contracts, certificates, medical letters or private photos on an Android phone (Android 7 or later),
- sometimes hand your phone to someone else, or leave it on a table,
- want to look at those files without passing them to another app,
- can keep a password and 12 recovery words safe, on paper, yourself.

**Not for you if...**

- **you need it for files you cannot afford to lose today.** v0.1.0 is an early build and has not been run on a real Android phone yet. Keep a copy elsewhere.
- **you use an iPhone.** The download here is Android only.
- **you only install apps from the Play Store.** This is an APK you install yourself ("sideload") from the release page.
- **you want a backup or cloud sync.** Nothing is backed up. Lose the phone and the vaults go with it.
- **you want someone to reset a forgotten password.** There is no account and no reset. Lose the password and the recovery words, and the files are gone.
- **you need to hide that a vault exists.** The vault name, file sizes and dates are not encrypted.

## Before / After

| Before | After |
| :--- | :--- |
| The ID card scan sits in the gallery, next to holiday photos | The scan is in a vault, encrypted |
| Names like `KTP_contoh.pdf` are readable by any app with storage access | Names and file types are inside the encrypted data. Size and date stay readable |
| Anyone holding the unlocked phone can scroll to it | A six-digit app passcode, then the vault's own password |
| To look at a file, you open it in another app | Photos, text, video and audio open inside the vault |
| The app stays open when you put the phone down | It locks 30 seconds after you switch away, blocks screenshots, and hides itself in recent apps |
| "Is this app uploading my files?" | v0.1.0 has no internet permission, so Android does not let it connect |

![Animated illustration, before and after. Before: Dina's gallery and Downloads show KTP_contoh.pdf, Kontrak_sewa.pdf and Sertifikat_rumah_scan.pdf next to holiday photos, and a terminal for any app with storage access lists those names in red. A lime bar wipes across to After: the three documents are copied into the vault and the originals deleted by Dina, only the holiday photos remain, and the vault on the storage lists scrambled .enc names with their sizes, noting that names and file types are encrypted while size and date stay readable.](docs/before-after.gif)

## How it works

1. **Pick files.** Open a vault, tap Add files, and pick one or more.
2. **They are encrypted on the way in.** Your vault password goes through Argon2id to make the key that opens the vault. Each file has its own key and is encrypted with XChaCha20-Poly1305. The name and file type go inside the encrypted data.
3. **Delete the originals yourself.** Adding a file copies it. The original stays in your gallery or Downloads until you delete it.
4. **Open them inside the app.** Photos, text, video and audio open in the vault. Tap Lock, or switch away for 30 seconds, and it locks.

![Animated illustration of the four steps, drawn in one by one with arrows between them. 1, Pick files: KTP_contoh.pdf, Kontrak_sewa.pdf and Sertifikat_rumah_scan.pdf get ticked. 2, Encrypted on the way in: a password is typed, a key appears, and the name KTP_contoh.pdf turns into e41a0c8f-77d3.enc. 3, Delete the originals: the gallery copy of KTP_contoh.pdf is crossed out, "deleted by you". 4, Open inside the app: a vault called Dokumen penting lists the files, with KTP_contoh.pdf highlighted.](docs/how-it-works.gif)

The full flow, from install to auto-lock: [How it works](docs/how-it-works.md). The encryption in detail: [Security and limits](docs/security.md).

## See it in the app

![Animated walkthrough made from real app screens: on the Dokumen penting vault, the password is entered and Open is tapped. The vault lists Sertifikat_rumah_scan.pdf, Ijazah_S1_contoh.pdf, Bromo_sunrise.jpg, Kontrak_sewa.pdf and KTP_contoh.pdf. Bromo_sunrise.jpg is tapped and opens inside the app. Back, then Lock, and the vault asks for its password again. The screens are real; only the taps and slides between them are animated.](docs/walkthrough.gif)

*Made from real screens of the current development build, with sample files. Only the taps and transitions are animated. A few controls, such as adding files without unlocking, arrive after v0.1.0.*

<details>
<summary>The three screens, side by side</summary>

![Three phone screens from the app. A vault called Dokumen penting asks for its password. Unlocked, it lists a house certificate scan, a diploma, a sunrise photo, a rental contract and an ID card, each with its size. The sunrise photo opens inside the app, with buttons to save a copy outside the vault or give the file its own password](docs/screens.png)

</details>

## What it does

- **Locks files in a vault.** Each vault has its own password, and each file is encrypted on the way in.
- **Hides the file names too.** `passport-scan.jpg` is not readable on the storage.
- **v0.1.0 has no internet permission**, so Android does not let it connect. Check it in App info, Permissions.
- **Opens files inside the app.** Photos, text, video and audio open in the vault, without another app.
- **Gives you 12 recovery words per vault**, for the day you forget the password.
- **Lets you give one file its own password**, which the vault password and recovery words cannot open.

Every feature, with what it is for: [Features](docs/features.md).

## Quick start

> **Early build.** v0.1.0 is not yet tested on a real phone, so keep a copy of anything important elsewhere. The source is not public yet; the APK is free to use.

The [latest release](https://github.com/BrianArfi/lock-my-files/releases/latest) has two files: `lock-my-files-0.1.0.apk` (about 60 MB) and `lock-my-files-0.1.0.apk.sha256`.

1. On your phone, download `lock-my-files-0.1.0.apk` from the [latest release](https://github.com/BrianArfi/lock-my-files/releases/latest).
2. Allow "Install unknown apps" for your browser when Android asks.
3. Optional: check the SHA-256 on a computer (command in [docs/install.md](docs/install.md#steps)).
4. Set a six-digit app passcode, make a vault, write down its 12 recovery words, and add your first file.

Try recovery once with a test vault before you trust it with real files: [Install and verify](docs/install.md#try-it-first-with-a-test-vault).

## Example

Dina makes a vault called "Dokumen penting" with a long password, and writes the 12 recovery words on paper. She taps Add files and picks `KTP_contoh.pdf`, `Kontrak_sewa.pdf` and `Sertifikat_rumah_scan.pdf`. They now show in the vault list with their sizes. She deletes the three originals from Downloads herself.

When her landlord asks for the contract again, she opens the vault, taps `Kontrak_sewa.pdf`, and uses "Save a copy outside the vault" to send it. The copy she sends is decrypted; the one in the vault stays locked.

---

## Documentation

- [Install and verify](docs/install.md): requirements, SHA-256 check, first setup, and a test vault to try recovery.
- [How it works](docs/how-it-works.md): the flow from install to auto-lock, step by step.
- [Features](docs/features.md): every feature, what you get, and what to use it for.
- [Security and limits](docs/security.md): how the encryption works, and what the app does not do.

## Status

Version 0.1.0, Android only. The encryption is checked against published test vectors, and the whole flow passes an automated end-to-end test. That test has only run in an iOS simulator. This Android build has not been run on a real phone. Do not put anything in it that you cannot afford to lose.

This repository hosts the release download. The source code is not published here.

## FAQ

**What happens if I forget my password?**
Use the 12 recovery words for that vault. If you lost those too, the files are gone. There is no reset, because a reset would mean someone else could open your files.

**How do I know it does not upload my files?**
Version 0.1.0 has no internet permission, so Android does not let it open a network connection. Open the app info screen on your phone and check the permissions list.

**Is it safe to use for important files now?**
Not yet. Version 0.1.0 has not been run on a real Android phone. Keep a copy of anything important somewhere else until a tested build is out.

**Does it hide the original photo from my gallery?**
No. It copies the file into the vault. You delete the original yourself.

**Can someone just keep guessing my password?**
There is no password verifier on the phone, so the only way to test a guess is the full key derivation. But wrong guesses are not rate-limited in 0.1.0, so pick a vault password that is long and hard to guess.

**What if I lose my phone?**
The vaults go with it. Nothing is backed up, and a vault is not a backup. Keep copies of important papers somewhere else.

**Can anyone see what is in a vault without opening it?**
They can see the vault name, and the size and date of each file. Names, file types and contents are encrypted. Use a plain vault name like "Documents".

**Is there an iPhone version?**
Not in this repository. The download here is Android only.

More questions and every known limit: [Security and limits](docs/security.md).

## Changelog

The full history is in [CHANGELOG.md](CHANGELOG.md). **Latest: [0.1.0] - 2026-09-09**, the first public build. Each [release](https://github.com/BrianArfi/lock-my-files/releases) carries its own notes and the SHA-256 of its download.

## License

The contents of this repository are licensed under Apache-2.0: see [LICENSE](LICENSE) and [NOTICE](NOTICE). The APK in the releases is free to download. The app's source code is not published in this repository.

The README animations are rendered from the sources in [docs/src](docs/src): `python docs/src/render_gifs.py`.

By [Brian Arfi](https://brianarfi.com).
