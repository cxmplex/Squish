from urllib.parse import urlparse
import socket
import whois
import dns.resolver

class URLParserException(Exception):
    pass

class URLParser:
    url = None

    def __init__(self):
        pass

    def parse_urls(self, entries):
        results = {"errors": [], "urls": []}
        
        for entry in entries:
            try:
                parsed_url = urlparse(entry)
                if not parsed_url.scheme or not parsed_url.netloc:
                    results['errors'].append({"error": f"Input {entry} was not a URL"})
                    continue

                url_info = {"scheme": parsed_url.scheme,
                            "netloc": parsed_url.netloc,
                            "path": parsed_url.path,
                            "params": parsed_url.params,
                            "query": parsed_url.query,
                            "fragment": parsed_url.fragment}
                
                # Determine the IP address
                try:
                    ip_address = socket.gethostbyname(parsed_url.netloc)
                    url_info["ip"] = ip_address
                except socket.gaierror:
                    url_info["ip_error"] = "Could not resolve IP"
                    results['urls'].append(url_info)
                    continue

                # Perform WHOIS lookup
                try:
                    domain_info = whois.whois(parsed_url.netloc)
                    url_info["whois"] = domain_info
                except Exception as e:
                    url_info["whois_error"] = str(e)
                
                # MX record lookup
                try:
                    mx_records = dns.resolver.resolve(parsed_url.netloc, 'MX')
                    url_info["mx_records"] = [str(record.exchange) for record in mx_records]
                except Exception as e:
                    url_info["mx_records_error"] = str(e)

                # PTR record lookup for the IP address
                try:
                    ptr_records = dns.resolver.resolve_address(ip_address)
                    url_info["ptr_records"] = [str(record) for record in ptr_records]
                except Exception as e:
                    url_info["ptr_records_error"] = str(e)

                results['urls'].append(url_info)
            except Exception as e:
                results['errors'].append("{}:{}".format(entry,str(e)))

        if len(results['error']):
            raise URLParserException(results)

        return results
