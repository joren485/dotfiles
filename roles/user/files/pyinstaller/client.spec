# -*- mode: python -*-
a = Analysis(['scanner.py'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='scanner.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
