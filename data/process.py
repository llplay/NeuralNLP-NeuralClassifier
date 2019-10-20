import random
import json

domains = {}

with open("domain", encoding="utf-8") as f:
    for line in f:
        dm, query = line.strip().split("\t")
        if dm not in domains:
            domains[dm] = [query]
        else:
            domains[dm].append(query)

# train, test, dev
for dm, querys in domains.items():
    random.shuffle(querys)
    querys_tmp = []
    for line in querys:
        if random.randint(0, 9) < 8:
            querys_tmp.append({"query": line, "mode": "train"})
        else:
            if random.randint(0, 1) < 1:
                querys_tmp.append({"query": line, "mode": "test"})
            else:
                querys_tmp.append({"query": line, "mode": "dev"})
    domains[dm] = querys_tmp

dev_file = open("dm_dev.json", "w", encoding="utf-8")
test_file = open("dm_test.json", "w", encoding="utf-8")
train_file = open("dm_train.json", "w", encoding="utf-8")

for dm, querys in domains.items():
    for i in querys:
        if i["mode"] == "train":
            train_file.write(json.dumps({"doc_label": [dm], "doc_token": [j for j in i["query"]],
                                         "doc_keyword": [], "doc_topic": []},
                                        ensure_ascii=False) + "\n")
        elif i["mode"] == "test":
            test_file.write(json.dumps({"doc_label": [dm], "doc_token": [j for j in i["query"]],
                                       "doc_keyword": [], "doc_topic": []},
                                       ensure_ascii=False) + "\n")
        else:
            dev_file.write(json.dumps({"doc_label": [dm], "doc_token": [j for j in i["query"]],
                                      "doc_keyword": [], "doc_topic": []},
                                      ensure_ascii=False) + "\n")

dev_file.close()
test_file.close()
train_file.close()

print(json.dumps(domains, indent=4, ensure_ascii=False))
