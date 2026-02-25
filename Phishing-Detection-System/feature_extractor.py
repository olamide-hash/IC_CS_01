from urllib.parse import urlparse
import socket

def extract_features(url):
    features = []

    # URL length
    features.append(len(url))

    # HTTPS check
    features.append(1 if url.startswith("https") else 0)

    # number of dots
    features.append(url.count("."))

    # IP address detection
    try:
        socket.inet_aton(urlparse(url).netloc)
        features.append(1)
    except:
        features.append(0)

    return features
