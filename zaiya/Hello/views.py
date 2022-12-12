from django.shortcuts import render  # 导入render模块
import os

def index_text(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == 'POST':
        if 'update' in request.POST:
            print('更新')
        elif 'del' in request.POST:
            print('删除')
            # 'screen', '-dmS', screen_dir.get(Dst_Master1),
            # './dontstarve_dedicated_server_nullrenderer_x64',
            # '-persistent_storage_root', persistent_storage_root,
            # '-conf_dir', conf_dir,  # 游戏路径
            # '-cluster', cluster,  # 存档路径
            # '-shard', Master1  # 世界路径

        elif 'add' in request.POST:
            os.system('chmod +x install.sh')
            os.system('./install.sh')
        return render(request, 'index.html')
