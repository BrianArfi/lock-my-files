# Install and verify

[Back to the README](../README.md)

## Requirements

- **Android 7 or later.**
- **A 64-bit or 32-bit ARM phone** (arm64-v8a or armeabi-v7a). Most Android phones are one of these.
- **Permission to install an APK** from outside the Play Store, for this one install.

## Steps

**1. Download.** Open the [latest release](https://github.com/BrianArfi/lock-my-files/releases/latest) on your phone or computer. Get `lock-my-files-0.1.0.apk` and `lock-my-files-0.1.0.apk.sha256`.

**2. Verify the download.** Compare the result with the SHA-256 in the release notes:

```bash
shasum -a 256 lock-my-files-0.1.0.apk                # macOS or Linux
certutil -hashfile lock-my-files-0.1.0.apk SHA256    # Windows
```

If the two values are not the same, do not install the file.

**3. Install.** Copy the APK to the phone and open it. Android asks you to allow installs from that source. Allow it for this install only.

**4. Set up.** Set the six-digit app passcode, then make your first vault and write down its 12 recovery words.

## Try it first, with a test vault

Before you put real files in, make a vault called "Test" and add a file you do not need. Lock the app, then open the vault again with the password. Then open it with the 12 recovery words. When both work, you know how the recovery works. Delete the test vault after that.

## Why an APK and not a store download?

This build is published here, as an APK on the release page. Check the SHA-256 before you install it.
