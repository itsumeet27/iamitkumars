#!/usr/bin/env python3
"""Find the Hostinger public_html folder two directories below the FTP login."""

import os
import sys
from ftplib import FTP, error_perm, error_proto


def join_path(parent, name):
    if parent in ("", "/"):
        return "/" + name
    return parent.rstrip("/") + "/" + name


def relative_dir(login, full):
    login = login.rstrip("/")
    full = full.rstrip("/")
    if login in ("", "/"):
        relative = full.lstrip("/")
    elif full.startswith(login + "/"):
        relative = full[len(login) + 1 :]
    else:
        relative = full.lstrip("/")
    return relative.strip("/") + "/"


def with_trailing_slash(path):
    path = path.strip()
    if not path.endswith("/"):
        path += "/"
    return path


def child_directories(ftp, path):
    ftp.cwd(path)
    names = []
    try:
        entries = list(ftp.mlsd())
    except (error_perm, error_proto, AttributeError):
        entries = None

    if entries is not None:
        for name, facts in entries:
            if name in (".", ".."):
                continue
            kind = facts.get("type", "")
            if kind in ("dir", "cdir") or "link" in kind or "symlink" in kind:
                names.append(name)
        return sorted(names)

    for raw in ftp.nlst():
        base = raw.rstrip("/").split("/")[-1]
        if base in (".", ".."):
            continue
        try:
            ftp.cwd(join_path(path, base))
            ftp.cwd(path)
        except error_perm:
            ftp.cwd(path)
            continue
        names.append(base)
    return sorted(names)


def public_html_two_down(ftp):
    login = ftp.pwd()
    matches = []
    for first in child_directories(ftp, login):
        first_path = join_path(login, first)
        for second in child_directories(ftp, first_path):
            second_path = join_path(first_path, second)
            if "public_html" in child_directories(ftp, second_path):
                matches.append(relative_dir(login, join_path(second_path, "public_html")))
    return matches


def main():
    override = os.environ.get("FTP_SERVER_DIR", "").strip()
    if override:
        print(with_trailing_slash(override))
        return 0

    server = os.environ["FTP_SERVER"]
    username = os.environ["FTP_USERNAME"]
    password = os.environ["FTP_PASSWORD"]

    ftp = FTP()
    ftp.connect(server, 21, timeout=60)
    try:
        ftp.login(username, password)
        ftp.set_pasv(True)
        matches = public_html_two_down(ftp)
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()

    if len(matches) == 1:
        print("Uploading to %s" % matches[0], file=sys.stderr)
        print(matches[0])
        return 0

    if not matches:
        print(
            "No public_html folder was found two directories below the FTP login.",
            file=sys.stderr,
        )
    else:
        print("More than one public_html folder was found:", file=sys.stderr)
        for match in matches:
            print("  %s" % match, file=sys.stderr)
    print(
        "Set the FTP_SERVER_DIR secret to the folder that should receive the site, including the trailing slash.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
