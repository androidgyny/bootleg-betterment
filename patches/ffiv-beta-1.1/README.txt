FFIV Trilogy English Beta 1.1 — patch kit
Last updated: November 1, 2026
Requires Python 3 and all three original Chinese X1, X2, X3 ROMs.
Extract the ROMs first. Keep each 16-byte NES header. Each source is 1,048,592 bytes.

Put all three ROMs in the extracted patch-kit folder, alongside the patch scripts.
Replace X1.nes, X2.nes and X3.nes below with your actual filenames, in chapter order.
Keep the quotation marks. The last filename is the finished ROM and must not already exist.

Windows: open the folder in File Explorer, click its address bar, type powershell,
and press Enter. Paste the Windows command below and press Enter.
macOS/Linux: open a terminal in this folder. On macOS, type cd followed by a space,
drag the folder into Terminal, and press Enter, then run the command below.
Double-clicking the launcher alone does not supply the required filenames.

Windows: .\patch-windows.cmd "X1.nes" "X2.nes" "X3.nes" "FFIV-Beta-1.1.nes"
macOS/Linux: sh patch-macos-linux.sh "X1.nes" "X2.nes" "X3.nes" "FFIV-Beta-1.1.nes"
Or run python3 patch.py with the same four arguments (Windows: py -3).

The script validates all three complete-file SHA-256 hashes, removes their headers,
places their 1 MiB payloads after a blank 1 MiB menu area and 16-byte header,
and applies trilogy.ips to that assembled intermediate in memory. Do not apply
this IPS to an individual chapter. It then verifies the exact Beta 1.1 output hash.
The output must be a new filename; originals and existing outputs are never overwritten.
No ROMs are included. The script makes no network requests.

Compatible and tested: FCEUmm (RetroArch core), with NES 2.0 mapper 342 support. Keep original saves backed up.
Use native saves and a fresh boot instead of save states from another release.

Credits: original Final Fantasy IV by Square; original NES trilogy published by
Henggedianzi (developer attribution uncertain). English adaptation and combined
release by P3 with ChatGPT. See the page for release scope and verification limits.

Final Fantasy X1 (Ch)[!].nes
SHA-256: ffc36fcc05bab705dd52d630b4192d509583203a5acd635468b72f520d642820

Final Fantasy X2 (Ch)[!].nes
SHA-256: a85d6c5b9dc0822b846de2e81e793bd1e4930e15a21ee1efeef1f85e72dba01b

Final Fantasy X3 (Ch)[!].nes
SHA-256: fef339d96cf099b687f6f7e403c13136dd22c6cf4d8da2edc99bafae78ca6982

Output SHA-256: 1054a3691807cf68bf483e8a96f11f42532ce32a57d585faa5fbaa3e190a081b

Additional inherited patch credits: Lugia2009 (menu patch); clymax (Lodestone Cavern softlock fix 0.12).

Beta 1.1: preserves Beta 1 story corrections; restores eight-digit GIL above the party, shortens overflowing location/choice labels, and extends the command panel to the bottom. Native save format unchanged.
