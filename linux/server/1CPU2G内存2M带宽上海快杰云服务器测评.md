---
title: 1CPU/2G内存/2M带宽/上海/快杰云服务器测评
abstract: 1CPU/2G内存/2M带宽/上海/快杰云服务器测评，包含磁盘 IO 测试、网络带宽测试、网络延时测试、网络丢包测试、Benchmarks 性能测试、SysBench 压力测试和Geekbench 处理器内存测试。
url: ucloud-kuaijie-server-evaluate
permalink: ucloud-kuaijie-server-evaluate
date: 2021-01-05 19:25:26
category:
  - [主机测评]
tags:
  - [主机测评]
  - [UCloud]
---

<details>
   <summary>目录</summary>

- [系统配置](#系统配置)
- [磁盘 IO 测试](#磁盘-io-测试)
  - [DD 测试](#dd-测试)
  - [IOPing 测试](#ioping-测试)
  - [FIO 测试](#fio-测试)
- [网络带宽测试](#网络带宽测试)
- [网络延迟测试](#网络延迟测试)
- [网络丢包测试](#网络丢包测试)
- [Benchmarks 性能测试](#benchmarks-性能测试)
- [SysBench 压力测试](#sysbench-压力测试)
  - [CPU 压力测试](#cpu-压力测试)
  - [内存压力测试](#内存压力测试)
- [Geekbench 处理器内存测试](#geekbench-处理器内存测试)

</details>

![ucloud-kuaijie-server-evaluate](https://img.zxj.guru/2021/01/ucloud-kuaijie-server-evaluate.png)

云服务器配置：

```ini
型号 : 快杰型 O
CPU  : 1核 （Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz  2.39 GHz）
内存 : 2G
带宽 : 2M
磁盘 : 40G （SSD）
虚拟 : KVM
IP  : IPv4 x 1 （BGP）
内网 : 支持内网互通
数据中心 : 上海二区
```

## 系统配置

```ini
 CPU Model            : Intel Xeon Processor (Cascadelake)
 CPU Cores            : 1 Cores 2494.140 MHz x86_64
 CPU Cache            : 16384 KB
 OS                   : CentOS 7.6.1810 (64 Bit) KVM
 AES-NI               : Enabled
 VM-x/AMD-V           : Disabled
 Kernel               : 4.19.0-9.el7.ucloud.x86_64
 Total Space          : 1.9 GB / 40.0 GB
 Total RAM            : 67 MB / 1917 MB (126 MB Buff)
 Total SWAP           : 0 MB / 0 MB
 Uptime               : 0 days 20 hour 22 min
 Load Average         : 0.00, 0.00, 0.00
 TCP CC               : cubic
 ASN & ISP            : AS4812, UCLOUD
 Organization         : Shanghai UCloud Information Technology Company Limited
 Location             : Beijing, China / CN
 Region               : Beijing
```

![superbench](https://img.zxj.guru/2021/01/superbench.jpg)

## 磁盘 IO 测试

### DD 测试

```bash
#dd 1Mx1k fdatasync
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB) copied, 13.7801 s, 77.9 MB/s

#dd 64kx16k fdatasync
16384+0 records in
16384+0 records out
1073741824 bytes (1.1 GB) copied, 13.7582 s, 78.0 MB/s

#dd 1Mx1k dsync
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB) copied, 13.7411 s, 78.1 MB/s

#dd 64kx16k dsync
16384+0 records in
16384+0 records out
1073741824 bytes (1.1 GB) copied, 13.9099 s, 77.2 MB/s
```

### IOPing 测试

```bash
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=1 time=90.6 us (warmup)
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=2 time=130.8 us
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=3 time=180.3 us
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=4 time=206.4 us
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=5 time=192.3 us
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=6 time=177.7 us
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=7 time=196.3 us
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=8 time=234.3 us (slow)
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=9 time=195.1 us
4 KiB <<< /root/benchmark/ (xfs /dev/vda1): request=10 time=204.8 us

--- /root/benchmark/ (xfs /dev/vda1) ioping statistics ---
9 requests completed in 1.72 ms, 36 KiB read, 5.24 k iops, 20.5 MiB/s
generated 10 requests in 9.00 s, 40 KiB, 1 iops, 4.44 KiB/s
min/avg/max/mdev = 130.8 us / 190.9 us / 234.3 us / 26.4 us

#IOPing seek rate
--- /root/benchmark/ (xfs /dev/vda1) ioping statistics ---
11.3 k requests completed in 2.99 s, 44.1 MiB read, 3.78 k iops, 14.8 MiB/s
generated 11.3 k requests in 3.00 s, 44.1 MiB, 3.76 k iops, 14.7 MiB/s
min/avg/max/mdev = 57.6 us / 264.8 us / 3.43 ms / 204.4 us

#IOPing sequential
--- /root/benchmark/ (xfs /dev/vda1) ioping statistics ---
898 requests completed in 2.98 s, 224.5 MiB read, 301 iops, 75.3 MiB/s
generated 899 requests in 3.00 s, 224.8 MiB, 299 iops, 74.9 MiB/s
min/avg/max/mdev = 1.86 ms / 3.32 ms / 4.19 ms / 502.4 us

#IOPing cached
--- /root/benchmark/ (xfs /dev/vda1) ioping statistics ---
2.45 M requests completed in 2.86 s, 9.34 GiB read, 854.8 k iops, 3.26 GiB/s
generated 2.45 M requests in 3.00 s, 9.34 GiB, 816.0 k iops, 3.11 GiB/s
min/avg/max/mdev = 460 ns / 1.17 us / 137.8 us / 472 ns
```

### FIO 测试

```bash
fio Disk Speed Tests (Mixed R/W 50/50):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 7.56 MB/s     (1.8k) | 38.16 MB/s     (596)
Write      | 7.59 MB/s     (1.8k) | 38.46 MB/s     (600)
Total      | 15.16 MB/s    (3.7k) | 76.62 MB/s    (1.1k)
           |                      |
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 37.31 MB/s      (72) | 37.00 MB/s      (36)
Write      | 39.31 MB/s      (76) | 39.65 MB/s      (38)
Total      | 76.63 MB/s     (148) | 76.66 MB/s      (74)


#FIO full write pass
writefile: (g=0): rw=write, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=200
fio-3.7
Starting 1 process
writefile: Laying out IO file (1 file / 10240MiB)

writefile: (groupid=0, jobs=1): err= 0: pid=30854: Tue Jan  5 16:35:54 2021
  write: IOPS=74, BW=74.8MiB/s (78.5MB/s)(10.0GiB/136867msec)
    slat (usec): min=8, max=401431, avg=13009.29, stdev=35003.85
    clat (msec): min=976, max=4315, avg=2655.81, stdev=201.12
     lat (msec): min=976, max=4315, avg=2668.83, stdev=204.07
    clat percentiles (msec):
     |  1.00th=[ 1737],  5.00th=[ 2635], 10.00th=[ 2635], 20.00th=[ 2635],
     | 30.00th=[ 2668], 40.00th=[ 2668], 50.00th=[ 2668], 60.00th=[ 2668],
     | 70.00th=[ 2668], 80.00th=[ 2668], 90.00th=[ 2668], 95.00th=[ 2769],
     | 99.00th=[ 3540], 99.50th=[ 3675], 99.90th=[ 4212], 99.95th=[ 4212],
     | 99.99th=[ 4329]
   bw (  KiB/s): min= 2048, max=212992, per=99.40%, avg=76155.04, stdev=13951.54, samples=270
   iops        : min=    2, max=  208, avg=74.33, stdev=13.63, samples=270
  lat (msec)   : 1000=0.02%
  cpu          : usr=1.44%, sys=0.13%, ctx=1405, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.2%, 32=0.3%, >=64=99.4%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,10240,0,1 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=200

Run status group 0 (all jobs):
  WRITE: bw=74.8MiB/s (78.5MB/s), 74.8MiB/s-74.8MiB/s (78.5MB/s-78.5MB/s), io=10.0GiB (10.7GB), run=136867-136867msec

Disk stats (read/write):
  vda: ios=4/10414, merge=0/4, ticks=6527/16922060, in_queue=16923349, util=9.00%


#FIO rand read
benchmark: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
...
fio-3.7
Starting 4 processes

benchmark: (groupid=0, jobs=4): err= 0: pid=30858: Tue Jan  5 16:36:25 2021
   read: IOPS=3791, BW=14.8MiB/s (15.5MB/s)(445MiB/30033msec)
    slat (nsec): min=1832, max=21089k, avg=1050410.92, stdev=2778297.58
    clat (usec): min=705, max=171180, avg=133773.08, stdev=6267.82
     lat (usec): min=711, max=171183, avg=134824.10, stdev=6187.07
    clat percentiles (msec):
     |  1.00th=[  126],  5.00th=[  126], 10.00th=[  127], 20.00th=[  128],
     | 30.00th=[  134], 40.00th=[  136], 50.00th=[  136], 60.00th=[  136],
     | 70.00th=[  136], 80.00th=[  136], 90.00th=[  136], 95.00th=[  144],
     | 99.00th=[  146], 99.50th=[  146], 99.90th=[  148], 99.95th=[  155],
     | 99.99th=[  165]
   bw (  KiB/s): min= 2746, max= 3952, per=24.91%, avg=3778.01, stdev=118.80, samples=240
   iops        : min=  686, max=  988, avg=944.50, stdev=29.72, samples=240
  lat (usec)   : 750=0.01%
  lat (msec)   : 2=0.01%, 10=0.01%, 20=0.01%, 50=0.08%, 100=0.21%
  lat (msec)   : 250=99.69%
  cpu          : usr=0.31%, sys=0.43%, ctx=14280, majf=0, minf=548
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=99.8%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=113861,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=14.8MiB/s (15.5MB/s), 14.8MiB/s-14.8MiB/s (15.5MB/s-15.5MB/s), io=445MiB (466MB), run=30033-30033msec

Disk stats (read/write):
  vda: ios=113352/2, merge=0/0, ticks=3754819/126, in_queue=3736875, util=99.61%


#FIO rand write
benchmark: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
...
fio-3.7
Starting 4 processes

benchmark: (groupid=0, jobs=4): err= 0: pid=30864: Tue Jan  5 16:36:56 2021
  write: IOPS=3791, BW=14.8MiB/s (15.5MB/s)(445MiB/30034msec)
    slat (nsec): min=1972, max=19064k, avg=1050205.92, stdev=2776178.64
    clat (msec): min=3, max=171, avg=133.78, stdev= 6.20
     lat (msec): min=3, max=171, avg=134.83, stdev= 6.08
    clat percentiles (msec):
     |  1.00th=[  126],  5.00th=[  126], 10.00th=[  127], 20.00th=[  128],
     | 30.00th=[  136], 40.00th=[  136], 50.00th=[  136], 60.00th=[  136],
     | 70.00th=[  136], 80.00th=[  136], 90.00th=[  136], 95.00th=[  144],
     | 99.00th=[  146], 99.50th=[  146], 99.90th=[  153], 99.95th=[  155],
     | 99.99th=[  165]
   bw (  KiB/s): min= 2792, max= 4023, per=24.91%, avg=3777.96, stdev=114.04, samples=240
   iops        : min=  698, max= 1005, avg=944.49, stdev=28.50, samples=240
  lat (msec)   : 4=0.01%, 20=0.01%, 50=0.08%, 100=0.23%, 250=99.68%
  cpu          : usr=0.36%, sys=0.47%, ctx=14266, majf=0, minf=36
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=99.8%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,113868,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=14.8MiB/s (15.5MB/s), 14.8MiB/s-14.8MiB/s (15.5MB/s-15.5MB/s), io=445MiB (466MB), run=30034-30034msec

Disk stats (read/write):
  vda: ios=0/113351, merge=0/0, ticks=0/3754735, in_queue=3737870, util=99.37%
```

## 网络带宽测试

上行带宽：`2Mbps`，下行带宽：`50Mbps`。

使用 `Superbench`脚本测试。

```ini
----------------------------------------------------------------------
 Node Name        Upload Speed      Download Speed      Latency
 Speedtest.net    1.92 Mbit/s       50.54 Mbit/s        16.19 ms
 Fast.com         0.00 Mbit/s       0 Mbit/s            -
 Nanjing 5G   CT  1.91 Mbit/s       47.90 Mbit/s        7.55 ms
 Hefei 5G     CT  1.92 Mbit/s       47.84 Mbit/s        10.57 ms
 Guangzhou 5G CT  1.97 Mbit/s       49.69 Mbit/s        31.17 ms
 TianJin 5G   CU  1.93 Mbit/s       50.44 Mbit/s        19.65 ms
 Shanghai 5G  CU  1.90 Mbit/s       47.98 Mbit/s        1.24 ms
 Tianjin 5G   CM  1.92 Mbit/s       48.66 Mbit/s        27.28 ms
 Wuxi 5G      CM  1.92 Mbit/s       48.63 Mbit/s        10.41 ms
 Nanjing 5G   CM  1.91 Mbit/s       47.39 Mbit/s        10.81 ms
 Hefei 5G     CM  1.94 Mbit/s       47.98 Mbit/s        15.42 ms
----------------------------------------------------------------------
```

使用 `LemonBench` 脚本测试。

```ini
----------------------------------------------------------------------------------
 Node Name                      Upload Speed      Download Speed   Ping Latency
 Speedtest Default                0.23 MB/s        6.00 MB/s        18.18 ms
 China, Jilin CU                0.23 MB/s        6.07 MB/s        41.26 ms
 China, Shandong CU                0.22 MB/s        5.77 MB/s        28.26 ms
 China, Nanjing CU                0.24 MB/s        5.82 MB/s        7.49 ms
 China, Shanghai CU                0.24 MB/s        5.75 MB/s        1.24 ms
 China, Lanzhou CU                Fail: Unknown Error
 China, Beijing CT                Fail: Unknown Error
 China, Hangzhou CT                0.23 MB/s        5.79 MB/s        5.50 ms
 China, Nanjing CT                0.22 MB/s        5.70 MB/s        8.94 ms
 China, Guangzhou CT            0.23 MB/s        6.86 MB/s        30.02 ms
 China, Wuhan CT                0.23 MB/s        5.74 MB/s        18.40 ms
 China, Shenyang CM                0.23 MB/s        5.82 MB/s        39.42 ms
 China, Hangzhou CM                0.24 MB/s        5.77 MB/s        17.65 ms
 China, Nanning CM                0.23 MB/s        5.86 MB/s        50.64 ms
 China, Lanzhou CM                0.23 MB/s        5.88 MB/s        46.02 ms
 Hong Kong, HGC                    0.15 MB/s        5.79 MB/s        52.86 ms
 Hong Kong, CSL                    0.23 MB/s        0.70 MB/s        44.04 ms
 Hong Kong, PCCW                Fail: Unknown Error
 Korea, SK [Kdatacenter]        0.23 MB/s        0.27 MB/s        41.41 ms
 Japan, NTT [fdcservers]        0.24 MB/s        0.30 MB/s        63.57 ms
 Japan, NTT [i3d]                Fail: Unknown Error
 Japan GLBB                        0.24 MB/s        0.11 MB/s        275.13 ms
 Japan Rakuten                    0.23 MB/s        1.71 MB/s        58.26 ms
 Taiwan, Seednet                0.13 MB/s        5.87 MB/s        59.95 ms
 Taiwan, HiNet                    0.24 MB/s        6.00 MB/s        50.90 ms
 Taiwan, TFN                    0.16 MB/s        5.85 MB/s        53.42 ms
 Singapore, Singtel                0.24 MB/s        6.77 MB/s        306.33 ms
 Singapore, M1                    0.26 MB/s        0.17 MB/s        307.53 ms
 Singapore, NME                    0.21 MB/s        7.15 MB/s        66.76 ms
 United States, Century Link    0.25 MB/s        0.11 MB/s        182.87 ms
 United States, Verizon            Fail: Unknown Error
----------------------------------------------------------------------------------
```

## 网络延迟测试

|  区域  |                                  最快/最慢                                   |  平均   |
| :----: | :--------------------------------------------------------------------------: | :-----: |
|  全网  |            上海(bgp) 2.8ms/新西兰奥克兰(globicom.co.nz) 3603.0ms             | 176.7ms |
|  移动  |                 江苏常州(移动) 5.9ms/湖南益阳(移动) 530.4ms                  | 56.1ms  |
|  联通  |                 江苏连云港(联通) 9.8ms/吉林延边(联通) 46.4ms                 | 26.4ms  |
|  电信  |                    上海(电信) 3.9ms/云南昆明(电信) 45.9ms                    | 23.6ms  |
|  华南  |             广东广州(腾讯云) 28.6ms / 广东深圳(天威-bgp) 45.2ms              | 34.4ms  |
|  华北  |                  天津(腾讯云) 20.4ms / 北京(移动云) 38.5ms                   | 27.6ms  |
|  华东  |                   上海(bgp) 2.8ms / 江苏南通(移动) 119.7ms                   | 15.0ms  |
|  华中  |                河南洛阳(bgp) 19.3ms / 湖南益阳(移动) 530.4ms                 | 85.7ms  |
|  东北  |             辽宁沈阳(联通-云端 2) 36.3ms / 辽宁沈阳(移动) 55.2ms             | 44.6ms  |
|  西北  |              陕西西安(移动云) 28.8ms / 陕西西安(移动云) 28.8ms               | 28.8ms  |
|  西南  |               山东济南(移动云) 18.3ms / 云南昆明(移动) 55.7ms                | 40.0ms  |
| 港澳台 |            香港(腾讯云-轻量) 29.3ms / 香港(stacksnet.com) 330.9ms            | 86.0ms  |
|  亚洲  |                  韩国首尔(4090.cn) 27.3ms/日本东京 711.7ms                   | 185.6ms |
|  欧洲  |                  俄罗斯伯力 92.8ms/芬兰哈米纳(GCP) 380.4ms                   | 249.9ms |
|  非洲  |      南非约翰内斯堡(runidc.com) 191.4ms/南非约翰内斯堡(华为云) 423.8ms       | 320.6ms |
| 北美洲 |              美国圣何塞(腾讯云) 129.9ms/墨西哥普埃布拉 326.9ms               | 203.7ms |
| 南美洲 |                巴西里约热内卢 299.4ms/智利瓦尔迪维亚 483.2ms                 | 378.4ms |
| 大洋洲 | 澳大利亚悉尼(AMAZON-LIGHTSAIL) 164.9ms/新西兰奥克兰(globicom.co.nz) 3603.0ms | 504.5ms |

## 网络丢包测试

![ucloud-server-packet-loss](https://img.zxj.guru/2021/01/ucloud-server-packet-loss.jpg)

## Benchmarks 性能测试

```ini
========================================================================
   BYTE UNIX Benchmarks (Version 5.1.3)

   System: 10-23-107-24: GNU/Linux
   OS: GNU/Linux -- 4.19.0-9.el7.ucloud.x86_64 -- #1 SMP Mon Sep 28 10:29:09 UTC 2020
   Machine: x86_64 (x86_64)
   Language: en_US.utf8 (charmap="UTF-8", collate="UTF-8")
   CPU 0: Intel Xeon Processor (Cascadelake) (4988.3 bogomips)
          x86-64, MMX, Physical Address Ext, SYSENTER/SYSEXIT, SYSCALL/SYSRET
   16:37:26 up 1 day, 49 min,  2 users,  load average: 2.17, 1.26, 0.54; runlevel 3

------------------------------------------------------------------------
Benchmark Run: Tue Jan 05 2021 16:37:26 - 17:05:28
1 CPU in system; running 1 parallel copy of tests

Dhrystone 2 using register variables       39250964.9 lps   (10.0 s, 7 samples)
Double-Precision Whetstone                     4683.3 MWIPS (9.8 s, 7 samples)
Execl Throughput                               4915.4 lps   (30.0 s, 2 samples)
File Copy 1024 bufsize 2000 maxblocks        718302.5 KBps  (30.0 s, 2 samples)
File Copy 256 bufsize 500 maxblocks          217004.9 KBps  (30.0 s, 2 samples)
File Copy 4096 bufsize 8000 maxblocks       1408054.4 KBps  (30.0 s, 2 samples)
Pipe Throughput                             1302544.1 lps   (10.0 s, 7 samples)
Pipe-based Context Switching                 263283.5 lps   (10.0 s, 7 samples)
Process Creation                              11682.1 lps   (30.0 s, 2 samples)
Shell Scripts (1 concurrent)                   5726.1 lpm   (60.0 s, 2 samples)
Shell Scripts (8 concurrent)                    739.2 lpm   (60.1 s, 2 samples)
System Call Overhead                        1003677.4 lps   (10.0 s, 7 samples)

System Benchmarks Index Values               BASELINE       RESULT    INDEX
Dhrystone 2 using register variables         116700.0   39250964.9   3363.4
Double-Precision Whetstone                       55.0       4683.3    851.5
Execl Throughput                                 43.0       4915.4   1143.1
File Copy 1024 bufsize 2000 maxblocks          3960.0     718302.5   1813.9
File Copy 256 bufsize 500 maxblocks            1655.0     217004.9   1311.2
File Copy 4096 bufsize 8000 maxblocks          5800.0    1408054.4   2427.7
Pipe Throughput                               12440.0    1302544.1   1047.1
Pipe-based Context Switching                   4000.0     263283.5    658.2
Process Creation                                126.0      11682.1    927.2
Shell Scripts (1 concurrent)                     42.4       5726.1   1350.5
Shell Scripts (8 concurrent)                      6.0        739.2   1231.9
System Call Overhead                          15000.0    1003677.4    669.1
                                                                   ========
System Benchmarks Index Score                                        1241.8

------------------------------------------------------------------------
Benchmark Run: Tue Jan 05 2021 17:05:28 - 17:33:30
1 CPU in system; running 1 parallel copy of tests

Dhrystone 2 using register variables       38893710.4 lps   (10.0 s, 7 samples)
Double-Precision Whetstone                     4670.4 MWIPS (9.8 s, 7 samples)
Execl Throughput                               4792.1 lps   (29.7 s, 2 samples)
File Copy 1024 bufsize 2000 maxblocks        654580.1 KBps  (30.0 s, 2 samples)
File Copy 256 bufsize 500 maxblocks          217516.6 KBps  (30.0 s, 2 samples)
File Copy 4096 bufsize 8000 maxblocks       1391127.2 KBps  (30.0 s, 2 samples)
Pipe Throughput                             1310590.0 lps   (10.0 s, 7 samples)
Pipe-based Context Switching                 264926.3 lps   (10.0 s, 7 samples)
Process Creation                              11501.0 lps   (30.0 s, 2 samples)
Shell Scripts (1 concurrent)                   5763.9 lpm   (60.0 s, 2 samples)
Shell Scripts (8 concurrent)                    747.8 lpm   (60.0 s, 2 samples)
System Call Overhead                        1003968.7 lps   (10.0 s, 7 samples)

System Benchmarks Index Values               BASELINE       RESULT    INDEX
Dhrystone 2 using register variables         116700.0   38893710.4   3332.8
Double-Precision Whetstone                       55.0       4670.4    849.2
Execl Throughput                                 43.0       4792.1   1114.4
File Copy 1024 bufsize 2000 maxblocks          3960.0     654580.1   1653.0
File Copy 256 bufsize 500 maxblocks            1655.0     217516.6   1314.3
File Copy 4096 bufsize 8000 maxblocks          5800.0    1391127.2   2398.5
Pipe Throughput                               12440.0    1310590.0   1053.5
Pipe-based Context Switching                   4000.0     264926.3    662.3
Process Creation                                126.0      11501.0    912.8
Shell Scripts (1 concurrent)                     42.4       5763.9   1359.4
Shell Scripts (8 concurrent)                      6.0        747.8   1246.3
System Call Overhead                          15000.0    1003968.7    669.3
                                                                   ========
System Benchmarks Index Score                                        1229.0
```

## SysBench 压力测试

### CPU 压力测试

```ini
sysbench 1.0.17 (using system LuaJIT 2.0.4)

Running the test with following options:
Number of threads: 1
Initializing random number generator from current time


Prime numbers limit: 20000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:   407.89

General statistics:
    total time:                          10.0010s
    total number of events:              4080

Latency (ms):
         min:                                    2.38
         avg:                                    2.45
         max:                                    3.24
         95th percentile:                        2.86
         sum:                                 9993.97

Threads fairness:
    events (avg/stddev):           4080.0000/0.00
    execution time (avg/stddev):   9.9940/0.00
```

### 内存压力测试

```ini
sysbench 1.0.17 (using system LuaJIT 2.0.4)

Running the test with following options:
Number of threads: 1
Initializing random number generator from current time


Running memory speed test with the following options:
  block size: 1KiB
  total size: 102400MiB
  operation: write
  scope: global

Initializing worker threads...

Threads started!

Total operations: 44316973 (4430902.78 per second)

43278.29 MiB transferred (4327.05 MiB/sec)


General statistics:
    total time:                          10.0001s
    total number of events:              44316973

Latency (ms):
         min:                                    0.00
         avg:                                    0.00
         max:                                    0.18
         95th percentile:                        0.00
         sum:                                 4305.55

Threads fairness:
    events (avg/stddev):           44316973.0000/0.00
    execution time (avg/stddev):   4.3056/0.00
```

## Geekbench 处理器内存测试

```ini
Running Gathering system information
System Information
  Operating System              Linux 4.19.0-9.el7.ucloud.x86_64 x86_64
  Model                         Red Hat KVM
  Motherboard                   N/A
  BIOS                          SeaBIOS 1.10.2-3.el7_4.1

Processor Information
  Name                          Intel Xeon Processor (Cascadelake)
  Topology                      1 Processor, 1 Core
  Identifier                    GenuineIntel Family 6 Model 85 Stepping 6
  Base Frequency                2.49 GHz
  L1 Instruction Cache          32.0 KB
  L1 Data Cache                 32.0 KB
  L2 Cache                      4.00 MB
  L3 Cache                      16.0 MB

Memory Information
  Size                          1.87 GB

Upload succeeded. Visit the following link and view your results online:

  https://browser.geekbench.com/v5/cpu/5713421
```
