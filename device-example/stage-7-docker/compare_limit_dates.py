"""Compare the limit dates two running services return.

    python compare_limit_dates.py http://127.0.0.1:8001 http://127.0.0.1:8000

The dates are compared exactly (the course's criterion for dates). Exit status 0
means identical; 1 means they differ.
"""

import json
import sys
import urllib.request


def fetch(base_url):
    with urllib.request.urlopen(f"{base_url.rstrip('/')}/limits", timeout=10) as response:
        return json.load(response)


def main(local_url, docker_url):
    local, docker = fetch(local_url), fetch(docker_url)
    for item in local["devices"]:
        print("local ", item["device_id"], item["limit_date"])
    for item in docker["devices"]:
        print("docker", item["device_id"], item["limit_date"])
    if local != docker:
        print("DIFFERENT: the limit dates do not match")
        return 1
    print("MATCH: local and Docker limit dates are identical")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
