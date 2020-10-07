import platform, cpuinfo
cpuinfo = cpuinfo.get_cpu_info() # Get it before hand, takes time

async def msg(msg):
    info=[
    'Arch: '+platform.machine(),
    'CPU: '+cpuinfo['brand_raw']+' \"'+cpuinfo['vendor_id_raw']+'\"',
    'Operating system: '+platform.system()+' '+platform.release(),
    ]
    await msg.channel.send('\n'.join(info))
