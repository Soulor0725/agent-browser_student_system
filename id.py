import random
import string
import csv

def generate_id_number():
    """生成随机身份证号码"""
    # 地区代码（前6位）
    area_code = random.choice([
        "110101", "310101", "440106", "500101", "510107",
        "420106", "330106", "320106", "610104", "410105"
    ])
    
    # 出生日期（8位） 1990-2005年出生
    year = random.randint(1990, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birth_date = f"{year}{month:02d}{day:02d}"
    
    # 顺序码（3位）
    sequence = f"{random.randint(0, 999):03d}"
    
    # 前17位
    id_17 = area_code + birth_date + sequence
    
    # 计算校验码（第18位）
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    
    sum_value = sum(int(id_17[i]) * weights[i] for i in range(17))
    check_code = check_codes[sum_value % 11]
    
    return id_17 + check_code

def generate_name():
    """生成随机中文姓名"""
    # 常见姓氏
    surnames = [
        "王", "李", "张", "刘", "陈", "杨", "黄", "赵", "吴", "周",
        "徐", "孙", "马", "朱", "胡", "郭", "何", "林", "罗", "高",
        "郑", "梁", "谢", "宋", "唐", "许", "韩", "冯", "邓", "曹"
    ]
    
    # 常见名字用字
    name_chars = [
        "伟", "芳", "娜", "敏", "静", "丽", "强", "磊", "军", "洋",
        "勇", "艳", "杰", "娟", "涛", "明", "超", "秀英", "华", "鹏",
        "飞", "婷", "宇", "浩", "欣", "雨", "晨", "轩", "昊", "瑞",
        "嘉", "怡", "慧", "鑫", "琪", "涵", "梦", "瑶", "琳", "妍"
    ]
    
    surname = random.choice(surnames)
    # 随机生成1-2个字的名字
    if random.random() < 0.3:
        name = random.choice(name_chars)
    else:
        name = random.choice(name_chars) + random.choice(name_chars)
    
    return surname + name

def generate_phone():
    """生成随机手机号码"""
    # 常见的手机号段
    prefixes = [
        "138", "139", "135", "136", "137", "150", "151", "152",
        "157", "158", "159", "182", "183", "187", "188", "130",
        "131", "132", "155", "156", "185", "186", "133", "153",
        "180", "189"
    ]
    
    prefix = random.choice(prefixes)
    # 生成后8位随机数字
    suffix = ''.join(random.choices(string.digits, k=8))
    
    return prefix + suffix

def generate_data(count=100):
    """批量生成数据"""
    data = []
    for _ in range(count):
        record = {
            "姓名": generate_name(),
            "身份证号": generate_id_number(),
            "电话": generate_phone()
        }
        data.append(record)
    return data

def write_to_csv(data, filename="output.csv"):
    """将数据写入CSV文件"""
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=["姓名", "身份证号", "电话"])
        writer.writeheader()
        writer.writerows(data)
    print(f"成功生成 {len(data)} 条数据，保存到 {filename}")

def main():
    # 生成100条数据，可修改数量
    count = 100
    data = generate_data(count)
    write_to_csv(data, "身份证姓名电话数据.csv")

if __name__ == "__main__":
    main()
