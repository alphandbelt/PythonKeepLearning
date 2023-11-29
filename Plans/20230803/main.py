
"""
    获取磁盘的信息

"""

import psutil
import shutil

# 获取磁盘的分区详情


def get_disk_partitions():
    disk_info = []

    pds = psutil.disk_partitions()
    for pd in pds:
        # print(pd.mountpoint)
        use = shutil.disk_usage(pd.mountpoint)
        # print(f"use:{use}")
        use_percentage = use.used/use.total * 100.0
        # print(f"use_percentage:{use_percentage}%")
        tmp = (pd.mountpoint,use_percentage)
        disk_info.append(tmp)
    # print(disk_info)
    return disk_info







if __name__  == "__main__":
    disks = get_disk_partitions()
    print(f"disks:{disks}")


