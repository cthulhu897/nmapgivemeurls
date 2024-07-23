
# Nmap HTTP/HTTPS Service URL Extractor

This script processes an Nmap XML file, extracts services that contain "http" in their name, and generates the corresponding URLs based on the port numbers.

## Features

- Parses an Nmap XML file.
- Extracts services with "http" in their name.
- Infers the protocol (HTTP/HTTPS) based on the port number.
- Prints the corresponding URLs.

## Requirements

- Python 3.x

## Usage

1. Run the script using the following command:

```bash
python nmapgivemeurls.py nmap.xml
```

## Example

Given an Nmap XML file `nmap.xml` with the following content:

```xml
<nmaprun>
  <host>
    <address addr="192.168.0.254" />
    <ports>
      <port protocol="tcp" portid="443">
        <service name="https" />
      </port>
      <port protocol="tcp" portid="80">
        <service name="http" />
      </port>
      <port protocol="tcp" portid="11000">
        <service name="http-alt" />
      </port>
    </ports>
  </host>
</nmaprun>
```

Running the script will produce the following output:

```plaintext
https://192.168.0.254
http://192.168.0.254
http://192.168.0.254:11000
https://192.168.0.254:11000
```

## License

This script is provided as-is without any warranty. Feel free to use and modify it as needed.
