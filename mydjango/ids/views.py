from django.shortcuts import render
from .utils.openai_utils import analyze_log_entry


def index(request):
    log_entries = [
        '192.168.1.100 - - [18/Nov/2023:15:27:39 +0000] "GET /product?id=1%20OR%201=1 HTTP/1.1" 200 5324 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"',
        '192.168.1.102 - - [18/Nov/2023:16:40:22 +0000] "POST /login" 200 1223 "-" "SQLMap/1.5.6#dev (http://sqlmap.org)"',
        '192.168.1.105 - - [18/Nov/2023:18:02:30 +0000] "GET /home HTTP/1.1" 200 7865 "http://example.net" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"',
        '192.168.1.104 - - [18/Nov/2023:17:55:11 +0000] "GET /search?query=%27%20OR%201=1-- HTTP/1.1" 200 4321 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"',
        '192.168.1.101 - - [18/Nov/2023:15:30:15 +0000] "GET /product?id=123 HTTP/1.1" 200 5432 "http://example.com" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"',
        '192.168.1.103 - - [18/Nov/2023:16:45:09 +0000] "GET /profile" 200 3211 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"',

    ]

    analysis_results = []
    for entry in log_entries:
        analysis = analyze_log_entry(entry)
        analysis_results.append({"entry": entry, "analysis": analysis})

    return render(request, 'dashboard(v3).html', {'analysis_results': analysis_results})
