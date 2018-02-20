# -*- mode: python -*-

block_cipher = None

a = Analysis(['bin/app'],
             pathex=['.'],
             binaries=None,
             datas=[],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='app',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='resources\\icons\\app.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='app')

app = BUNDLE(coll,
             name='App.app',
             icon='resources/icons/app.icns',
             bundle_identifier=None)
