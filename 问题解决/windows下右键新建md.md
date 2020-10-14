## windows下右键新建md文件

1. ### 打开注册表

   win键+R打开运行对话框, 输入regedit, 打开注册表编辑器.

2. ### 修改注册表

   在磁盘的任意位置新建一个文件, 后缀名为reg, 并写入一下内容

   ```
   [HKEY_CLASSES_ROOT\.md]
   @="Typora.exe"
   [HKEY_CLASSES_ROOT\.md\ShellNew]
   "NullFile"=""
   [HKEY_CLASSES_ROOT\Typora.exe]
   @="Markdown"
   ```

   写入后另存为, 文件名自定, 后缀必须为reg, 保存类型为文本类型, 编码为unicode或ANSI.

   保存后双击运行, 即可. 如果没有生效, 可重启.

3. ### 编辑新建图标

   注册表编辑器中, 在`计算机\HKEY_CLASSES_ROOT`右键查找, 输入Typora, 只勾选项. 
   
   在注册表Typora.ex下点击DefaultIcon, 右键修改, 将属性修改为想要设置的图标即可.

