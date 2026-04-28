import json
with open('0_30_s_academic_mc_v0_1_qa_processed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
new_data = []
for item in data:
    new_item = item.copy()
    image_path = new_item.pop('video')
    new_item['videos'] = [image_path]
    new_data.append(new_item)  
with open('video.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

