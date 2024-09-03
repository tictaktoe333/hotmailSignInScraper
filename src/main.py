import re
import ipaddress


if __name__ == "__main__":
    mhtml_file = "./file.mhtml"
    ip_start_sequence = '<span data-bind=3D"text: ip">'
    with open(mhtml_file, 'r') as f:
        mhtml_content = f.readlines()
        for line in mhtml_content:
            try:
                if re.search(ip_start_sequence, line) is not None:
                    target_ip_address = line.split(ip_start_sequence)[1]
                    target_ip_address = target_ip_address.split("<")[0]
                    ipaddress.IPv4Address(target_ip_address)
                    print(target_ip_address)
            except ValueError as exc:
                continue
