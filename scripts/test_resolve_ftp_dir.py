#!/usr/bin/env python3
"""Check path selection against a Hostinger-shaped folder tree."""

import unittest
from ftplib import error_perm

import resolve_ftp_dir as resolver


class FakeFTP:
    def __init__(self, tree):
        self.tree = tree
        self.cwd_path = "/"

    def pwd(self):
        return self.cwd_path

    def cwd(self, path):
        path = path if path.startswith("/") else resolver.join_path(self.cwd_path, path)
        path = "/" if path == "" else path
        if path != "/" and path.strip("/") not in self._dirs():
            raise error_perm("missing")
        self.cwd_path = path

    def mlsd(self):
        prefix = "" if self.cwd_path == "/" else self.cwd_path.strip("/") + "/"
        children = []
        for full in self._dirs():
            if prefix == "":
                rest = full
            elif full.startswith(prefix):
                rest = full[len(prefix) :]
            else:
                continue
            if "/" in rest or rest == "":
                continue
            children.append((rest, {"type": "dir"}))
        return children

    def _dirs(self):
        return set(self.tree)


class ResolveTests(unittest.TestCase):
    def test_public_html_after_two_directories(self):
        ftp = FakeFTP(
            {
                "domains",
                "domains/example.com",
                "domains/example.com/public_html",
                "domains/example.com/logs",
                ".trash",
            }
        )
        self.assertEqual(resolver.public_html_two_down(ftp), ["domains/example.com/public_html/"])

    def test_two_sites_are_both_reported(self):
        ftp = FakeFTP(
            {
                "domains",
                "domains/one.com",
                "domains/one.com/public_html",
                "domains/two.com",
                "domains/two.com/public_html",
            }
        )
        self.assertEqual(
            resolver.public_html_two_down(ftp),
            ["domains/one.com/public_html/", "domains/two.com/public_html/"],
        )

    def test_override_keeps_trailing_slash(self):
        self.assertEqual(resolver.with_trailing_slash("domains/example.com/public_html"), "domains/example.com/public_html/")


if __name__ == "__main__":
    unittest.main()
