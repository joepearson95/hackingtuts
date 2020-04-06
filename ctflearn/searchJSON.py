import json
import sys

def findOccurances(ip):
    with open('incidents.json') as f:
        data = json.load(f)
        result = {}
        hashes = {}
        occur = []
        for d in data['tickets']:
            if 'src_ip' in d:
                result[d['src_ip']] = result.get(d['src_ip'], 0) + 1
            if 'file_hash' in d:
                hashes[d['file_hash']] = hashes.get(d['file_hash'], 0) + 1
        print("src_ip occurances:", result)
        print(hashes)
def main():
    findOccurances(sys.argv[1])

if __name__ == "__main__":
    main()
