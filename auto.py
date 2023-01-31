import yaml
import sys
import shutil

if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if not data['proxy-groups'] is None and not data['proxies'] is None and not any(proxie['type'] =='url-test' for proxie in data['proxy-groups']):
            proxies = list(map(lambda x: x['name'], data['proxies']))
            proxy_group = {}
            proxy_group['name'] = '♻️ 自动选择'
            proxy_group['type'] = 'url-test'
            proxy_group['url'] = 'http://www.gstatic.com/generate_204'
            proxy_group['interval'] = 300
            proxy_group['proxies'] = proxies
            data['proxy-groups'].append(proxy_group)
            data['proxy-groups'][0]['proxies'].insert(1, '♻️ 自动选择')
            with open(sys.argv[2], 'w', encoding='utf-8') as f1:
                yaml.safe_dump(data, f1, allow_unicode=True)
        else:
            shutil.copy(sys.argv[1], sys.argv[2])

