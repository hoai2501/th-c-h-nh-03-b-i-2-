import requests
import random
import time
while True:
    def random_name():
        first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng"]
        middle_names = ["Huy", "Minh", "Anh", "Quang", "Thanh", "Thị", "Văn", "Đức", "Thái", "Bảo"]
        last_names = ["Hoàng", "Anh", "Hải", "Phong", "Tuấn", "Nam", "Thành", "Thắng", "Hùng", "Dũng"]
        
        first_name = random.choice(first_names)
        middle_name = random.choice(middle_names)
        last_name = random.choice(last_names)
        
        return f"{first_name} {middle_name} {last_name}"

    def random_number(start, end):
        return random.randint(start, end)

    name = random_name()
    number = random_number(1, 10)



    url = "http://localhost/add_student.php"

    payload = {
        "name":name,
        "dob":"2024-05-01",
        "address":"Hà nội",
        "faculty":1,
        "major":1,
        "course":2,
        "diemtongket":number
    }
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'vi',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '120',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'PHPSESSID=lqbojmmshk3fbnb89ts8hrrvol; PHPSESSID=hes2k4okgua9iu4plhuvi3mqcn',
    'Host': 'localhost',
    'Origin': 'http://localhost',
    'Referer': 'http://localhost/add_student.php',
    'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }




    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(5)