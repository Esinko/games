# Disobey CTF challenge submission guidelines

First of all, a big thank you for considering to submit a challenge to Disobey CTF. It wouldn't be possible without people like you! These guidelines are here to help you and us to provide the participants with the best competition experience possible.

Latest changes:

* 2026-10-20 - added a recommended solver script (solve.py) with a common interface, and asked for a category and difficulty estimate
* 2025-07-18 - added a submission directory structure template
* 2022-11-14 - minor tweaks on submission formats etc.
* 2022-11-02 - updated the supported platform distributions

## Challenge types

Challenges come in many forms. Examples of challenges (which should not limit you):
* a vulnerable application (SQLi, path traversal, ...) or server (e.g. middleware vulnerabilities) or a combination of these
* reverse engineering
* steganography (lots of different file types possible)
* cryptography
* "escape" challenges, e.g. limited shells
* OSINT
* social engineering
* analysing captured signals or packets
* ...

A single challenge submission can include multiple flags like obtaining a common user account (first flag) and then privescing to another user or root (another flag, be careful with root).

## Submission contents

### Metadata

Please include a text/Markdown file (or HTML/PDF if needed, please avoid proprietary formats) containing the following metadata about the challenge. See [the challenge template](challenge_template/README.md) and [the challenge public information](challenge_template/public/README.md).

* **Preferred challenge name.** We will try to respect this, but will reserve the right to alter it in case of duplicate names or e.g. inappropriate language. This may include your company's name or similar if wanted.
* **Category and difficulty** (nice to have). The category, e.g. web, crypto, forensics, reverse engineering, pwn, stego, OSINT or misc, and your estimate of the difficulty: easy, medium or hard. It helps us balance the competition; we may adjust them.
* **Challenge/task description.** Usually these look like "The intelligence team captured some suspicious packets, can you find out what the attacker was able to steal?" or "Find the flag from our customer database at http://challenge.example.com" (we will fill in the final URL).
* **The flag(s).** The flag should be easily recognizable as a flag. If in any way possible, use DISOBEY[yourflaggoeshere] as the flag format.
* **A walkthrough** so we can test that the challenge works as intended even after we've installed it somewhere. Extremely important if the challenge is hosted by us. A [solver script](#solver-script-recommended) is even better, but the walkthrough is still needed for answering the players' questions.
* **Possible hints** (which will cost points for the participants) if you want to provide any.
* **Installation (and reset) instructions** in case the challenge needs installing with a shell script/Ansible playbook/similar. The more automated and fool proof, the better.
* **Open ports** which the participants should be able to access, if your challenge is a virtual machine, a Docker image, or you are hosting it yourself (in which case we also need the challenge location information). Other ports might not be opened.
* **Your contact information.** At least an email address, preferably a phone number too (or other near-realtime mean of communication) in the case we need more information on the challenge a few weeks before and especially during the event.

### The challenge itself

* For file based challenges, all the necessary files. Use descriptive filenames when possible. "challenge.jpg" is a bad example. If you have very large files (in the ballpark of 1GB and up), please contact the CTF team beforehand
* For web applications / servers, see [the hosting instructions](hosting.md)
* At least try to both minimise and compress large files. Plz.

### Solver script (recommended)

We'd love to get a script that solves your challenge automatically. We run it after installing the challenge, after every update, and every now and then during the event, to notice that something broke before the players do. It's not mandatory: if you can't write one, make the walkthrough exact enough (commands, requests, values) that we can script it ourselves. There's a skeleton in [challenge_template/solve.py](challenge_template/solve.py).

So that we can run every challenge's solver the same way:

* **Name and place:** `solve.py` (Python 3) next to your metadata file, not among the player files. Another language is fine as an executable `solve` that behaves the same way.
* **How we run it:**
  * hosted challenges: `solve.py HOST PORT [PORT ...]`, with the ports in the order of your "Open ports" list. `HOST` can be an IP address or a name, so don't hard-code `localhost`, IP addresses or domains.
  * file-based challenges: `solve.py FILES_DIR`, where `FILES_DIR` contains exactly the files the players get. Use only those files, not your source code or generator, so the script also proves that the challenge is solvable with what the players have.
  * physical/on-site challenges don't need one.
* **Output:** print each flag on its own line on stdout, exactly as in your metadata; anything else goes to stderr. Exit with 0 only when all flags were found, otherwise with non-zero (still printing the flags you did get).
* **Solve it like a player:** don't read the flags from files, the image or the server.
* **Be nice to the live challenge:** the teams share it and we may run the script during the event, so don't break or spoil anything: don't change shared passwords, use random names for anything you create, clean up afterwards, and expect other people to be using the challenge at the same time.
* **Short and unattended:** finish in about 5 minutes, no interactive input or GUI, retry flaky steps yourself. Brute force only with the wordlist you provide.
* **Dependencies:** the standard library if possible, otherwise a `requirements.txt` with pinned versions next to the script. Talk only to the challenge itself, nothing else on the internet.

## Things to consider

* Logic is more appreciated than guessing. Provide enough information so that guessing is minimal or fully avoided. Even when brute-forcing is needed, try to give some hints on the wordlist or a similar starting point. This is a subject for debate so you have the final word on this :-)
* To continue on the guessing topic, avoid requiring software with incompatibilities or similar differences between versions. The participants might not be able to find the exactly right version even if they somehow figure out the right software needed.
* Please avoid the need of uncommon hardware (surprisingly, most participants don't have e.g. a HacKRF with them) or hard-to-obtain tools. However, if you provide these to the participants in some way, then we're all good.
* If your challenge environment is shared between teams, and there's privesc involved, there is always a danger of people breaking things. So allow especially root privescs sparingly. If you still want to do privesc, lateral movement (to non-root accounts) is safer.
* In case of virtual machine images/installation automation, clean up the machine. Try not to leave traces of the automation process and try to also remove binaries that people might misuse.

## Contact

games@disobey.fi
