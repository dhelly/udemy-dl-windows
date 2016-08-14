# -*- mode: python -*-
a = Analysis(['src\\udemy_dl.py'],
             hiddenimports=[],
             hookspath=['./hooks'],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='udemy-dl.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , version='res\\version.txt', icon='res\\icon.ico')
