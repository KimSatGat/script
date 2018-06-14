# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['C:\\Users\\김병완\\Desktop\\EClass\\스크립트언어\\텀프로젝트\\텀프로젝트'],
             binaries=[],
             datas=[],
             hiddenimports=['queue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
