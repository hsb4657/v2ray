import re
import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding="utf-8") as f:
        lines = f.readlines()
        need_fix = True
        for line in lines:
            if line.find("自动选择") >= 0:
                need_fix = False
        if need_fix:
            auto_proxy = []
            in_proxy_groups = False
            find_node_select = False
            row = 0
            auto_row = 1
            auto_sel = ''
            for line in lines:
                if in_proxy_groups is False and line.find("proxy-groups") >= 0:
                    in_proxy_groups = True
                if in_proxy_groups and find_node_select is False and line.find("name:") >= 0 and line.find("节点选择") >= 0:
                    find_node_select = True
                    match = re.search(r'name\s*:(.*)\n', line)
                    if match:
                        auto_proxy.append(re.sub(match.group(1), ' ♻️ 自动选择', line))
                        continue
                if find_node_select and line.find("name:") < 0:
                    if line.find("type:") >= 0:
                        auto_proxy.append(re.sub(re.search(r'type\s*:(.*)\n', line).group(1), ' url-test', line))
                        auto_proxy.append(re.sub(r'type\s*:(.*)\n', 'url: http://www.gstatic.com/generate_204\n', line))
                        auto_proxy.append(re.sub(r'type\s*:(.*)\n', 'interval: 300\n', line))
                    elif line.find("DIRECT") < 0:
                        auto_proxy.append(line)
                    else:
                        auto_sel = re.sub("DIRECT", "♻️ 自动选择", line)
                        auto_row = row + 1
                if find_node_select and line.find("name:") >= 0:
                    break
                row = row + 1
            row = row + 1
            for record in auto_proxy:
                lines.insert(row, record)
                row = row + 1
            lines.insert(auto_row, auto_sel)
        with open(sys.argv[2], 'w', encoding="utf-8") as f2:
            f2.writelines(lines)
            print("update file")
